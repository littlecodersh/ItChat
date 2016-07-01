import re

import os
import config

def clear_screen():
    os.system('cls' if config.OS == 'Windows' else 'clear')
def emoji_dealer(d):
    regex = re.compile('^(.*?)(?:<span class="emoji (.*?)"></span>(.*?))+$')
    match = re.findall(regex, d['NickName'])
    if len(match) > 0: d['NickName'] = ''.join(match[0])
    return d
def check_file(fileDir):
    try:
        with open(fileDir): pass
        return True
    except:
        return False
