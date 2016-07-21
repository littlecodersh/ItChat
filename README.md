# itchat

[![Gitter](https://badges.gitter.im/littlecodersh/ItChat.svg)](https://gitter.im/littlecodersh/ItChat?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge) ![python](https://img.shields.io/badge/python-2.7-ff69b4.svg) ![python](https://img.shields.io/badge/python-3.5-red.svg) [English version](https://github.com/littlecodersh/ItChat/blob/master/README_EN.md)

itchat是一个开源的微信个人号接口，使用他你可以轻松的通过命令行使用个人微信号。

微信机器人的实现及命令行版微信见[robot分支](https://github.com/littlecodersh/ItChat/tree/robot)，Python 3.5.1 的版本可见这里：[here](https://github.com/littlecodersh/ItChat/tree/py3-dev)。

使用不到三十行的代码，你就可以完成一个能够处理所有信息的微信机器人。

如今微信已经成为了个人社交的很大一部分，希望这个项目能够帮助你扩展你的个人的微信号、方便自己的生活。


## Documents

你可以在[这里](https://itchat.readthedocs.org/zh/latest/)获取api的使用帮助。

## Installation

可以通过本命令安装itchat：

```python
pip install itchat
```

## Simple uses

通过如下代码，微信已经可以就日常的各种信息进行获取与回复。

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

这是一个基于这一项目的[开源小机器人](https://github.com/littlecodersh/ItChat/tree/robot)，百闻不如一见，有兴趣可以尝试一下。

![QRCode](http://7xrip4.com1.z0.glb.clouddn.com/ItChat%2FQRCode2.jpg?imageView/2/w/400/)

## Screenshots

![file_autoreply](http://7xrip4.com1.z0.glb.clouddn.com/ItChat%2FScreenshots%2F%E5%BE%AE%E4%BF%A1%E8%8E%B7%E5%8F%96%E6%96%87%E4%BB%B6%E5%9B%BE%E7%89%87.png?imageView/2/w/300/) ![login_page](http://7xrip4.com1.z0.glb.clouddn.com/ItChat%2FScreenshots%2F%E7%99%BB%E5%BD%95%E7%95%8C%E9%9D%A2%E6%88%AA%E5%9B%BE.jpg?imageView/2/w/450/)

## FAQ

Q: 为什么中文的文件没有办法上传？

A: 这是由于`requests`的编码问题导致的。若需要支持中文文件传输，将[fields.py](https://github.com/littlecodersh/ItChat/blob/robot/plugin/config/fields.py)文件放入requests包的packages/urllib3下即可

Q: 为什么我在设定了`itchat.auto_login()`的`enableCmdQR`为`True`后还是没有办法在命令行显示二维码？

A: 这是由于没有安装可选的包`pillow`，可以使用右边的命令安装：`pip install pillow`

## Author

[LittleCoder](https://github.com/littlecodersh): 整体构架及完成Python2版本。

[Chyroc](https://github.com/Chyroc): 完成Python3版本。

## See also

[liuwons/wxBot](https://github.com/liuwons/wxBot): 类似的基于Python的微信机器人

[zixia/wechaty](https://github.com/zixia/wechaty): 基于Javascript(ES6)的微信个人账号机器人NodeJS框架/库

## Comments

如果有什么问题或者建议都可以在这个[Issue](https://github.com/littlecodersh/ItChat/issues/1)和我讨论

或者也可以在gitter上交流：[![Gitter](https://badges.gitter.im/littlecodersh/ItChat.svg)](https://gitter.im/littlecodersh/ItChat?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge)
