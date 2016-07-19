import re, os

from . import config

def clear_screen():
    os.system('cls' if config.OS == 'Windows' else 'clear')
    
def emojiRecover(string):
    def match(matched):
        return eval("u'\\U000{}'".format(matched.group("emoji")))

    reobj = re.compile('<span class="emoji emoji(?P<emoji>.{,10})"></span>')
    result, count = reobj.subn(match, string)
    return result
    
def emoji_dealer(d):
    d['NickName'] = emojiRecover(d['NickName'])
    return d
def check_file(fileDir):
    try:
        with open(fileDir): pass
        return True
    except:
        return False
