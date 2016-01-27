#coding=utf8
import time
import storage, out
from client import WeChatClient

def deal_with_msg(msg, s):
    if msg['MsgType'] == 'Text':
        client.send_msg(msg['FromUserName'], 'I received: ' + msg['Content'])
        out.print_line('%s: %s'%(s.find_nickname(msg['FromUserName']), msg['Content']))
    elif msg['MsgType'] == 'Map':
        client.send_msg(msg['FromUserName'], 'You are there!')
        out.print_line('%s is at %s'%(s.find_nickname(msg['FromUserName']), msg['Content']))
    elif msg['MsgType'] == 'Picture':
        client.send_msg(msg['FromUserName'], 'Picture received')
        out.print_line('%s sent a picture [%s]'%(s.find_nickname(msg['FromUserName']), msg['Content']))
    elif msg['MsgType'] == 'Recording':
        client.send_msg(msg['FromUserName'], 'Nice Voice!')
        out.print_line('%s sent a recording'%(s.find_nickname(msg['FromUserName'])))
    elif msg['MsgType'] == 'Card':
        client.send_msg(msg['FromUserName'], 'Greeting, %s!'%msg['Content'])
        out.print_line('%s sent a business card of [%s]'%(s.find_nickname(msg['FromUserName']), msg['Content']))
    elif msg['MsgType'] == 'Sharing':
        client.send_msg(msg['FromUserName'], '"%s" is good!'%msg['Content'])
        out.print_line('%s sent a web about [%s]'%(s.find_nickname(msg['FromUserName']), msg['Content']))
    elif msg['MsgType'] == 'Attachment':
        client.send_msg(msg['FromUserName'], '"%s" received'%msg['Content'])
        out.print_line('%s sent an attachment: [%s]'%(s.find_nickname(msg['FromUserName']), msg['Location']))
    elif msg['MsgType'] == 'Video':
        client.send_msg(msg['FromUserName'], 'I received a video')
        out.print_line('%s sent a video [%s]'%(s.find_nickname(msg['FromUserName']), msg['Content']))
    elif msg['MsgType'] == 'Note':
        out.print_line('Notification: %s'%(msg['Content']))
    else:
        pass#out.print_line(str(msg)

if __name__ == '__main__':
    s = storage.Storage()
    client = WeChatClient(s)
    client.login()
    msgList = client.storage()

    # ONLY FOR DEMO
    print 'Start auto-replying'
    while True: 
        if msgList: 
            msg = msgList.pop()
            if s.find_nickname(msg['FromUserName']): deal_with_msg(msg, s)
            time.sleep(.5)
