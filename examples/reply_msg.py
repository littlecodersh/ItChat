import itchat

# 运行前请确认已经安装itchat：pip install itchat
# 对于朋友发来的TEXt信息，会回复完全一样的信息
@itchat.msg_register(itchat.content.TEXT)
def text_reply(msg):
    return msg['Text']

itchat.auto_login()
itchat.run()
