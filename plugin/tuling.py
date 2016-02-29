#coding=utf8
import sys
import requests, json
from ChatLikeCMD import ChatLikeCMD

try:
    with open('tuling.json') as f: key = json.loads(f.read())['key']
except:
    raise Exception('You need to have a correct tuling.json file')

def get_response(msg, userid):
    url = 'http://www.tuling123.com/openapi/api'
    payloads = {
        'key': key,
        'info': msg,
        'userid': userid,
    }
    r = json.loads(requests.post(url, data = payloads).text)
    if not r['code'] in (100000, 200000, 302000, 308000, 313000, 314000):
        if r['code'] == 400004: return None
        raise Exception('code: %s'%r['code'])
    elif r['code'] == 100000: # 文本类
        return [r['text'].replace('<br>','\n')]
    elif r['code'] == 200000: # 链接类
        return [r['text'].replace('<br>','\n'), r['url']]
    elif r['code'] == 302000: # 新闻类
        l = [r['text'].replace('<br>','\n')]
        for n in r['list']: l.append('%s - %s'%(n['article'], n['detailurl']))
        return l
    elif r['code'] == 308000: # 菜谱类
        l = [r['text'].replace('<br>','\n')]
        for n in r['list']: l.append('%s - %s'%(n['name'], n['detailurl']))
        return l
    elif r['code'] == 313000: # 儿歌类
        return [r['text'].replace('<br>','\n')]
    elif r['code'] == 314000: # 诗词类
        return [r['text'].replace('<br>','\n')]

if __name__ == '__main__':
    while True:
        a = raw_input('>').decode(sys.stdin.encoding).encode('utf8')
        for m in get_response(a, 'ItChat'): print m
