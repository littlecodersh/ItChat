#coding=utf8
import thread, time, sys

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

class ChatLikeCMD():
    def __init__(self, header = 'LittleCoder', symbol = '>', inPip = None, inputMaintain = False):
        self.strBuff = []
        if not inPip: self.inPip = inPip
        self.outPip = []
        self.isLaunch = False
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
    def command_thread(self):
        c = None
        while self.isLaunch:
            c = self.getch()
            if c == chr(27):
                sys.stdout.write('\r' + ' ' * 50 + '\r')
                sys.stdout.flush()
                self.reprint_input()
                self.outPip.append(c)
            elif c == '\b': # Backspace
                # Chinese \b problems when using input method 
                if self.strBuff: 
                    sys.stdout.write('\b \b')
                    self.strBuff.pop()
            elif c == chr(3): # Ctrl+C
                self.stop()
            elif c == '\n':
                if self.inputMaintain: 
                    sys.stdout.write(c)
                else:
                    sys.stdout.write('\r' + ' ' * 50 + '\r')
                sys.stdout.flush()
                self.reprint_input()
                self.outPip.append(''.join(self.strBuff))
                self.strBuff = []
            else:
                sys.stdout.write(c)
                sys.stdout.flush()
                self.strBuff.append(c)
    def start(self):
        self.isLaunch = True
        thread.start_new_thread(self.print_thread, ())
        self.reprint_input()
        thread.start_new_thread(self.command_thread, ())
    def stop(self):
        sys.stdout.write('\r' + ' ' * 50 + '\r')
        sys.stdout.flush()
        print 'Command Line Exit'
        self.isLaunch = False
    def print_line(self, msg = None):
        self.inPip.append(msg)
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
    while c.isLaunch:
        if s:
            c.print_line(s.pop())
