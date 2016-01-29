import os, time
import config

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
    'clear': {
        'help': 'clear             :clear the screen',
    },
}

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
                elif cmd[0] == 'clear':
                    os.system('cls' if config.OS == 'Windows' else 'clear')
                else:
                    front.print_line('Error command, type in \'help\' for help')
            else:
                if chr(27) in cmd:
                    frontStatus = 0
                    set_header('')
                    front.print_line('Talk with %s finished'%client_s.find_nickname(userTalkingTo))
                else:
                    client.send_msg(userTalkingTo, cmd)
                    front.print_line('->%s'%cmd)
            cmd = None
        time.sleep(.01)
