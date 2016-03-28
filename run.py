import time
import itchat

itchat.auto_login()

def simple_reply():
    @itchat.msg_dealer
    def simple_reply(msg):
        if msg.get('Type', '') == 'Text':
            return 'I received: %s'%msg.get('Content', '')

    while 1:
        simple_reply()
        time.sleep(1)

def complex_reply():

    @itchat.msg_dealer(['Text', 'Map', 'Card', 'Note', 'Sharing'])
    def text_reply(msg):
        itchat.send('%s: %s'%(msg['Type'], msg['Text']), msg['FromUserName'])

    @itchat.msg_dealer(['Picture', 'Recording', 'Attachment', 'Video'])
    def download_files(msg):
        fileDir = '%s%s'%(msg['Type'], int(time.time()))
        msg['Text'](fileDir)
        itchat.send('%s received'%msg['Type'], msg['FromUserName'])
        itchat.send('@%s@%s'%('img' if msg['Type'] == 'Picture' else 'fil', fileDir), msg['FromUserName'])

    @itchat.msg_dealer('Friends')
    def add_friend(msg):
        print msg['Text']
        itchat.add_friend(**msg['Text'])
        itchat.get_contract()
        itchat.send_msg(msg['RecommendInfo']['UserName'], 'Nice to meet you!')

    @itchat.msg_dealer('Text', isGroupChat = True)
    def text_reply(msg):
        itchat.send(u'@%s\u2005I received: %s'%(msg['ActualNickName'], msg['Content']), msg['FromUserName'])

    itchat.run()

if __name__ == '__main__':
    complex_reply()
