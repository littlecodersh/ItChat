import os, time, thread
import config

arg = {
    'talk': {
        'help': 'talk [name]          :talk to the user, only talk will talk to default user',
        },
    'send': {
        'help': 'send name message    :send message to the user',
    },
    'search': {
        'help': 'search name          :find the full name of the user',
    },
    'history': {
        'help': 'history name [count] :print the history of the user',
    },
    'clear': {
        'help': 'clear                :clear the screen',
    },
}
SEND_SYMBOL = '->'

def startCommandLine(client_s, client, msgList, front, cmdList):
    frontStatus = 0 # 0 for command, 1 for talks
    userTalkingTo = None
    def set_header(header = ''):
        nickName = client_s.find_nickname(client_s.userName)
        front.set_header('%s%s%s'%(nickName if nickName else '', '@' if header else '', header))
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
                        nickName = ' '.join(cmd[1:])
                        userName = client_s.find_user(nickName)
                        if not userName: front.print_line('User Not Found');continue
                    else:
                        if client_s.lastInputUserName:
                            userName = client_s.lastInputUserName
                        else:
                            userName = client_s.userName
                    nickName = client_s.find_nickname(userName)
                    set_header(nickName)
                    frontStatus = 1
                    userTalkingTo = userName
                    front.print_line('Talking to %s, press Esc to exit talking mode'%nickName)
                elif cmd[0] == 'send': #UserName BUG
                    if len(cmd) < 3 : front.print_line('%s params found 3 needed'%len(cmd));continue
                    for i in range(2, len(cmd)):
                        if cmd[i] == '--':
                            userName = client_s.find_user(cmd[1:i])
                            msg = ' '.join(cmd[i:])
                    if not userName: front.print_line('User Not Found');continue
                    if not msg: front.print_line('No message');continue
                    if msg and msg[1] == msg[-1] == '"': msg = msg[1:-1]
                    front.print_line('%s%s'%(SEND_SYMBOL, msg))
                    def send(front, userTalkingTo, cmd):
                        try:
                            client.send_msg(userTalkingTo, cmd)
                        except:
                            front.print_line('[FAIL: SEND AGAIN]%s'%cmd)
                    thread.start_new_thread(send, (front, userTalkingTo, msg))
                elif cmd[0] == 'search':
                    if len(cmd) == 1: front.print_line('%s params found 2 needed'%len(cmd));continue
                    nickName = ' '.join(cmd[1:])
                    l = client_s.search_nickname(nickName)
                    if not l: front.print_line('No names found');continue
                    if len(l) > 21: front.print_line('%s names found, please keep it more specific'%len(l));continue
                    s = '%s found:'%len(l)
                    for i in range(len(l) / 3 + 1):
                        s += '\n'
                        for j in range(3):
                            if i * 3 + j < len(l): s += (l[i * 3 + j] + '    ')
                    front.print_line(s)
                elif cmd[0] == 'history': #UserName BUG
                    if len(cmd) < 2 : front.print_line('%s params found 2 at least needed'%len(cmd));continue 
                    if len(cmd) < 3 or not cmd[-1].isdigit():
                        userName = client_s.find_user(' '.join(cmd[1:]))
                        count = 10
                    else:
                        userName = client_s.find_user(' '.join(cmd[1:-1]))
                        count = int(cmd[-1])
                    if not userName: front.print_line('User Not Found');continue

                    for m in client_s.find_msg_list(userName, count):
                        msg = m[1]
                        if m[-1] == 'to':
                            msg = SEND_SYMBOL + msg
                        else:
                            msg = '%s: %s'%(m[2], msg)
                        front.print_line(msg)
                elif cmd[0] == 'clear':
                    front.clear()
                else:
                    front.print_line('Error command, type in \'help\' for help')
            else:
                if chr(27) in cmd:
                    frontStatus = 0
                    set_header('')
                    front.print_line('Talk with %s finished'%client_s.find_nickname(userTalkingTo))
                else:
                    front.print_line('%s%s'%(SEND_SYMBOL, cmd))
                    def send(front, userTalkingTo, cmd):
                        try:
                            client.send_msg(userTalkingTo, cmd)
                        except:
                            front.print_line('[FAIL: SEND AGAIN]%s'%cmd)
                    thread.start_new_thread(send, (front, userTalkingTo, cmd))
            cmd = None
        time.sleep(.01)
