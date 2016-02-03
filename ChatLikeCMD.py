#coding=utf8
import thread, time, sys, os, platform

try:
    import termios, tty
    termios.tcgetattr, termios.tcsetattr
except (ImportError, AttributeError):
    try:
        import msvcrt
    except ImportError:
        raise Exception('Mac is currently not supported')
    else:
        getch = msvcrt.getwch
else:
    def fn():
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        tty.setraw(fd)
        ch = sys.stdin.read(1)
        if ord(ch)>=256: ch += sys.stdin.read(1)
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        return ch
    getch = fn

CMD_HISTORY = 30

class ChatLikeCMD():
    def __init__(self, header = 'LittleCoder', symbol = '>', inPip = None, inputMaintain = False):
        self.strBuff = []
        self.cmdBuff = []
        self.historyCmd = -1
        self.inPip = [] if inPip == None else inPip
        self.outPip = []
        self.isLaunch = False
        self.isPause = False
        self.header = header
        self.symbol = symbol
        self.inputMaintain = inputMaintain
    def reprint_input(self):
        sys.stdout.write(self.header + self.symbol)
        if self.strBuff:
            for i in self.strBuff: sys.stdout.write(i)
        sys.stdout.flush()
    def getch(self):
        c = getch()
        return c if c != '\r' else '\n'
    def get_history_command(self, direction):
        if direction == 'UP':
            if self.historyCmd < CMD_HISTORY - 1 and self.historyCmd < len(self.cmdBuff) - 1: self.historyCmd += 1
        else:
            if self.historyCmd > 0: self.historyCmd -= 1
        if -1 < self.historyCmd < len(self.cmdBuff): return self.cmdBuff[self.historyCmd]
    def output_command(self, s):
        self.outPip.append(s)
        if len(self.cmdBuff) >= CMD_HISTORY: self.cmdBuff = self.cmdBuff[::-1].pop()[::-1]
        self.cmdBuff.append(s)
    def print_thread(self):
        while self.isLaunch:
            if self.inPip:
                sys.stdout.write('\r' + ' ' * 50 + '\r')
                sys.stdout.flush()
                print self.inPip.pop()
                # linux special
                sys.stdout.write('\r')
                sys.stdout.flush()
                self.reprint_input()
            time.sleep(0.01)
    def command_thread(self):
        c = None
        while self.isLaunch:
            c = self.getch()
            if ord(c) == 27: # Esc
                sys.stdout.write('\r' + ' ' * 50 + '\r')
                sys.stdout.flush()
                self.reprint_input()
                self.outPip.append(c)
            elif ord(c) == 3: # Ctrl+C
                self.stop()
                self.isPause = True
                if raw_input('Exit?(y) ') == 'y':
                    sys.stdout.write('Command Line Exit')
                else:
                    self.start()
                self.isPause = False
            elif ord(c) == 224: # direction
                direction = ord(self.getch())
                if direction == 75:
                    if self.strBuff: 
                        sys.stdout.write('\b \b' if ord(self.strBuff[-1]) < 256 else '\b\b \b')
                        self.strBuff.pop()
                elif direction == 72:
                    hc = self.get_history_command('UP')
                    if hc:
                        self.strBuff = [i for i in hc]
                        sys.stdout.write('\r' + ' ' * 50 + '\r')
                        self.reprint_input()
                elif direction == 77:
                    pass
                elif direction == 80:
                    hc = self.get_history_command('DOWN')
                    if hc:
                        self.strBuff = [i for i in hc]
                        sys.stdout.write('\r' + ' ' * 50 + '\r')
                        self.reprint_input()
                else:
                    raise Exception
            elif c == '\b': # Backspace
                if self.strBuff: 
                    sys.stdout.write('\b \b' if ord(self.strBuff[-1]) < 256 else '\b\b \b')
                    self.strBuff.pop()
            elif c == '\n':
                if self.strBuff:
                    if self.inputMaintain: 
                        sys.stdout.write(c)
                    else:
                        sys.stdout.write('\r' + ' ' * 50 + '\r')
                    sys.stdout.flush()
                    self.reprint_input()
                    self.output_command(''.join(self.strBuff))
                    self.strBuff = []
                self.historyCmd = -1
            else:
                sys.stdout.write(c)
                sys.stdout.flush()
                self.strBuff.append(c)
            time.sleep(0.01)
    def start(self):
        self.isLaunch = True
        thread.start_new_thread(self.print_thread, ())
        self.reprint_input()
        thread.start_new_thread(self.command_thread, ())
    def stop(self):
        sys.stdout.write('\r' + ' ' * 50 + '\r')
        sys.stdout.flush()
        self.isLaunch = False
    def print_line(self, msg = None):
        self.inPip.append(msg)
    def clear(self):
        os.system('cls' if platform.system() == 'Windows' else 'clear')
        self.reprint_input()
    def get_command_pip(self):
        return self.outPip
    def set_header(self, header):
        self.header = header

if __name__ == '__main__':
    c = ChatLikeCMD()
    s = c.get_command_pip()
    c.start()
    def loopinput(c):
        while True:
            c.print_line('LOOP INPUT......')
            time.sleep(3)
    thread.start_new_thread(loopinput, (c,))
    while c.isLaunch or c.isPause:
        if s:
            c.print_line(s.pop())
        time.sleep(0.01)
