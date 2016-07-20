import re, os
try:
    from HTMLParser import HTMLParser
except ImportError:
    from html.parser import HTMLParser

from . import config

emojiRegex = re.compile(r'<span class="emoji emoji(.*?)"></span>')
htmlParser = HTMLParser()

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
