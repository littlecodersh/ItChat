#coding=utf8
import time
import storage, out
from client import WeChatClient
from ChatLikeCMD import ChatLikeCMD

def demo(s, msgList): # ONLY FOR DEMO
    print 'Start auto-replying'
    while True: 
        if msgList: 
            msg = msgList.pop()
            if s.find_nickname(msg['FromUserName']): deal_with_msg(msg, s)
            time.sleep(.5)
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

arg = {
    'talk': {
        'help': 'talk [name]       :talk to the user, only talk will talks to the default user',
        },
    'send': {
        'help': 'send name message :send message to the user',
    },
    'search': {
        'help': 'search name       :find the full name of the user',
    },
}
if __name__ == '__main__':
    client_s = storage.Storage()
    client = WeChatClient(client_s)
    client.login()
    msgList = client.storage()
    # demo(client_s, msgList)

    front = ChatLikeCMD(header = client_s.find_nickname(client_s.userName), symbol = '>', inPip = msgList)
    cmdList = front.get_command_pip()
    front.start()
    frontStatus = 0 # 0 for command, 1 for talks
    userTalkingTo = None
    def set_header(header = ''):
        front.set_header('%s%s%s'%(client_s.find_nickname(client_s.userName),'@' if header else '', header))
    while front.isLaunch:
        if cmdList:
            cmd = cmdList.pop()
            if frontStatus == 0:
                cmd = cmd.split(' ')
                if cmd[0] == 'help':
                    for i,j in arg.items():
                        front.print_line(j['help'])
                elif cmd[0] == 'talk':
                    if len(cmd) > 1:
                        nickName = ''
                        for s in cmd[1:]: nickName += s
                        userName = client_s.find_user(nickName)
                        if not userName: front.print_line('User Not Found');continue
                    else:
                        if client_s.msgStorage:
                            userName = client_s.lastInputUserName
                        else:
                            userName = client_s.userName
                    nickName = client_s.find_nickname(userName)
                    set_header(nickName)
                    frontStatus = 1
                    userTalkingTo = userName
                    front.print_line('Talking to %s, press Esc to exit talking mode'%nickName)
                elif cmd[0] == 'send':
                    if len(cmd) < 3 : front.print_line('%s params found 3 needed'%len(cmd));continue
                    userName = client_s.find_user(cmd[1])
                    if not userName: front.print_line('User Not Found');continue

                    msg = ''
                    for s in cmd[1:]: msg += s
                    if msg and msg[1] == msg[-1] == '"': msg = msg[1:-1]

                    client.send_msg(userName, msg)
                elif cmd[0] == 'search':
                    if len(cmd) == 1: front.print_line('%s params found 2 needed'%len(cmd));continue
                    nickName = ''
                    for s in cmd[1:]: nickName += s
                    l = client_s.search_nickname(nickName)
                    if not l: front.print_line('No names found');continue
                    if len(l) > 10: front.print_line('%s names found, please keep it more specific'%len(l));continue
                    s = '%s found:'%len(l)
                    for i in range(len(l) / 3 + 1):
                        s += '\n'
                        for j in range(3):
                            if i * 3 + j < len(l): s += (l[i * 3 + j] + '    ')
                    front.print_line(s)
                else:
                    front.print_line('Error command, type in 'help' help')
            else:
                if chr(27) in cmd:
                    frontStatus = 0
                    set_header('')
                    front.print_line('Talk with %s finished'%client_s.find_nickname(userTalkingTo))
                else:
                    client.send_msg(userTalkingTo, cmd)
                    front.print_line('->%s'%cmd)
            cmd = None
