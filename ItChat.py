#coding=utf8
import requests, time, re
import os
import time

BASE_URL = 'https://login.weixin.qq.com'
class GeekChat:
    def __init__(self):
        self.uuid = None
        self.s = requests.Session()
    def get_QRuuid(self):
        url = '%s/jslogin'%BASE_URL
        payloads = {
            'appid': 'wx782c26e4c19acffb',
            'fun': 'new',
            # '_': int(time.time()),
        }
        r = self.s.get(url, params = payloads)

        regx = r'window.QRLogin.code = (\d+); window.QRLogin.uuid = "(\S+?)";'
        data = re.search(regx, r.text)
        if data and data.group(1) == '200': self.uuid = data.group(2);return
        raise Exception('get_QRuuid Failed')
    def get_QR(self):
        url = '%s/qrcode/%s'%(BASE_URL, self.uuid)
        r = self.s.get(url, stream = True)# params = payloads, headers = HEADER, 
        with open('QR.jpg', 'wb') as f: f.write(r.content)
        os.startfile('QR.jpg')
    def check_login(self):
        url = '%s/cgi-bin/mmwebwx-bin/login'%BASE_URL
        # add tip so that we can get many reply, use string payload to avoid auto-urlencode
        payloads = 'tip=1&uuid=%s&_=%s'%(self.uuid, int(time.time()))
        r = self.s.get(url, params = payloads)
        regx = r'window.code=(\d+)'
        data = re.search(regx, r.text)
        if data and data.group(1) == '200':
            regx = r'window.redirect_uri="(\S+)";'
            r = self.s.get(re.search(regx, r.text).group(1)+'&fun=new')
            with open('get.txt', 'wb') as f: f.write(r.content)
            return False
        return True

if __name__ == '__main__':
    g = GeekChat()
    g.get_QRuuid()
    g.get_QR()
    while g.check_login(): time.sleep(1)
    print 'Done'
