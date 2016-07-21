import re, os, sys

try:
    from HTMLParser import HTMLParser
except ImportError:
    from html.parser import HTMLParser

from . import config

emojiRegex = re.compile(r'<span class="emoji emoji(.*?)"></span>')
htmlParser = HTMLParser()
try:
    b = u'\u2588'
    sys.stdout.write(b + '\r')
    sys.stdout.flush()
except UnicodeEncodeError:
    BLOCK = 'MM'
else:
    BLOCK = b

def clear_screen():
    os.system('cls' if config.OS == 'Windows' else 'clear')
def emoji_formatter(d, k):
    # there's still a serious bug about emoji match
    # like :face with tears of joy: will be replaced with :cat face with tears of joy:
    def _emoji_formatter(m):
        s = m.group(1)
        if len(s) == 6:
            return ('\\U%s\\U%s'%(s[:2].rjust(8, '0'), s[2:].rjust(8, '0'))
                ).encode('utf8').decode('unicode-escape', 'replace')
        elif len(s) == 10:
            return ('\\U%s\\U%s'%(s[:5].rjust(8, '0'), s[5:].rjust(8, '0'))
                ).encode('utf8').decode('unicode-escape', 'replace')
        else:
            return ('\\U%s'%m.group(1).rjust(8, '0')
                ).encode('utf8').decode('unicode-escape', 'replace')
    d[k] = emojiRegex.sub(_emoji_formatter, d[k])
def msg_formatter(d, k):
    emoji_formatter(d, k)
    d[k]  = htmlParser.unescape(d[k])
def check_file(fileDir):
    try:
        with open(fileDir): pass
        return True
    except:
        return False
def print_qr(fileDir):
    if config.OS == 'Darwin':
        subprocess.call(['open', fileDir])
    elif config.OS == 'Linux':
        subprocess.call(['xdg-open', fileDir])
    else:
        os.startfile(fileDir)
try:
    from PIL import Image 
    def print_cmd_qr(fileDir, size = 37, padding = 3,
            white = BLOCK, black = '  '):
        img     = Image.open(fileDir)
        times   = img.size[0] / (size + padding * 2)
        rgb     = img.convert('RGB')
        sys.stdout.write(' '*50 + '\r')
        sys.stdout.flush()
        qr = white * (size + 2) + '\n'
        startPoint = padding + 0.5
        for y in range(size):
            qr += white
            for x in range(size):
                r,g,b = rgb.getpixel(((x + startPoint) * times, (y + startPoint) * times))
                qr += white if r > 127 else black
            qr += white + '\n'
        qr += white * (size + 2) + '\n'
        sys.stdout.write(qr)
except ImportError:
    def print_cmd_qr(fileDir, size = 37, padding = 3,
            white = BLOCK, black = '  '):
        print_qr(fileDir)
