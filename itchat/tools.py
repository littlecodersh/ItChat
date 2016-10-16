import re, os, sys, subprocess, copy

try:
    from HTMLParser import HTMLParser
except ImportError:
    from html.parser import HTMLParser

from . import config

emojiRegex = re.compile(r'<span class="emoji emoji(.{1,10})"></span>')
htmlParser = HTMLParser()
try:
    b = u'\u2588'
    sys.stdout.write(b + '\r')
    sys.stdout.flush()
except UnicodeEncodeError:
    BLOCK = 'MM'
else:
    BLOCK = b
friendInfoTemplate = {}
for k in ('UserName', 'City', 'DisplayName', 'PYQuanPin', 'RemarkPYInitial', 'Province',
    'KeyWord', 'RemarkName', 'PYInitial', 'EncryChatRoomId', 'Alias', 'Signature', 
    'NickName', 'RemarkPYQuanPin', 'HeadImgUrl'): friendInfoTemplate[k] = ''
for k in ('UniFriend', 'Sex', 'AppAccountFlag', 'VerifyFlag', 'ChatRoomId', 'HideInputBarFlag',
    'AttrStatus', 'SnsFlag', 'MemberCount', 'OwnerUin', 'ContactFlag', 'Uin',
    'StarFriend', 'Statues'): friendInfoTemplate[k] = 0
friendInfoTemplate['MemberList'] = []

def clear_screen():
    os.system('cls' if config.OS == 'Windows' else 'clear')
def emoji_formatter(d, k):
    # _emoji_deebugger is for bugs about emoji match caused by wechat backstage
    # like :face with tears of joy: will be replaced with :cat face with tears of joy:
    def _emoji_debugger(d, k):
        s = d[k].replace('<span class="emoji emoji1f450"></span',
            '<span class="emoji emoji1f450"></span>') # fix missing bug
        def __fix_miss_match(m):
            return '<span class="emoji emoji%s"></span>' % ({
                '1f63c': '1f601', '1f639': '1f602', '1f63a': '1f603',
                '1f4ab': '1f616', '1f64d': '1f614', '1f63b': '1f60d',
                '1f63d': '1f618', '1f64e': '1f621', '1f63f': '1f622',
                }.get(m.group(1), m.group(1)))
        return emojiRegex.sub(__fix_miss_match, s)
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
    d[k] = _emoji_debugger(d, k)
    d[k] = emojiRegex.sub(_emoji_formatter, d[k])
def msg_formatter(d, k):
    emoji_formatter(d, k)
    d[k] = d[k].replace('<br/>', '\n')
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
            white = BLOCK, black = '  ', enableCmdQR = True):
        img     = Image.open(fileDir)
        times   = img.size[0] / (size + padding * 2)
        rgb     = img.convert('RGB')
        try:
            blockCount = int(enableCmdQR)
            assert(0 < abs(blockCount))
        except:
            blockCount = 1
        finally:
            white *= abs(blockCount)
            if blockCount < 0: white, black = black, white
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
            white = BLOCK, black = '  ', enableCmdQR = True):
        print('pillow should be installed to use command line QRCode: pip install pillow')
        print_qr(fileDir)
def struct_friend_info(knownInfo):
    member = copy.deepcopy(friendInfoTemplate)
    for k, v in copy.deepcopy(knownInfo).items(): member[k] = v
    return member

def search_dict_list(l, key, value):
    ''' Search a list of dict
        * return dict with specific value & key '''
    for i in l:
        if i.get(key) == value: return i
