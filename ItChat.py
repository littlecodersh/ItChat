#coding=utf8
import requests, time, re
import os
import json, xml.dom.minidom
import codecs

BASE_URL = 'https://login.weixin.qq.com'
class ItChat:
    def __init__(self):
        self.s = requests.Session()
        self.uuid = None
        self.loginInfo = {}
        self.userName = None
        self.heihei = 0
        self.load()
    def load(self):
        while self.get_QRuuid(): time.sleep(1)
        self.get_QR()
        while self.check_login(): time.sleep(1)
        self.web_init()
        self.show_mobile_login()
        self.get_contract()
        self.polling()
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
        print 'QRCode Retry'; return True
    def get_QR(self):
        url = '%s/qrcode/%s'%(BASE_URL, self.uuid)
        r = self.s.get(url, stream = True)# params = payloads, headers = HEADER, 
        with open('QR.jpg', 'wb') as f: f.write(r.content)
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
        return True
    def get_login_info(self, s):
        self.loginInfo['BaseRequest'] = {}
        for node in xml.dom.minidom.parseString(s).documentElement.childNodes:
            if node.nodeName == 'skey':
                self.loginInfo['skey'] = self.loginInfo['BaseRequest']['Skey'] = node.childNodes[0].data
            elif node.nodeName == 'wxsid':
                self.loginInfo['wxsid'] = self.loginInfo['BaseRequest']['Sid'] = node.childNodes[0].data
            elif node.nodeName == 'wxuin':
                self.loginInfo['wxuin'] = self.loginInfo['BaseRequest']['Uin'] = node.childNodes[0].data
            elif node.nodeName == 'pass_ticket':
                self.loginInfo['pass_ticket'] = self.loginInfo['BaseRequest']['DeviceID'] = node.childNodes[0].data
    def web_init(self):
        url = '%s/webwxinit?r=%s' % (self.loginInfo['url'], int(time.time()))
        payloads = {
            'BaseRequest': self.loginInfo['BaseRequest']
        }
        headers = { 'ContentType': 'application/json; charset=UTF-8' }
        r = self.s.post(url, data = json.dumps(payloads), headers = headers)
        dic = json.loads(r.content.decode('utf-8', 'replace'))
        self.userName = dic['User']['UserName']
        self.loginInfo['SyncKey'] = dic['SyncKey']
        self.loginInfo['synckey'] = '|'.join(['%s_%s' % (item['Key'], item['Val'])
                        for item in dic['SyncKey']['List']])
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
    def polling(self):
        print 'Start Polling'
        i = self.sync_check()
        while i:
            i = self.sync_check()
            if i != '0': msgList = self.get_msg()
            if msgList: self.print_msg(msgList)
            time.sleep(3)
        print 'LOGOUT'
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
    def print_msg(self, l):
        for m in l:
            if m['FromUserName'] == self.userName: continue
            print '%s: %s'%(self.find_nickname(m['FromUserName']), m['Content'])
            # only for debug, reply the same msg
            self.send_msg(self.find_nickname(m['FromUserName']), 'I received: %s'%m['Content'])
    def send_msg(self, toUserName = None, msg = 'Test Message'):
        url = '%s/webwxsendmsg'%self.loginInfo['url']
        payloads = {
                'BaseRequest': self.loginInfo['BaseRequest'],
                'Msg': {
                    'Type': 1,
                    'Content': msg,
                    'FromUserName': self.userName,
                    'ToUserName': self.find_user(toUserName) if toUserName else self.userName,
                    'LocalID': str(int(time.time())),
                    'ClientMsgId': str(int(time.time())),
                    },
                }
        headers = { 'ContentType': 'application/json; charset=UTF-8' }
        r = self.s.post(url, data = json.dumps(payloads), headers = headers)
    def find_user(self, n):
        for i in self.memberList:
            if i['NickName'] == n: return i['UserName']
    def find_nickname(self, u):
        for i in self.memberList:
            if i['UserName'] == u: return i['NickName']

if __name__ == '__main__':
    c = ItChat()
