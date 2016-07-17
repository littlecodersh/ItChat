#coding=utf8
import itchat.out as out
import itchat.log as log
from PluginTest import *
import re

try:
    import plugin.msgdealers.findbus as findbus
    findbus.findbus('机场', '坪洲')
    IFFINDBUS = True
except:
    IFFINDBUS = False

try:
    import plugin.tuling as tuling
    tuling.get_response('Hi', 'LittleCoder')
    TULING = True
except:
    TULING = False

PRINT_ON_CMD = True

def send_msg(client, toUserName, msg):
    if len(msg) > 5:
        if msg[:5] == '@fil@':
            try:
                with open(msg[5:]): pass
                client.send_file(msg[5:], toUserName)
            except:
                log.log('Send file %s failed'%msg[5:], False)
        elif msg[:5] == '@img@':
            try:
                with open(msg[5:]): pass
                client.send_image(msg[5:], toUserName)
            except:
                log.log('Send image %s failed'%msg[5:], False)
        elif msg[:5] == '@msg@':
            client.send_msg(toUserName, msg[:5])
        else:
            client.send_msg(toUserName, msg)
    else:
        client.send_msg(toUserName, msg)

def get_reply(msg, s, client, isGroupChat = False, cmdPrint = PRINT_ON_CMD):
    reply = ''
    if msg['MsgType'] == 'Text':
        content = msg['Content']
        # Plugins should be added in order as ('name', function)
        pluginOrder = [('vote', vote), ('findbus', findbus.findbus), ('tuling', tuling.get_response)]
        if isGroupChat: pluginOrder = [('findbus', findbus.findbus), ('tuling', tuling.get_response)]
        getReply = False
        for plugin in pluginOrder:
            if plugin[0] in (pluginList['msgdealers'] + pluginList['systemmodules']):
                r = plugin[1](content, client.storageClass, msg['FromUserName'])
                if r:
                    reply = r
                    getReply = True
                    break
        if not getReply: reply = 'I received: %s'%content
    elif msg['MsgType'] == 'Map':
        return 'You are there!'
        if not isGroupChat and cmdPrint: 
            out.print_line('%s is at %s'%(s.find_nickname(msg['FromUserName']), msg['Content']))
    elif msg['MsgType'] == 'Picture':
        return 'Picture received!'
        if not isGroupChat and cmdPrint: 
            out.print_line('%s sent a picture [%s]'%(s.find_nickname(msg['FromUserName']), msg['Content']))
    elif msg['MsgType'] == 'Recording':
        return 'Nice Voice!'
        if not isGroupChat and cmdPrint: 
            out.print_line('%s sent a recording'%(s.find_nickname(msg['FromUserName'])))
    elif msg['MsgType'] == 'Card':
        return 'Greeting, %s!'%msg['Content']
        if not isGroupChat and cmdPrint: 
            out.print_line('%s sent a business card of [%s]'%(s.find_nickname(msg['FromUserName']), msg['Content']))
    elif msg['MsgType'] == 'Sharing':
        return '"%s" is good!'%msg['Content']
        if not isGroupChat and cmdPrint: 
            out.print_line('%s sent a web about [%s]'%(s.find_nickname(msg['FromUserName']), msg['Content']))
    elif msg['MsgType'] == 'Attachment':
        return '"%s" received!'%msg['Content']
        if not isGroupChat and cmdPrint: 
            out.print_line('%s sent an attachment: [%s]'%(s.find_nickname(msg['FromUserName']), msg['Location']))
    elif msg['MsgType'] == 'Video':
        return 'I received a video'
        if not isGroupChat and cmdPrint: 
            out.print_line('%s sent a video [%s]'%(s.find_nickname(msg['FromUserName']), msg['Content']))
    elif msg['MsgType'] == 'Note':
        if not isGroupChat and cmdPrint: out.print_line('Notification: %s'%(msg['Content']))
    else:
        pass#out.print_line(str(msg))
    return reply

def deal_with_msg(msg, s, client):
    if msg.has_key('FromUserName') and msg['FromUserName'][:2] == '@@':
        if msg.has_key('ActualNickName'):
            out.print_line('[group msg] %s: %s'%(msg['ActualNickName'], msg['Content']))
            try:
                r = get_reply(msg, s, client, True)
                # r = grouptalking(msg, s, client, get_reply)
                send_msg(client, msg['FromUserName'], u'@%s\u2005 %s'%(msg['ActualNickName'], r))
            except:
                log.log('Send group chat failed', False)
    else:
        out.print_line('[msg] %s: %s'%(s.find_nickname(msg['FromUserName']), msg['Content']))
        r = get_reply(msg, s, client)
        send_msg(client, msg['FromUserName'], r)
