# itchat

[![Gitter](https://badges.gitter.im/littlecodersh/ItChat.svg)](https://gitter.im/littlecodersh/ItChat?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge) ![python](https://img.shields.io/badge/python-2.7-ff69b4.svg) ![python](https://img.shields.io/badge/python-3.5-red.svg) [中文版](https://github.com/littlecodersh/ItChat/blob/master/README.md)

itchat is an open source api for WeChat, a commonly-used Chinese social networking app, you can easily access your personal wechat account through itchat in cmd.

Wechat is structured with a wechat robot and a command line, you can view them in [robot branch](https://github.com/littlecodersh/ItChat/tree/robot).

A wechat robot can handle all the basic messages with only less than 30 lines of codes.

Now Wechat is an important part of personal life, hopefully this repo can help you extend your personal wechat account's functionality and enbetter user's experience with wechat.

Python 2.7.11 version is also available [here](https://github.com/littlecodersh/ItChat/tree/py3-dev).

## Documents

You may get the document of this api from [here](https://itchat.readthedocs.org/zh/latest/).

## Installation

itchat can be installed with this little one-line command:

```python
pip install itchat
```

## Simple uses

The following is a demo of how itchat is configured to fetch and reply daily information.

```python
import itchat, time

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
    itchat.send_msg('Nice to meet you!', msg['RecommendInfo']['UserName'])

@itchat.msg_register('Text', isGroupChat = True)
def text_reply(msg):
    if msg['isAt']:
        itchat.send(u'@%s\u2005I received: %s'%(msg['ActualNickName'], msg['Content']), msg['FromUserName'])

itchat.auto_login()
itchat.run()
```

## Have a try

This QRCode is a wechat account based on the framework of [robot branch](https://github.com/littlecodersh/ItChat/tree/robot). Seeing is believing, so have a try:)

![QRCode](http://7xrip4.com1.z0.glb.clouddn.com/ItChat%2FQRCode2.jpg?imageView/2/w/400/)

## Screenshots

![file_autoreply](http://7xrip4.com1.z0.glb.clouddn.com/ItChat%2FScreenshots%2F%E5%BE%AE%E4%BF%A1%E8%8E%B7%E5%8F%96%E6%96%87%E4%BB%B6%E5%9B%BE%E7%89%87.png?imageView/2/w/300/) ![login_page](http://7xrip4.com1.z0.glb.clouddn.com/ItChat%2FScreenshots%2F%E7%99%BB%E5%BD%95%E7%95%8C%E9%9D%A2%E6%88%AA%E5%9B%BE.jpg?imageView/2/w/450/)

## FAQ

Q: Why I can't upload files whose name is not purely english?

A: This is caused because of the encoding of `requests`, you may fix it by placing [fields.py](https://github.com/littlecodersh/ItChat/blob/robot/plugin/config/fields.py) in packages/urllib of requests.

Q: Why I still can't show QRCode with command line after I set enableCmdQr key to True in itchat.auto_login()?

A: That's because you need to install optional site-package pillow, try this script: pip install pillow

## Author

[LittleCoder](https://github.com/littlecodersh): Structure and py2 version

[Chyroc](https://github.com/Chyroc): py3 version

## See also

[liuwons/wxBot](https://github.com/liuwons/wxBot): A wechat robot similiar to the robot branch

[zixia/wechaty](https://github.com/zixia/wechaty): wechat for bot in Javascript(ES6), Personal Account Robot Framework/Library.

## Comments

If you have any problems or suggestions, feel free to put it up in this [Issue](https://github.com/littlecodersh/ItChat/issues/1).

Or you may also use [![Gitter](https://badges.gitter.im/littlecodersh/ItChat.svg)](https://gitter.im/littlecodersh/ItChat?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge)
