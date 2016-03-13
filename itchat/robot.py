#coding=utf8
import itchat.out as out
import itchat.log as log
import PluginTest
from plugin.msgdealers.vote import vote
from plugin.msgdealers.autoreply import autoreply

try:
    import plugin.tuling as tuling
    tuling.get_response('Hi', 'LittleCoder')
    TULING = True
except:
    TULING = False

def send_msg(client, toUserName, msg):
    if len(msg) > 5:
        if msg[:5] == '@fil@':
            try:
                with open(msg[5:]): pass
                client.send_file(msg[5:], toUserName)
            except:
                log.log('Send %s failed'%msg[5:], False)
        elif msg[:5] == '@msg@':
            client.send_msg(toUserName, msg[:5])
        else:
            client.send_msg(toUserName, msg)
    else:
        client.send_msg(toUserName, msg)

def deal_with_msg(msg, s, client):
    if msg['MsgType'] == 'Text':
        content = msg['Content']
        # Plugins should be added in order as ('name', function)
        pluginOrder = [('vote', vote), ('autoreply', autoreply)]
        getReply = False
        for plugin in pluginOrder:
            if plugin[0] in PluginTest.pluginList['msgdealers']:
                r = plugin[1](content, client.storageClass, msg['FromUserName'])
                if r:
                    send_msg(client, msg['FromUserName'], r)
                    getReply = True
                    break
        if not getReply:
            client.send_msg(msg['FromUserName'],
                    '\n'.join(tuling.get_response(msg['Content'])) if TULING else 'I received: %s'%msg['Content'])
        out.print_line('%s: %s'%(s.find_nickname(msg['FromUserName']), msg['Content']))
    elif msg['MsgType'] == 'Map':
        client.send_msg(msg['FromUserName'], 'You are there!')
        out.print_line('%s is at %s'%(s.find_nickname(msg['FromUserName']), msg['Content']))
    elif msg['MsgType'] == 'Picture':
        client.send_msg(msg['FromUserName'], 'Picture received')
        out.print_line('%s sent a picture [%s]'%(s.find_nickname(msg['FromUserName']), msg['Content']))
    elif msg['MsgType'] == 'Recording':
        client.send_msg(msg['FromUserName'], 'Nice Voice!')
        out.print_line('%s sent a recording'%(s.find_nickname(msg['FromUserName'])))
    elif msg['MsgType'] == 'Card':
        client.send_msg(msg['FromUserName'], 'Greeting, %s!'%msg['Content'])
        out.print_line('%s sent a business card of [%s]'%(s.find_nickname(msg['FromUserName']), msg['Content']))
    elif msg['MsgType'] == 'Sharing':
        client.send_msg(msg['FromUserName'], '"%s" is good!'%msg['Content'])
        out.print_line('%s sent a web about [%s]'%(s.find_nickname(msg['FromUserName']), msg['Content']))
    elif msg['MsgType'] == 'Attachment':
        client.send_msg(msg['FromUserName'], '"%s" received'%msg['Content'])
        out.print_line('%s sent an attachment: [%s]'%(s.find_nickname(msg['FromUserName']), msg['Location']))
    elif msg['MsgType'] == 'Video':
        client.send_msg(msg['FromUserName'], 'I received a video')
        out.print_line('%s sent a video [%s]'%(s.find_nickname(msg['FromUserName']), msg['Content']))
    elif msg['MsgType'] == 'Note':
        out.print_line('Notification: %s'%(msg['Content']))
    else:
        pass#out.print_line(str(msg)
