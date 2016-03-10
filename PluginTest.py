#coding=utf8
import json
import sys, traceback, os

succeed = True

def plugin_load_succeed():
    return succeed

def sys_print(level, msg):
    if level == 'SUCC': msg += ' plugin loaded'
    if level == 'WARN': global succeed; succeed = False
    print '[%s] %s'%(level, msg)

# load plugin list
try:
    pluginListDir = 'pluginlist.json'
    with open(pluginListDir) as f: pluginList = json.loads(f.read())
except:
    pluginList = []
    sys_print('WARN', 'There is something wrong with the format of your pluginlist.json')

# Test tuling.py
if 'tuling' in pluginList:
    try:
        pluginList.remove('tuling')
        import plugin.tuling as tuling
        try:
            tuling.get_response('Hi', 'LittleCoder')
            pluginList.append('tuling')
            sys_print('SUCC', 'Tuling')
        except:
            sys_print('WARN', 'Your key for tuling robot can\'t be used now, change one in plugin/config/tuling.json')
            sys_print('~~~~', 'You can get it from http://www.tuling123.com/')
    except:
        sys_print('WARN', 'There is something wrong with the format of your plugin/config/tuling.json')

# Test QRCode.py
if 'QRCode' in pluginList:
    try:
        import plugin.QRCode as QRCode
        sys_print('SUCC', 'Command line QRCode')
    except:
        sys_print('INFO', 'Command line QRCode loaded failed, if you want to use this, you need to run `pip install Image`')

# Test msgdealers.autoreply
if 'msgdealers.autoreply' in pluginList:
    try:
        pluginList.remove('msgdealers.autoreply')
        from plugin.msgdealers.autoreply import autoreply
        pluginList.append('msgdealers.autoreply')
        sys_print('SUCC', 'msgdealers.autoreply')
    except Exception, e:
        sys_print('WARN', str(e))

# Test msgdealers.vote
if 'msgdealers.vote' in pluginList:
    try:
        from plugin.msgdealers.vote import vote 
        sys_print('SUCC', 'msgdealers.vote')
        sys_print('INFO', 'But whether it can be properly used need to be tested online')
    except:
        sys_print('WARN', 'Vote plugin loaded failed, this is strange, you need to contact me')
        traceback.print_exc()

if __name__ == '__main__':
    try:
        print plugin_load_succeed()
        while True:
            msg = raw_input('>').decode(sys.stdin.encoding)
            if 'msgdealers.autoreply' in pluginList:
                r = autoreply(msg)
            if 'tuling' in pluginList:
                r = r or '\n'.join(tuling.get_response(msg, 'ItChat'))
            if not r: r = 'No plugin matched'

            print r
    except:
        print 'Exit'
        traceback.print_exc()
else:
    sys_print('INFO', 'Plugin loading finished')

