#coding=utf8
import thread, time, sys, os, platform

try:
    import termios, tty
    termios.tcgetattr, termios.tcsetattr
    import threading
    OS = 'Linux'
except (ImportError, AttributeError):
    try:
        import msvcrt
        OS = 'Windows'
    except ImportError:
        raise Exception('Mac is currently not supported')
        OS = 'Mac'
    else:
        getch = msvcrt.getwch
else:
    def fn():
        try:
            fd = sys.stdin.fileno()
            old_settings = termios.tcgetattr(fd)
            tty.setraw(fd)
            ch = sys.stdin.read(1)
        except:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
            raise Exception
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        return ch
    getch = fn

CMD_HISTORY = 30

class ChatLikeCMD():
    def __init__(self, header = 'LittleCoder', symbol = '>', inPip = None, inputMaintain = False):
        self.strBuff = []
        self.cmdBuff = []
        self.historyCmd = -1
        self.cursor = 0
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
            if self.historyCmd == 0: return ''
            if self.historyCmd > 0: self.historyCmd -= 1
        if -1 < self.historyCmd < len(self.cmdBuff): return self.cmdBuff[self.historyCmd]
    def output_command(self, s):
        self.outPip.append(s if isinstance(s, unicode) else s.decode(sys.stdin.encoding))
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
    def fast_input_test(self):
        timer = threading.Timer(0.001, thread.interrupt_main)
        c = None
        try:
            timer.start()
            c = getch()
        except:
            pass
        timer.cancel()
        return c
    def process_direction_char(self, c):
        if OS == 'Windows':
            if ord(c) == 72:
                c = 'A'
            elif ord(c) == 80:
                c = 'B'
            elif ord(c) == 77:
                c = 'C'
            elif ord(c) == 75:
                c = 'D'
        if ord(c) == 68: # LEFT
            self.process_char('\b')
            return 
            # cursor bugs
            if self.cursor > 0:
                if OS == 'Windows':
                    sys.stdout.write(chr(224) + chr(75))
                else:
                    sys.stdout.write(chr(27) + '[C')
                self.cursor -= 1
        elif ord(c) == 67: # RIGHT
            return 
            # cursor bugs
            if self.cursor < len(self.strBuff):
                if OS == 'Windows':
                    sys.stdout.write(chr(224) + chr(77))
                else:
                    sys.stdout.write(chr(27) + '[D')
                self.cursor += 1
        elif ord(c) == 65: # UP
            hc = self.get_history_command('UP')
            if not hc is None:
                self.strBuff = [i for i in hc]
                self.cursor = len(hc)
                sys.stdout.write('\r' + ' ' * 50 + '\r')
                self.reprint_input()
        elif ord(c) == 66: # DOWN
            hc = self.get_history_command('DOWN')
            if not hc is None:
                self.strBuff = [i for i in hc]
                self.cursor = len(hc)
                sys.stdout.write('\r' + ' ' * 50 + '\r')
                self.reprint_input()
        else:
            raise Exception(c)
    def process_char(self, c):
        if ord(c) == 27: # Esc
            if OS == 'Linux':
                fitc1 = self.fast_input_test()
                if ord(fitc1) == 91:
                    fitc2 = self.fast_input_test()
                    if 65 <= ord(fitc2) <= 68:
                        self.process_direction_char(fitc2)
                        return
            sys.stdout.write('\r' + ' ' * 50 + '\r')
            sys.stdout.flush()
            self.reprint_input()
            self.outPip.append(c)
            time.sleep(0.02)
            if fitc1 in dir():
                self.process_char(fitc1)
                self.cursor += 1
            if fitc2 in dir():
                self.process_char(fitc2)
                self.cursor += 1
        elif ord(c) == 3: # Ctrl+C
            self.stop()
            self.isPause = True
            if raw_input('Exit?(y) ') == 'y':
                sys.stdout.write('Command Line Exit')
            else:
                self.start()
            self.isPause = False
        elif ord(c) in (8, 127): # Backspace
            if self.strBuff: 
                if ord(self.strBuff[-1]) < 128:
                    sys.stdout.write('\b \b')
                else:
                    sys.stdout.write('\b\b \b')
                    if OS == 'Linux':
                        self.strBuff.pop()
                        self.strBuff.pop()
                self.strBuff.pop()
                self.cursor -= 1
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
        elif ord(c) == 224: # Windows direction
            if OS == 'Windows':
                direction = self.getch()
                self.process_direction_char(direction)
        else:
            sys.stdout.write(c)
            sys.stdout.flush()
            self.strBuff.append(c)
            self.cursor += 1
    def command_thread(self):
        c = None
        while self.isLaunch:
            c = self.getch()
            self.process_char(c)
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
