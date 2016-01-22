import sys
import tools

def print_msg(m):
    print m
def print_line(msg):
    sys.stdout.write(' '*40 + '\r')
    sys.stdout.flush()
    sys.stdout.write(msg)
    sys.stdout.flush()
    # if m['FromUserName'] == self.userName: continue
    # print '%s: %s'%(self.find_nickname(m['FromUserName']), m['Content'])
    # # only for debug, reply the same msg
    # self.send_msg(self.find_nickname(m['FromUserName']), 'I received: %s'%m['Content'])
