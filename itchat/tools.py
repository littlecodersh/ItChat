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
    d[k] = emojiRegex.sub(lambda x: ('\\U%s'%x.group(1).rjust(8, '0')
        ).encode('utf8').decode('unicode-escape'), d[k])
def msg_formatter(d, k):
    emoji_formatter(d, k)
    d[k]  = htmlParser.unescape(d[k])
def check_file(fileDir):
    try:
        with open(fileDir): pass
        return True
    except:
        return False
