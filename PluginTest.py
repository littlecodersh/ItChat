#coding=utf8
import json
import sys, traceback, os

succeed = True

def plugin_load_succeed():
    return succeed

def sys_print(level, msg):
    if level == 'SUCC': msg += ' plugin loaded'
    if level == 'WARN': global succeed; succeed = False
    print '[%s] %s'%(level[:4], msg)

# load plugin list
try:
    pluginListDir = 'pluginlist.json'
    with open(pluginListDir) as f: pluginList = json.loads(f.read())
except:
    pluginList = {}
    sys_print('WARN', 'There is something wrong with the format of your pluginlist.json')

# Test grouptalking.py
if 'grouptalking' in pluginList['systemmodules']:
    try:
        from plugin.msgdealers.grouptalking import grouptalking
        sys_print('INFO', 'Group talking plugin is open now, please be careful about it.')
    except:
        sys_print('WARN', 'There is something wrong with the grouptalking plugin')
        # traceback.print_exc()

# Test tuling.py
if 'tuling' in pluginList['systemmodules']:
    try:
        pluginList['systemmodules'].remove('tuling')
        import plugin.tuling as tuling
        try:
            tuling.get_response('Hi', 'LittleCoder')
            pluginList['systemmodules'].append('tuling')
            sys_print('SUCC', 'Tuling')
        except:
            sys_print('INFO', 'Your key for tuling robot can\'t be used now, change one in plugin/config/tuling.json')
            sys_print('~~~~', 'You can get it from http://www.tuling123.com/')
    except:
        sys_print('WARN', 'There is something wrong with the format of your plugin/config/tuling.json')

# Test QRCode.py
if 'QRCode' in pluginList['systemmodules']:
    try:
        import plugin.QRCode as QRCode
        sys_print('SUCC', 'Command line QRCode')
    except:
        sys_print('INFO', 'Command line QRCode loaded failed, if you want to use this, you need to run `pip install Image`')

# Test msgdealers.autoreply
if 'autoreply' in pluginList['msgdealers']:
    try:
        pluginList['msgdealers'].remove('autoreply')
        from plugin.msgdealers.autoreply import autoreply
        pluginList['msgdealers'].append('autoreply')
        sys_print('SUCC', 'msgdealers.autoreply')
    except Exception, e:
        sys_print('WARN', e.message)

# Test msgdealers.vote
if 'vote' in pluginList['msgdealers']:
    try:
        pluginList['msgdealers'].remove('vote')
        from plugin.msgdealers.vote import vote 
        pluginList['msgdealers'].append('vote')
        sys_print('SUCC', 'msgdealers.vote')
        sys_print('INFO', 'But whether it can be properly used need to be tested online')
    except:
        sys_print('WARN', 'Vote plugin loaded failed, this is strange, you need to contact me')
        # traceback.print_exc()

def send_msg(msg):
    if len(msg) > 5:
        if msg[:5] == '@fil@':
            try:
                with open(msg[5:]): pass
                print 'File: %s'%msg[5:]
            except:
                pass
        if msg[:5] == '@img@':
            try:
                with open(msg[5:]): pass
                print 'Picture: %s'%msg[5:]
            except:
                pass
        elif msg[:5] == '@msg@':
            print msg[5:]
        else:
            print msg
    else:
        print msg[5:]

if __name__ == '__main__':
    try:
        print 'Loading %s'%('successfully' if plugin_load_succeed() else 'failed')
        pluginOrder = [('autoreply', autoreply), ('tuling', tuling.get_response)]
        while True:
            msg = raw_input('>').decode(sys.stdin.encoding)
            if not msg: continue
            res = ''
            for plugin in pluginOrder:
                if plugin[0] in (pluginList['msgdealers'] + pluginList['systemmodules']):
                    r = plugin[1](msg, None, None)
                    if r: res = r;break
            if not res: r = 'No plugin matched'

            send_msg(r)
    except:
        print 'Exit'
        # traceback.print_exc()
else:
    sys_print('INFO', 'Plugin loading finished')

