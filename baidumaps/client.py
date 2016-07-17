# -*- coding: utf-8 -*-
# The MIT License (MIT)
# Copyright © 2015 Eli Song

# Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the “Software”), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

import sys
PY2 = sys.version[0] == '2'
import urllib
if not PY2: import urllib.parse
import requests
import re
import baidumaps
from baidumaps import apis
from baidumaps import exceptions
from baidumaps import parse
# import apis
# import exceptions
# import parse


class Client(object):
    def __init__(self, ak=None, domain='http://api.map.baidu.com',
                 output='json'):
        if not ak:
            raise ValueError("Must provide API when creating client. Refer to\
                             the link: http://lbsyun.baidu.com/apiconsole/key")

        if ak and not re.search(r'^[a-zA-Z0-9]+$', ak):
            raise ValueError('Invalid ak(API key)!')

        self.ak = ak
        self.domain = domain
        self.output = output

    def get(self, params):
        request_url = self.generate_url(params)
        response = requests.get(request_url).json()

        status = response['status']
        server_name = params['server_name']
        subserver_name = params['subserver_name']
        if status != 0:
            raise exceptions.StatusError(server_name, subserver_name, status)
        elif 'raw' in params and params['raw']:
            result = response
        else:
            result = self.parse(server_name, subserver_name, response)
        return result

    def generate_url(self, params):
        base_url = '/'.join([self.domain,
                            params['server_name'],
                            params['version'],
                            params['subserver_name']]
                            ) + '?'
        base_url = re.sub(r'//ip', '/ip', base_url)   # for ip_locate()

        temp = params.copy()    # avoid altering argument 'params'
        {temp.pop(key) for key in ['server_name', 'version', 'subserver_name']}
        temp.update({'ak': self.ak, 'output': self.output})
        addi_url = urllib.urlencode(temp) if PY2 else urllib.parse.urlencode(temp)
        # addi_url = urllib.urlencode(temp)

        return base_url + addi_url


Client.place_search = apis.place_search
Client.place_detail = apis.place_detail
Client.place_eventsearch = apis.place_eventsearch
Client.place_eventdetail = apis.place_eventdetail
Client.place_suggest = apis.place_suggest
Client.geocode = apis.geocode
Client.direct = apis.direct
Client.ip_locate = apis.ip_locate
Client.route_matrix = apis.route_matrix
Client.geoconv = apis.geoconv
Client.parse = parse.parse


if __name__ == "__main__":
    bdmaps = Client(ak='cQlzSOBQEZGTbhHTbeUMcTU62vakzrvF')
    # result = bdmaps.geoconv('114.21892734521,29.575429778924')
    result = bdmaps.direct('华翰科技','侯斯顿','transit',region='深圳')
    mymsg = ''
    content = ''
    for i in range(len(result['routes'])):
        scheme = result['routes'][i]
        content += '[方案%d]: 从华翰科技'%(i+1)
        timeout = 0
        for steplist in scheme['steps']:
            step = steplist[0]
            if step['type']==5:
                content += ' '
                if PY2:
                    content += step['stepInstruction'].encode('utf-8')
                else:
                    content += step['stepInstruction']
                content += ' '
            elif step['type']==3:
                pattern = '''<font[.\n]*?color=.*?>'''
                stepinfo = re.sub(pattern,'',step['stepInstruction'])
                pattern = '''</font>'''
                stepinfo = re.sub(pattern,'',stepinfo)
                pattern = '''<font color=.*?>'''
                stepinfo = re.sub(pattern,'',stepinfo)
                if PY2:
                    content += stepinfo.encode('utf-8')
                else:
                    content += stepinfo
            timeout += step['duration']
        content += ' 用时%d分钟\n'%(timeout/60)
    if PY2:
        print(content.decode('utf-8'))
    else:
        print(content)
