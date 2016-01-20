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
        self.heihei = '@e0da87603081255d7bc7648afb25bd7604f7d716542caff1f16c352dbd401832'
        self.load()
    def load(self):
        while c.get_QRuuid(): time.sleep(1)
        c.get_QR()
        while c.check_login(): time.sleep(1)
        c.web_init()
        c.get_contract()
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
        # with codecs.open('contractList.txt', 'w', 'utf-8') as f: f.write(str(self.memberList).encode('utf-8','replace'))
        # with codecs.open('contract.txt', 'w', 'utf-8') as f:
        #     for m in self.memberList: f.write(m['NickName']+u' '+str(m['Sex'])+u'\n')
    def send_msg(self, toUserName = self.userName, msg = 'Test Message'):
        url = '%s/webwxsendmsg'%self.loginInfo['url']
        payloads = {
                'BaseRequest': self.loginInfo['BaseRequest'],
                'Msg': {
                    'Type': 1,
                    'Content': msg,
                    'FromUserName': self.userName,
                    'ToUserName': self.find_user(toUserName),
                    'LocalID': str(int(time.time())),
                    'ClientMsgId': str(int(time.time())),
                    },
                }
        headers = { 'ContentType': 'application/json; charset=UTF-8' }
        r = self.s.post(url, data = json.dumps(payloads), headers = headers)
        print r.text
    def find_user(self, u):
        for i in self.memberList:
            if i['NickName'] == u: return i['UserName']

if __name__ == '__main__':
    c = ItChat()
    for i in range(20):
        c.send_msg(msg = 'Yo~ *%s'%i)
        time.sleep(1)
