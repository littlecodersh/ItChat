import requests, time, re
import os, sys
import thread
import json, xml.dom.minidom
import config, storage, out, log
from QRCode import QRCode

BASE_URL = config.BASE_URL
CMD_QRCODE = True
DEBUG = False

class WeChatClient:
    def __init__(self, storageClass = None):
        self.storageClass = storageClass if storageClass else storage.Storage()
        self.msgStorage = self.storageClass.msgList
        self.loginInfo = self.storageClass.loginInfo
        self.s = requests.Session()
        self.uuid = None
        self.userName = None
    def login(self):
        out.print_line('Getting uuid\r')
        while self.get_QRuuid(): time.sleep(1)
        out.print_line('Getting QR Code\r')
        self.get_QR()
        out.print_line('Please scan the QR Code\r')
        while self.check_login(): time.sleep(1)
        self.web_init()
        self.show_mobile_login()
        self.get_contract()
        out.print_line('Login successfully as %s\n'%self.find_nickname(self.userName))
        thread.start_new_thread(self.maintain_loop, ())
    def get_QRuuid(self):
        url = '%s/jslogin'%BASE_URL
        payloads = {
            'appid': 'wx782c26e4c19acffb',
            'fun': 'new',
        }
        r = self.s.get(url, params = payloads)

        regx = r'window.QRLogin.code = (\d+); window.QRLogin.uuid = "(\S+?)";'
        data = re.search(regx, r.text)
        if data and data.group(1) == '200': self.uuid = data.group(2);return False
        # continous failing
    def get_QR(self):
        url = '%s/qrcode/%s'%(BASE_URL, self.uuid)
        r = self.s.get(url, stream = True)# params = payloads, headers = HEADER, 
        with open('QR.jpg', 'wb') as f: f.write(r.content)
        if CMD_QRCODE:
            q = QRCode('QR.jpg', 37, 3, 'BLACK')
            q.print_qr()
        elif sys.platform.find('darwin') >= 0:
            subprocess.call(['open', 'QR.jpg'])
        elif sys.platform.find('linux') >= 0:
            subprocess.call(['xdg-open', 'QR.jpg'])
        else:
            os.startfile('QR.jpg')
    def check_login(self):
        url = '%s/cgi-bin/mmwebwx-bin/login'%BASE_URL
        # add tip so that we can get many reply, use string payloads to avoid auto-urlencode
        payloads = 'tip=1&uuid=%s&_=%s'%(self.uuid, int(time.time()))
        r = self.s.get(url, params = payloads)
        regx = r'window.code=(\d+)'
        data = re.search(regx, r.text)
        if data and data.group(1) == '200':
            regx = r'window.redirect_uri="(\S+)";'
            self.loginInfo['url'] = re.search(regx, r.text).group(1)
            r = self.s.get(self.loginInfo['url'], allow_redirects=False)
            self.loginInfo['url'] = self.loginInfo['url'][:self.loginInfo['url'].rfind('/')]
            self.get_login_info(r.text)
            return False
        if data and data.group(1) == '201':
            out.print_line(' '*40 + '\rPlease press confirm')
        if data and data.group(1) == '408':
            out.print_line(' '*40 + '\rReloading QR Code')
            while self.get_QRuuid(): time.sleep(1)
            self.get_QR()
        return True
    def get_login_info(self, s):
        self.loginInfo['BaseRequest'] = {}
        for node in xml.dom.minidom.parseString(s).documentElement.childNodes:
            if node.nodeName == 'skey':
                self.loginInfo['skey'] = self.loginInfo['BaseRequest']['Skey'] = node.childNodes[0].data.encode('utf8')
            elif node.nodeName == 'wxsid':
                self.loginInfo['wxsid'] = self.loginInfo['BaseRequest']['Sid'] = node.childNodes[0].data.encode('utf8')
            elif node.nodeName == 'wxuin':
                self.loginInfo['wxuin'] = self.loginInfo['BaseRequest']['Uin'] = node.childNodes[0].data.encode('utf8')
            elif node.nodeName == 'pass_ticket':
                self.loginInfo['pass_ticket'] = self.loginInfo['BaseRequest']['DeviceID'] = node.childNodes[0].data.encode('utf8')
    def web_init(self):
        url = '%s/webwxinit?r=%s' % (self.loginInfo['url'], int(time.time()))
        payloads = {
            'BaseRequest': self.loginInfo['BaseRequest']
        }
        headers = { 'ContentType': 'application/json; charset=UTF-8' }
        r = self.s.post(url, data = json.dumps(payloads), headers = headers)
        dic = json.loads(r.content.decode('utf-8', 'replace'))
        self.userName = dic['User']['UserName']
        if DEBUG:
            with open('userName.txt', 'w') as f: f.write(self.userName)
        self.loginInfo['SyncKey'] = dic['SyncKey']
        self.loginInfo['synckey'] = '|'.join(['%s_%s' % (item['Key'], item['Val']) for item in dic['SyncKey']['List']])
    def get_contract(self):
        url = '%s/webwxgetcontact?r=%s&seq=0&skey=%s' % (self.loginInfo['url'],
            int(time.time()), self.loginInfo['skey'])
        headers = { 'ContentType': 'application/json; charset=UTF-8' }
        r = self.s.get(url, headers = headers)
        self.memberList = json.loads(r.content.decode('utf-8', 'replace'))['MemberList']
        i = 1
        while i != 0:
            i = 0
            for m in self.memberList:
                if m['Sex'] == 0 or m['Sex'] == '0': self.memberList.remove(m);i+=1
        if DEBUG:
            with open('MemberList.txt', 'w') as f: f.write(str(self.memberList))
    def show_mobile_login(self):
        url = '%s/webwxstatusnotify'%self.loginInfo['url']
        payloads = {
                'BaseRequest': self.loginInfo['BaseRequest'],
                'Code': 3,
                'FromUserName': self.userName,
                'ToUserName': self.userName,
                'ClientMsgId': int(time.time()),
                }
        headers = { 'ContentType': 'application/json; charset=UTF-8' }
        r = self.s.post(url, data = json.dumps(payloads), headers = headers)
    def maintain_loop(self):
        i = self.sync_check()
        count = 0
        while i and count <4:
            try:
                # ISSUE 1
                if i != '0': msgList = self.get_msg()
                if msgList: self.store_msg(msgList)
                time.sleep(3)
                i = self.sync_check()
                count = 0
            except:
                count += 1
                log.log('Exception%s'%count, False)
                time.sleep(count*3)
        # Issue 2
        log.log('LOG OUT', False)
        raise Exception('Log out')
    def sync_check(self):
        url = '%s/synccheck'%self.loginInfo['url']
        payloads = {
                'r': int(time.time()),
                'skey': self.loginInfo['skey'],
                'sid': self.loginInfo['wxsid'],
                'uin': self.loginInfo['wxuin'],
                'deviceid': self.loginInfo['pass_ticket'],
                'synckey': self.loginInfo['synckey'],
                }
        r = self.s.get(url, params = payloads)

        regx = r'window.synccheck={retcode:"(\d+)",selector:"(\d+)"}'
        pm = re.search(regx, r.text)

        if pm.group(1) != '0' : return None
        return pm.group(2)
    def get_msg(self):
        url = '%s/webwxsync?sid=%s&skey=%s'%(
            self.loginInfo['url'], self.loginInfo['wxsid'], self.loginInfo['skey'])
        payloads = {
            'BaseRequest': self.loginInfo['BaseRequest'],
            'SyncKey': self.loginInfo['SyncKey'],
            'rr': int(time.time())
            }
        headers = { 'ContentType': 'application/json; charset=UTF-8' }
        r = self.s.post(url, data = json.dumps(payloads), headers = headers)

        dic = json.loads(r.content.decode('utf-8', 'replace'))
        self.loginInfo['SyncKey'] = dic['SyncKey']
        if dic['AddMsgCount'] != 0: return dic['AddMsgList']
        return None
    def store_msg(self, l):
        for m in l:
        # Issue 2
            if m['FromUserName'] == self.userName: continue
            self.msgStorage.append(m)
            # msg = '%s: %s'%(self.find_nickname(m['FromUserName']), m['Content'])
    def send_msg(self, toUserName = None, msg = 'Test Message'):
        if self.find_user(toUserName): toUserName = self.find_user(toUserName) 
        url = '%s/webwxsendmsg'%self.loginInfo['url']
        payloads = {
                'BaseRequest': self.loginInfo['BaseRequest'],
                'Msg': {
                    'Type': 1,
                    'Content': msg.encode('utf8') if isinstance(msg, unicode) else msg,
                    'FromUserName': self.userName.encode('utf8'),
                    'ToUserName': (toUserName if toUserName else self.userName).encode('utf8'),
                    'LocalID': int(time.time()),
                    'ClientMsgId': int(time.time()),
                    },
                }
        data = json.dumps(payloads, ensure_ascii = False)
        headers = { 'ContentType': 'application/json; charset=UTF-8' }
        r = self.s.post(url, data = json.dumps(payloads, ensure_ascii = False), headers = headers)
    def storage(self):
        return self.msgStorage
    # will be move to tools
    def find_user(self, n):
        for i in self.memberList:
            if i['NickName'] == n: return i['UserName']
    def find_nickname(self, u):
        for i in self.memberList:
            if i['UserName'] == u: return i['NickName']
