#coding=utf8
from client import WeChatClient


if __name__ == '__main__':
    client = WeChatClient()
    client.login()

    # ONLY FOR DEBUG
    # replying the same msg to the sender
    # find_nickname should not be in client actually
    s = client.storage()
    print 'Start auto-replying'
    while True: 
        if s: 
            msg = s.pop()
            if client.find_nickname(msg['FromUserName']):
                print '%s: %s'%(client.find_nickname(msg['FromUserName']), msg['Content'])
                client.send_msg(msg['FromUserName'], 'I received: ' + msg['Content'])
