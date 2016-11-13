import os, time, re
import json
import mimetypes
import traceback, logging

import requests

from .. import config, utils
from ..returnvalues import ReturnValue

logger = logging.getLogger('itchat')

def load_messages(core):
    core.send_raw_msg = send_raw_msg
    core.send_msg     = send_msg
    core.upload_file  = upload_file
    core.send_file    = send_file
    core.send_image   = send_image
    core.send_video   = send_video
    core.send         = send

def get_download_fn(core, url, msgId):
    def download_fn(downloadDir=None):
        params = {
            'msgid': msgId,
            'skey': core.loginInfo['skey'],}
        headers = { 'User-Agent' : config.USER_AGENT }
        r = core.s.get(url, params=params, stream=True, headers = headers)
        tempStorage = io.BytesIO()
        for block in r.iter_content(1024):
            tempStorage.write(block)
        if downloadDir is None: return tempStorage.getvalue()
        with open(downloadDir, 'wb') as f: f.write(tempStorage.getvalue())
        return ReturnValue({'BaseResponse': {
            'ErrMsg': 'Successfully downloaded',
            'Ret': 0, }})
    return download_fn

def produce_msg(core, msgList):
    ''' for messages types
     * 40 msg, 43 videochat, 50 VOIPMSG, 52 voipnotifymsg
     * 53 webwxvoipnotifymsg, 9999 sysnotice 
    '''
    rl = []
    srl = [40, 43, 50, 52, 53, 9999]
    for m in msgList:
        if '@@' in m['FromUserName'] or '@@' in m['ToUserName']:
            produce_group_chat(core, m)
        else:
            utils.msg_formatter(m, 'Content')
        if m['MsgType'] == 1: # words
            if m['Url']:
                regx = r'(.+?\(.+?\))'
                data = re.search(regx, m['Content'])
                data = 'Map' if data is None else data.group(1)
                msg = {
                    'Type': 'Map',
                    'Text': data,}
            else:
                msg = {
                    'Type': 'Text',
                    'Text': m['Content'],}
        elif m['MsgType'] == 3 or m['MsgType'] == 47: # picture
            download_fn = get_download_fn(core, 
                '%s/webwxgetmsgimg' % core.loginInfo['url'], m['NewMsgId'])
            msg = {
                'Type'     : 'Picture',
                'FileName' : '%s.%s'%(time.strftime('%y%m%d-%H%M%S', time.localtime()),
                    'png' if m['MsgType'] == 3 else 'gif'),
                'Text'     : download_fn, }
        elif m['MsgType'] == 34: # voice
            download_fn = get_download_fn(core,
                '%s/webwxgetvoice' % core.loginInfo['url'], m['NewMsgId'])
            msg = {
                'Type': 'Recording',
                'FileName' : '%s.mp4' % time.strftime('%y%m%d-%H%M%S', time.localtime()),
                'Text': download_fn,}
        elif m['MsgType'] == 37: # friends
            msg = {
                'Type': 'Friends',
                'Text': {
                    'status'        : m['Status'],
                    'userName'      : m['RecommendInfo']['UserName'],
                    'ticket'        : m['Ticket'],
                    'userInfo' : m['RecommendInfo'], }, }
        elif m['MsgType'] == 42: # name card
            msg = {
                'Type': 'Card',
                'Text': m['RecommendInfo'], }
        elif m['MsgType'] == 49: # sharing
            if m['AppMsgType'] == 6:
                msg = m
                cookiesList = {name:data for name,data in core.s.cookies.items()}
                def download_atta(attaDir=None):
                    url = core.loginInfo['fileUrl'] + '/webwxgetmedia'
                    params = {
                        'sender': msg['FromUserName'],
                        'mediaid': msg['MediaId'],
                        'filename': msg['FileName'],
                        'fromuser': core.loginInfo['wxuin'],
                        'pass_ticket': 'undefined',
                        'webwx_data_ticket': cookiesList['webwx_data_ticket'],}
                    headers = { 'User-Agent' : config.USER_AGENT }
                    r = core.s.get(url, params=params, stream=True, headers=headers)
                    tempStorage = io.BytesIO()
                    for block in r.iter_content(1024):
                        tempStorage.write(block)
                    if attaDir is None: return tempStorage.getvalue()
                    with open(attaDir, 'wb') as f: f.write(tempStorage.getvalue())
                    return ReturnValue({'BaseResponse': {
                        'ErrMsg': 'Successfully downloaded',
                        'Ret': 0, }})
                msg = {
                    'Type': 'Attachment',
                    'Text': download_atta, }
            elif m['AppMsgType'] == 17:
                msg = {
                    'Type': 'Note',
                    'Text': m['FileName'], }
            elif m['AppMsgType'] == 2000:
                regx = r'\[CDATA\[(.+?)\][\s\S]+?\[CDATA\[(.+?)\]'
                data = re.search(regx, m['Content'])
                if data:
                    data = data.group(2).split(u'\u3002')[0]
                else:
                    data = 'You may found detailed info in Content key.'
                msg = {
                    'Type': 'Note',
                    'Text': data, }
            else:
                msg = {
                    'Type': 'Sharing',
                    'Text': m['FileName'], }
        elif m['MsgType'] == 51: # phone init
            msg = {
                'Type': 'Init',
                'Text': m['ToUserName'], }
        elif m['MsgType'] == 62: # tiny video
            msgId = m['MsgId']
            def download_video(videoDir=None):
                url = '%s/webwxgetvideo' % core.loginInfo['url']
                params = {
                    'msgid': msgId,
                    'skey': core.loginInfo['skey'],}
                headers = {'Range': 'bytes=0-', 'User-Agent' : config.USER_AGENT }
                r = core.s.get(url, params=params, headers=headers, stream=True)
                tempStorage = io.BytesIO()
                for block in r.iter_content(1024):
                    tempStorage.write(block)
                if videoDir is None: return tempStorage.getvalue()
                with open(videoDir, 'wb') as f: f.write(tempStorage.getvalue())
                return ReturnValue({'BaseResponse': {
                    'ErrMsg': 'Successfully downloaded',
                    'Ret': 0, }})
            msg = {
                'Type': 'Video',
                'FileName' : '%s.mp4' % time.strftime('%y%m%d-%H%M%S', time.localtime()),
                'Text': download_video, }
        elif m['MsgType'] == 10000:
            msg = {
                'Type': 'Note',
                'Text': m['Content'],}
        elif m['MsgType'] == 10002:
            regx = r'\[CDATA\[(.+?)\]\]'
            data = re.search(regx, m['Content'])
            data = 'System message' if data is None else data.group(1).replace('\\', '')
            msg = {
                'Type': 'Note',
                'Text': data, }
        elif m['MsgType'] in srl:
            msg = {
                'Type': 'Useless',
                'Text': 'UselessMsg', }
        else:
            logger.debug('MsgType Unknown: %s\n%s' % (m['MsgType'], str(m)))
            msg = {
                'Type': 'Useless',
                'Text': 'UselessMsg', }
        m = dict(m, **msg)
        rl.append(m)
    return rl

def produce_group_chat(core, msg):
    r = re.match('(@[0-9a-z]*?):<br/>(.*)$', msg['Content'])
    if not r: return
    actualUserName, content = r.groups()
    chatroom = core.storageClass.search_chatrooms(userName=msg['FromUserName'])
    member = utils.search_dict_list((chatroom or {}).get(
        'MemberList') or [], 'UserName', actualUserName)
    if member is None:
        chatroom = core.update_chatroom(msg['FromUserName'])
        member = utils.search_dict_list((chatroom or {}).get(
            'MemberList') or [], 'UserName', actualUserName)
    msg['ActualUserName'] = actualUserName
    msg['ActualNickName'] = member['DisplayName'] or member['NickName']
    msg['Content']        = content
    utils.msg_formatter(msg, 'Content')
    atFlag = '@' + (chatroom['self']['DisplayName']
        or core.storageClass.nickName)
    msg['isAt'] = (
        (atFlag + (u'\u2005' if u'\u2005' in msg['Content'] else ' '))
        in msg['Content']
        or
        msg['Content'].endswith(atFlag))

def send_raw_msg(self, msgType, content, toUserName):
    url = '%s/webwxsendmsg' % self.loginInfo['url']
    payloads = {
        'BaseRequest': self.loginInfo['BaseRequest'],
        'Msg': {
            'Type': msgType,
            'Content': content,
            'FromUserName': self.storageClass.userName,
            'ToUserName': (toUserName if toUserName else self.storageClass.userName),
            'LocalID': self.loginInfo['msgid'],
            'ClientMsgId': self.loginInfo['msgid'],
            }, }
    self.loginInfo['msgid'] += 1
    headers = { 'ContentType': 'application/json; charset=UTF-8', 'User-Agent' : config.USER_AGENT }
    r = self.s.post(url, headers=headers,
        data=json.dumps(payloads, ensure_ascii=False).encode('utf8'))
    return ReturnValue(rawResponse=r)

def send_msg(self, msg='Test Message', toUserName=None):
    r = self.send_raw_msg(1, msg, toUserName)
    return r

def upload_file(self, fileDir, isPicture=False, isVideo=False):
    if not utils.check_file(fileDir):
        return ReturnValue({'BaseResponse': {
            'ErrMsg': 'No file found in specific dir',
            'Ret': -1002, }})
    url = self.loginInfo.get('fileUrl', self.loginInfo['url']) + \
        '/webwxuploadmedia?f=json'
    # save it on server
    fileSize = str(os.path.getsize(fileDir))
    cookiesList = {name:data for name,data in self.s.cookies.items()}
    fileType = mimetypes.guess_type(fileDir)[0] or 'application/octet-stream'
    files = {
        'id': (None, 'WU_FILE_0'),
        'name': (None, os.path.basename(fileDir)),
        'type': (None, fileType),
        'lastModifiedDate': (None, time.strftime('%a %b %d %Y %H:%M:%S GMT+0800 (CST)')),
        'size': (None, fileSize),
        'mediatype': (None, 'pic' if isPicture else 'video' if isVideo else'doc'),
        'uploadmediarequest': (None, json.dumps({
            'BaseRequest': self.loginInfo['BaseRequest'],
            'ClientMediaId': int(time.time()),
            'TotalLen': fileSize,
            'StartPos': 0,
            'DataLen': fileSize,
            'MediaType': 4, }, separators = (',', ':'))),
        'webwx_data_ticket': (None, cookiesList['webwx_data_ticket']),
        'pass_ticket': (None, 'undefined'),
        'filename' : (os.path.basename(fileDir), open(fileDir, 'rb'), fileType), }
    headers = { 'User-Agent' : config.USER_AGENT }
    r = self.s.post(url, files=files, headers=headers)
    return ReturnValue(rawResponse=r)

def send_file(self, fileDir, toUserName=None, mediaId=None):
    if toUserName is None: toUserName = self.storageClass.userName
    if mediaId is None:
        r = self.upload_file(fileDir)
        if r:
            mediaId = r['MediaId']
        else:
            return r
    url = '%s/webwxsendappmsg?fun=async&f=json' % self.loginInfo['url']
    data = {
        'BaseRequest': self.loginInfo['BaseRequest'],
        'Msg': {
            'Type': 6,
            'Content': ("<appmsg appid='wxeb7ec651dd0aefa9' sdkver=''><title>%s</title>"%os.path.basename(fileDir) +
                "<des></des><action></action><type>6</type><content></content><url></url><lowurl></lowurl>" +
                "<appattach><totallen>%s</totallen><attachid>%s</attachid>"%(str(os.path.getsize(fileDir)), mediaId) +
                "<fileext>%s</fileext></appattach><extinfo></extinfo></appmsg>"%os.path.splitext(fileDir)[1].replace('.','')),
            'FromUserName': self.storageClass.userName,
            'ToUserName': toUserName,
            'LocalID': self.loginInfo['msgid'],
            'ClientMsgId': self.loginInfo['msgid'], }, }
    self.loginInfo['msgid'] += 1
    headers = {
        'User-Agent': config.USER_AGENT,
        'Content-Type': 'application/json;charset=UTF-8', }
    r = self.s.post(url, headers=headers,
        data=json.dumps(data, ensure_ascii=False).encode('utf8'))
    return ReturnValue(rawResponse=r)

def send_image(self, fileDir, toUserName=None, mediaId=None):
    if toUserName is None: toUserName = self.storageClass.userName
    if mediaId is None:
        r = self.upload_file(fileDir, isPicture=not fileDir[-4:] == '.gif')
        if r:
            mediaId = r['MediaId']
        else:
            return r
    url = '%s/webwxsendmsgimg?fun=async&f=json' % self.loginInfo['url']
    data = {
        'BaseRequest': self.loginInfo['BaseRequest'],
        'Msg': {
            'Type': 3,
            'MediaId': mediaId,
            'FromUserName': self.storageClass.userName,
            'ToUserName': toUserName,
            'LocalID': self.loginInfo['msgid'],
            'ClientMsgId': self.loginInfo['msgid'], }, }
    self.loginInfo['msgid'] += 1
    if fileDir[-4:] == '.gif':
        url = '%s/webwxsendemoticon?fun=sys' % self.loginInfo['url']
        data['Msg']['Type'] = 47
        data['Msg']['EmojiFlag'] = 2
    headers = {
        'User-Agent': config.USER_AGENT,
        'Content-Type': 'application/json;charset=UTF-8', }
    r = self.s.post(url, headers=headers,
        data=json.dumps(data, ensure_ascii=False).encode('utf8'))
    return ReturnValue(rawResponse=r)

def send_video(self, fileDir=None, toUserName=None, mediaId=None):
    if toUserName is None: toUserName = self.storageClass.userName
    if mediaId is None:
        r = self.upload_file(fileDir, isVideo=True)
        if r:
            mediaId = r['MediaId']
        else:
            return r
    url = '%s/webwxsendvideomsg?fun=async&f=json&pass_ticket=%s' % (
        self.loginInfo['url'], self.loginInfo['pass_ticket'])
    data = {
        'BaseRequest': self.loginInfo['BaseRequest'],
        'Msg': {
            'Type'         : 43,
            'MediaId'      : mediaId,
            'FromUserName' : self.storageClass.userName,
            'ToUserName'   : toUserName,
            'LocalID'      : self.loginInfo['msgid'],
            'ClientMsgId'  : self.loginInfo['msgid'], },
        'Scene': 0, }
    self.loginInfo['msgid'] += 1
    headers = {
        'User-Agent' : config.USER_AGENT,
        'Content-Type': 'application/json;charset=UTF-8', }
    r = self.s.post(url, headers=headers,
        data=json.dumps(data, ensure_ascii=False).encode('utf8'))
    return ReturnValue(rawResponse=r)

def send(self, msg, toUserName=None, mediaId=None):
    if not msg:
        r = ReturnValue({'BaseResponse': {
            'ErrMsg': 'No message.',
            'Ret': -1005, }})
    elif msg[:5] == '@fil@':
        if mediaId is None:
            r = self.send_file(msg[5:], toUserName)
        else:
            r = self.send_file(msg[5:], toUserName, mediaId)
    elif msg[:5] == '@img@':
        if mediaId is None:
            r = self.send_image(msg[5:], toUserName)
        else:
            r = self.send_image(msg[5:], toUserName, mediaId)
    elif msg[:5] == '@msg@':
        r = self.send_msg(msg[5:], toUserName)
    elif msg[:5] == '@vid@':
        if mediaId is None:
            r = self.send_video(msg[5:], toUserName)
        else:
            r = self.send_video(msg[5:], toUserName, mediaId)
    else:
        r = self.send_msg(msg, toUserName)
    return r
