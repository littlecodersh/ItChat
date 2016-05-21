import time
import itchat



def simple_reply():
    @itchat.msg_register
    def simple_reply(msg):
        if msg.get('Type', '') == 'Text':
            return 'I received: %s'%msg.get('Content', '')
    itchat.run()

def complex_reply():

    @itchat.msg_register(['Text', 'Map', 'Card', 'Note', 'Sharing'])
    def text_reply(msg):
        itchat.send('%s: %s'%(msg['Type'], msg['Text']), msg['FromUserName'])

    @itchat.msg_register(['Picture', 'Recording', 'Attachment', 'Video'])
    def download_files(msg):
        fileDir = '%s%s'%(msg['Type'], int(time.time()))
        msg['Text'](fileDir)
        itchat.send('%s received'%msg['Type'], msg['FromUserName'])
        itchat.send('@%s@%s'%('img' if msg['Type'] == 'Picture' else 'fil', fileDir), msg['FromUserName'])

    @itchat.msg_register('Friends')
    def add_friend(msg):
        itchat.add_friend(**msg['Text'])
        itchat.get_contract()
        itchat.send('Nice to meet you!', msg['RecommendInfo']['UserName'])

    @itchat.msg_register('Text', isGroupChat = True)
    def text_reply(msg):
        itchat.send(u'@%s\u2005I received: %s'%(msg['ActualNickName'], msg['Content']), msg['FromUserName'])

    itchat.run()

if __name__ == '__main__':
    itchat.auto_login()
    # simple_reply()
    complex_reply()
