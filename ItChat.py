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
                if msg['MsgType'] == 'Text':
                    client.send_msg(msg['FromUserName'], 'I received: ' + msg['Content'])
                    print '%s: %s'%(client.find_nickname(msg['FromUserName']), msg['Content'])
                elif msg['MsgType'] == 'Picture':
                    client.send_msg(msg['FromUserName'], 'I received a picture')
                    print '%s sent a picture [%s]'%(client.find_nickname(msg['FromUserName']), msg['Content'])
                elif msg['MsgType'] == 'Card':
                    client.send_msg(msg['FromUserName'], 'Greeting, %s!'%msg['Content'])
                    print '%s sent a business card of [%s]'%(client.find_nickname(msg['FromUserName']), msg['Content'])
                elif msg['MsgType'] == 'Sharing':
                    client.send_msg(msg['FromUserName'], '"%s" is good!'%msg['Content'])
                    print '%s sent a web about [%s]'%(client.find_nickname(msg['FromUserName']), msg['Content'])
                elif msg['MsgType'] == 'Video':
                    client.send_msg(msg['FromUserName'], 'I received a video')
                    print '%s sent a video [%s]'%(client.find_nickname(msg['FromUserName']), msg['Content'])
                elif msg['MsgType'] == 'Note':
                    print 'Notification: %s'%(msg['Content'])
                else:
                    print str(msg)
