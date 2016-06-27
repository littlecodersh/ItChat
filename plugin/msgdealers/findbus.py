# -*- coding: utf-8 -*-
import sys,os
PY2 = sys.version[0] == '2'
from baidumaps import Client
import re
import json

SQLITE_DIR = os.path.join('plugin', 'config')
try:
    with open(os.path.join(SQLITE_DIR, 'findbus.json')) as f: key = json.loads(f.read())['key']
except:
    key = '' # if key is '', get_response will return None
    # raise Exception('There is something wrong with the format of you plugin/config/tuling.json')
# with open('../config/findbus.json') as f: key = json.loads(f.read())['key']

bdmaps = Client(ak=key)
# def findbus(from_place,to_place,city='深圳',mode = 'transit'):
def findbus(msg, storageClass = None, msgFrom = None):
    # result = bdmaps.geoconv('114.21892734521,29.575429778924')
    match = re.search(u'在?([^在\s]*?)从([^从\s]+?)[到去]([^到去\s]+)用?([^用\s]*?)', msg)
    if match:
        if PY2:
            from_place = match.group(2).encode("utf-8")
            to_place = match.group(3).encode("utf-8")
            city = match.group(1).encode("utf-8")
            mode = match.group(4)
        else:
            from_place = match.group(2)
            to_place = match.group(3)
            city = match.group(1)
            mode = match.group(4)
    else:
        return False
    if city=='':city='深圳' 
    if mode=='':mode='transit' 
    try:
        result = bdmaps.direct(from_place,to_place,mode,region=city)
    except:
        return '无结果'
    mymsg = ''
    content = ''
    for i in range(len(result['routes'])):
        scheme = result['routes'][i]
        content += '[方案%d]: 从%s'%(i+1,from_place)
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
        content += ' 到达%s 用时%d分钟\n'%(to_place,timeout/60)
    content = content.decode('utf-8') if PY2 else content
    return content if len(content)>0 else ''

if __name__ == '__main__':
    match = re.search(u'在?([^在\s]*?)从([^从\s]+?)[到去]([^到去\s]+)用?([^用\s]*?)', u'从机场到坪洲')
    print(match.group(0))
    print(match.group(1))
    print(match.group(2))
    print(match.group(3))
    print(match.group(4))
    print(findbus(u'深圳从机场到坪洲'))
