import os, sys, time, re, io
import threading
import json, xml.dom.minidom
import copy, pickle, random
import traceback, logging

import requests

from .. import config, utils
from ..returnvalues import ReturnValue
from .contact import update_local_chatrooms
from .messages import produce_msg

logger = logging.getLogger('itchat')

def load_login(core):
    core.login             = login
    core.get_QRuuid        = get_QRuuid
    core.get_QR            = get_QR
    core.check_login       = check_login
    core.web_init          = web_init
    core.show_mobile_login = show_mobile_login
    core.start_receiving   = start_receiving
    core.get_msg           = get_msg
    core.logout            = logout

def login(self, enableCmdQR=False, picDir=None, qrCallback=None,
        loginCallback=None, exitCallback=None):
    if self.alive:
        logger.debug('itchat has already logged in.')
        return
    while 1:
        for getCount in range(10):
            logger.info('Getting uuid of QR code.')
            while not self.get_QRuuid(): time.sleep(1)
            logger.info('Downloading QR code.')
            qrStorage = self.get_QR(enableCmdQR=enableCmdQR,
                picDir=picDir, qrCallback=qrCallback)
            if qrStorage:
                break
            elif 9 == getCount:
                logger.info('Failed to get QR code, please restart the program.')
                sys.exit()
        logger.info('Please scan the QR code to log in.')
        isLoggedIn = False
        while not isLoggedIn:
            status = self.check_login()
            if hasattr(qrCallback, '__call__'):
                qrCallback(uuid=self.uuid, status=status, qrcode=qrStorage.getvalue())
            if status == '200':
                isLoggedIn = True
            elif status == '201':
                if isLoggedIn is not None:
                    logger.info('Please press confirm on your phone.')
                    isLoggedIn = None
            elif status != '408':
                break
        if isLoggedIn: break
        logger.info('Log in time out, reloading QR code')
    self.web_init()
    self.show_mobile_login()
    self.get_contact(True)
    if hasattr(loginCallback, '__call__'):
        r = loginCallback()
    else:
        utils.clear_screen()
        if os.path.exists(picDir or config.DEFAULT_QR):
            os.remove(picDir or config.DEFAULT_QR)
        logger.info('Login successfully as %s' % self.storageClass.nickName)
    self.start_receiving(exitCallback)

def get_QRuuid(self):
    url = '%s/jslogin' % config.BASE_URL
    params = {
        'appid' : 'wx782c26e4c19acffb',
        'fun'   : 'new', }
    headers = { 'User-Agent' : config.USER_AGENT }
    r = self.s.get(url, params=params, headers=headers)
    regx = r'window.QRLogin.code = (\d+); window.QRLogin.uuid = "(\S+?)";'
    data = re.search(regx, r.text)
    if data and data.group(1) == '200':
        self.uuid = data.group(2)
        return self.uuid

def get_QR(self, uuid=None, enableCmdQR=False, picDir=None, qrCallback=None):
    uuid = uuid or self.uuid
    picDir = picDir or config.DEFAULT_QR
    url = '%s/qrcode/%s' % (config.BASE_URL, uuid)
    headers = { 'User-Agent' : config.USER_AGENT }
    try:
        r = self.s.get(url, stream=True, headers=headers)
    except:
        return False
    qrStorage = io.BytesIO(r.content)
    if hasattr(qrCallback, '__call__'):
        qrCallback(uuid=uuid, status='0', qrcode=qrStorage.getvalue())
    else:
        with open(picDir, 'wb') as f: f.write(r.content)
        if enableCmdQR:
            utils.print_cmd_qr(picDir, enableCmdQR=enableCmdQR)
        else:
            utils.print_qr(picDir)
    return qrStorage

def check_login(self, uuid=None):
    uuid = uuid or self.uuid
    url = '%s/cgi-bin/mmwebwx-bin/login' % config.BASE_URL
    localTime = int(time.time())
    params = 'loginicon=true&uuid=%s&tip=0&r=%s&_=%s' % (
        uuid, localTime / 1579, localTime)
    headers = { 'User-Agent' : config.USER_AGENT }
    r = self.s.get(url, params=params, headers=headers)
    regx = r'window.code=(\d+)'
    data = re.search(regx, r.text)
    if data and data.group(1) == '200':
        process_login_info(self, r.text)
        return '200'
    elif data:
        return data.group(1)
    else:
        return '400'

def process_login_info(core, loginContent):
    ''' when finish login (scanning qrcode)
     * syncUrl and fileUploadingUrl will be fetched
     * deviceid and msgid will be generated
     * skey, wxsid, wxuin, pass_ticket will be fetched
    '''
    regx = r'window.redirect_uri="(\S+)";'
    core.loginInfo['url'] = re.search(regx, loginContent).group(1)
    headers = { 'User-Agent' : config.USER_AGENT }
    r = core.s.get(core.loginInfo['url'], headers=headers, allow_redirects=False)
    core.loginInfo['url'] = core.loginInfo['url'][:core.loginInfo['url'].rfind('/')]
    for indexUrl, detailedUrl in (
            ("wx2.qq.com"      , ("file.wx2.qq.com", "webpush.wx2.qq.com")),
            ("wx8.qq.com"      , ("file.wx8.qq.com", "webpush.wx8.qq.com")),
            ("qq.com"          , ("file.wx.qq.com", "webpush.wx.qq.com")),
            ("web2.wechat.com" , ("file.web2.wechat.com", "webpush.web2.wechat.com")),
            ("wechat.com"      , ("file.web.wechat.com", "webpush.web.wechat.com"))):
        fileUrl, syncUrl = ['https://%s/cgi-bin/mmwebwx-bin' % url for url in detailedUrl]
        if indexUrl in core.loginInfo['url']:
            core.loginInfo['fileUrl'], core.loginInfo['syncUrl'] = \
                fileUrl, syncUrl
            break
    else:
        core.loginInfo['fileUrl'] = core.loginInfo['syncUrl'] = core.loginInfo['url']
    core.loginInfo['deviceid'] = 'e' + repr(random.random())[2:17]
    core.loginInfo['BaseRequest'] = {}
    for node in xml.dom.minidom.parseString(r.text).documentElement.childNodes:
        if node.nodeName == 'skey':
            core.loginInfo['skey'] = core.loginInfo['BaseRequest']['Skey'] = node.childNodes[0].data
        elif node.nodeName == 'wxsid':
            core.loginInfo['wxsid'] = core.loginInfo['BaseRequest']['Sid'] = node.childNodes[0].data
        elif node.nodeName == 'wxuin':
            core.loginInfo['wxuin'] = core.loginInfo['BaseRequest']['Uin'] = node.childNodes[0].data
        elif node.nodeName == 'pass_ticket':
            core.loginInfo['pass_ticket'] = core.loginInfo['BaseRequest']['DeviceID'] = node.childNodes[0].data

def web_init(self):
    url = '%s/webwxinit?r=%s' % (self.loginInfo['url'], int(time.time()))
    data = { 'BaseRequest': self.loginInfo['BaseRequest'], }
    headers = {
        'ContentType': 'application/json; charset=UTF-8',
        'User-Agent' : config.USER_AGENT, }
    r = self.s.post(url, data=json.dumps(data), headers=headers)
    dic = json.loads(r.content.decode('utf-8', 'replace'))
    utils.emoji_formatter(dic['User'], 'NickName')
    self.loginInfo['InviteStartCount'] = int(dic['InviteStartCount'])
    self.loginInfo['User'] = utils.struct_friend_info(dic['User'])
    self.loginInfo['SyncKey'] = dic['SyncKey']
    self.loginInfo['synckey'] = '|'.join(['%s_%s' % (item['Key'], item['Val'])
        for item in dic['SyncKey']['List']])
    self.storageClass.userName = dic['User']['UserName']
    self.storageClass.nickName = dic['User']['NickName']
    self.memberList.append(dic['User'])
    return dic

def show_mobile_login(self):
    url = '%s/webwxstatusnotify?lang=zh_CN&pass_ticket=%s' % (
        self.loginInfo['url'], self.loginInfo['pass_ticket'])
    data = {
        'BaseRequest'  : self.loginInfo['BaseRequest'],
        'Code'         : 3,
        'FromUserName' : self.storageClass.userName,
        'ToUserName'   : self.storageClass.userName,
        'ClientMsgId'  : int(time.time()), }
    headers = {
        'ContentType': 'application/json; charset=UTF-8',
        'User-Agent' : config.USER_AGENT, }
    r = self.s.post(url, data=json.dumps(data), headers=headers)
    return ReturnValue(rawResponse=r)

def start_receiving(self, exitCallback=None, getReceivingFnOnly=False):
    self.alive = True
    def maintain_loop():
        retryCount = 0
        while self.alive:
            try:
                i = sync_check(self)
                if i is None:
                    self.alive = False
                elif i == '0':
                    continue
                else:
                    msgList, contactList = self.get_msg()
                    if contactList:
                        chatroomList, otherList = [], []
                        for contact in contactList:
                            if '@@' in contact['UserName']:
                                chatroomList.append(contact)
                            else:
                                otherList.append(contact)
                        chatroomMsg = update_local_chatrooms(self, chatroomList)
                        self.msgList.put(chatroomMsg)
                    if msgList:
                        msgList = produce_msg(self, msgList)
                        for msg in msgList: self.msgList.put(msg)
                retryCount = 0
            except:
                retryCount += 1
                logger.debug(traceback.format_exc())
                if self.receivingRetryCount < retryCount:
                    self.alive = False
                else:
                    time.sleep(1)
        self.logout()
        if hasattr(exitCallback, '__call__'):
            exitCallback()
        else:
            logger.info('LOG OUT!')
    if getReceivingFnOnly:
        return maintain_loop
    else:
        maintainThread = threading.Thread(target=maintain_loop)
        maintainThread.setDaemon(True)
        maintainThread.start()

def sync_check(self):
    url = '%s/synccheck' % self.loginInfo.get('syncUrl', self.loginInfo['url'])
    params = {
        'r'        : int(time.time() * 1000),
        'skey'     : self.loginInfo['skey'],
        'sid'      : self.loginInfo['wxsid'],
        'uin'      : self.loginInfo['wxuin'],
        'deviceid' : self.loginInfo['deviceid'],
        'synckey'  : self.loginInfo['synckey'],
        '_'        : int(time.time() * 1000),}
    headers = { 'User-Agent' : config.USER_AGENT }
    r = self.s.get(url, params=params, headers=headers)
    regx = r'window.synccheck={retcode:"(\d+)",selector:"(\d+)"}'
    pm = re.search(regx, r.text)
    if pm is None or pm.group(1) != '0':
        logger.debug('Unexpected sync check result: %s' % r.text)
        return None
    return pm.group(2)

def get_msg(self):
    url = '%s/webwxsync?sid=%s&skey=%s&pass_ticket=%s' % (
        self.loginInfo['url'], self.loginInfo['wxsid'],
        self.loginInfo['skey'],self.loginInfo['pass_ticket'])
    data = {
        'BaseRequest' : self.loginInfo['BaseRequest'],
        'SyncKey'     : self.loginInfo['SyncKey'],
        'rr'          : ~int(time.time()), }
    headers = {
        'ContentType': 'application/json; charset=UTF-8',
        'User-Agent' : config.USER_AGENT }
    r = self.s.post(url, data=json.dumps(data), headers=headers)
    dic = json.loads(r.content.decode('utf-8', 'replace'))
    if dic['BaseResponse']['Ret'] != 0: return None, None
    self.loginInfo['SyncKey'] = dic['SyncCheckKey']
    self.loginInfo['synckey'] = '|'.join(['%s_%s' % (item['Key'], item['Val'])
        for item in dic['SyncCheckKey']['List']])
    return dic['AddMsgList'], dic['ModContactList']

def logout(self):
    if self.alive:
        url = '%s/webwxlogout' % self.loginInfo['url']
        params = {
            'redirect' : 1,
            'type'     : 1,
            'skey'     : self.loginInfo['skey'], }
        headers = { 'User-Agent' : config.USER_AGENT }
        self.s.get(url, params=params, headers=headers)
        self.alive = False
    self.s.cookies.clear()
    del self.chatroomList[:]
    del self.memberList[:]
    del self.mpList[:]
    return ReturnValue({'BaseResponse': {
        'ErrMsg': 'logout successfully.',
        'Ret': 0, }})
