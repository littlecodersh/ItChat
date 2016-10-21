# itchat

[![Gitter][gitter-picture]][gitter] ![py27][py27] ![py35][py35] [English version][english-version]

itchat是一个开源的微信个人号接口，使用python调用微信从未如此简单。

使用不到三十行的代码，你就可以完成一个能够处理所有信息的微信机器人。

当然，该api的使用远不止一个机器人，更多的功能等着你来发现。

如今微信已经成为了个人社交的很大一部分，希望这个项目能够帮助你扩展你的个人的微信号、方便自己的生活。

## Installation

可以通过本命令安装itchat：

```python
pip install itchat
```

## Simple uses

有了itchat，如果你想要回复发给自己的文本消息，只需要这样：

```python
import itchat

@itchat.msg_register(itchat.content.TEXT)
def text_reply(msg):
    itchat.send(msg['Text'], msg['FromUserName'])

itchat.auto_login()
itchat.run()
```

一些进阶应用可以在Advanced uses中看到，或者你也可以阅览[文档][document]。

## Have a try

这是一个基于这一项目的[开源小机器人][robot-source-code]，百闻不如一见，有兴趣可以尝试一下。

![QRCode][robot-qr]

## Screenshots

![file-autoreply][robot-demo-file] ![login-page][robot-demo-login]

## Advanced uses

### 各类型消息的注册

通过如下代码，微信已经可以就日常的各种信息进行获取与回复。

```python
#coding=utf8
import itchat, time
from itchat.content import *

@itchat.msg_register([TEXT, MAP, CARD, NOTE, SHARING])
def text_reply(msg):
    itchat.send('%s: %s' % (msg['Type'], msg['Text']), msg['FromUserName'])

@itchat.msg_register([PICTURE, RECORDING, ATTACHMENT, VIDEO])
def download_files(msg):
    msg['Text'](msg['FileName'])
    return '@%s@%s' % ({'Picture': 'img', 'Video': 'vid'}.get(msg['Type'], 'fil'), msg['FileName'])

@itchat.msg_register(FRIENDS)
def add_friend(msg):
    itchat.add_friend(**msg['Text']) # 该操作会自动将新好友的消息录入，不需要重载通讯录
    itchat.send_msg('Nice to meet you!', msg['RecommendInfo']['UserName'])

@itchat.msg_register(TEXT, isGroupChat=True)
def text_reply(msg):
    if msg['isAt']:
        itchat.send(u'@%s\u2005I received: %s' % (msg['ActualNickName'], msg['Content']), msg['FromUserName'])

itchat.auto_login(True)
itchat.run()
```

### 命令行二维码

通过以下命令可以在登陆的时候使用命令行显示二维码：

```python
itchat.auto_login(enableCmdQR=True)
```

部分系统可能字幅宽度有出入，可以通过将enableCmdQR赋值为特定的倍数进行调整：

```python
# 如部分的linux系统，块字符的宽度为一个字符（正常应为两字符），故赋值为2
itchat.auto_login(enableCmdQR=2)
```

默认控制台背景色为暗色（黑色），若背景色为浅色（白色），可以将enableCmdQR赋值为负值：

```python
itchat.auto_login(enableCmdQR=-1)
```

### 退出程序后暂存登陆状态

通过如下命令登陆，即使程序关闭，一定时间内重新开启也可以不用重新扫码。

```python
itchat.auto_login(hotReload=True)
```

### 用户搜索

使用`search_friends`方法可以搜索用户，有四种搜索方式：
1. 仅获取自己的用户信息
2. 获取特定`UserName`的用户信息
3. 获取备注、微信号、昵称中的任何一项等于`name`键值的用户
4. 获取备注、微信号、昵称分别等于相应键值的用户

其中三、四项可以一同使用，下面是示例程序：

```python
# 获取自己的用户信息，返回自己的属性字典
itchat.search_friends()
# 获取特定UserName的用户信息
itchat.search_friends(userName='@abcdefg1234567')
# 获取任何一项等于name键值的用户
itchat.search_friends(name='littlecodersh')
# 获取分别对应相应键值的用户
itchat.search_friends(wechatAccount='littlecodersh')
# 三、四项功能可以一同使用
itchat.search_friends(name='LittleCoder机器人', wechatAccount='littlecodersh')
```

关于公众号、群聊的获取与搜索在文档中有更加详细的介绍。

### 附件的下载与发送

itchat的附件下载方法存储在msg的Text键中。

发送的文件的文件名（图片给出的默认文件名）都存储在msg的FileName键中。

下载方法接受一个可用的位置参数（包括文件名），并将文件相应的存储。

```python
@itchat.msg_register(['Picture', 'Recording', 'Attachment', 'Video'])
def download_files(msg):
    msg['Text'](msg['FileName'])
    itchat.send('@%s@%s'%('img' if msg['Type'] == 'Picture' else 'fil', msg['FileName']), msg['FromUserName'])
    return '%s received'%msg['Type']
```

如果你不需要下载到本地，仅想要读取二进制串进行进一步处理可以不传入参数，方法将会返回图片的二进制串。

```python
@itchat.msg_register(['Picture', 'Recording', 'Attachment', 'Video'])
def download_files(msg):
    with open(msg['FileName'], 'wb') as f:
        f.write(msg['Text']())
```

## FAQ

Q: 为什么中文的文件没有办法上传？

A: 这是由于`requests`的编码问题导致的。若需要支持中文文件传输，将[fields.py][fields.py-2](py3版本见[这里][fields.py-3])文件放入requests包的packages/urllib3下即可

Q: 为什么我在设定了`itchat.auto_login()`的`enableCmdQR`为`True`后还是没有办法在命令行显示二维码？

A: 这是由于没有安装可选的包`pillow`，可以使用右边的命令安装：`pip install pillow`

Q: 如何通过这个包将自己的微信号变为控制器？

A: 有两种方式：发送、接受自己UserName的消息；发送接收文件传输助手（filehelper）的消息

Q: 为什么我发送信息的时候部分信息没有成功发出来？

A: 有些账号是天生无法给自己的账号发送信息的，建议使用`filehelper`代替。另外，接口调用是有频率限制，限制一下连续发送信息之间的时间间隔即可。

## Author

[LittleCoder][littlecodersh]: 整体构架及完成Python2 Python3版本。

[Chyroc][Chyroc]: 完成第一版本的Python3构架。

## See also

[liuwons/wxBot][liuwons-wxBot]: 类似的基于Python的微信机器人

[zixia/wechaty][zixia-wechaty]: 基于Javascript(ES6)的微信个人账号机器人NodeJS框架/库

## Comments

如果有什么问题或者建议都可以在这个[Issue][issue#1]和我讨论

或者也可以在gitter上交流：[![Gitter][gitter-picture]][gitter]

当然也可以加入我们新建的QQ群讨论：549762872

[gitter-picture]: https://badges.gitter.im/littlecodersh/ItChat.svg
[gitter]: https://gitter.im/littlecodersh/ItChat?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge
[py27]: https://img.shields.io/badge/python-2.7-ff69b4.svg
[py35]: https://img.shields.io/badge/python-3.5-red.svg
[english-version]: https://github.com/littlecodersh/ItChat/blob/master/README_EN.md
[document]: https://itchat.readthedocs.org/zh/latest/
[robot-source-code]: https://gist.github.com/littlecodersh/ec8ddab12364323c97d4e36459174f0d
[robot-qr]: http://7xrip4.com1.z0.glb.clouddn.com/ItChat%2FQRCode2.jpg?imageView/2/w/400/
[robot-demo-file]: http://7xrip4.com1.z0.glb.clouddn.com/ItChat%2FScreenshots%2F%E5%BE%AE%E4%BF%A1%E8%8E%B7%E5%8F%96%E6%96%87%E4%BB%B6%E5%9B%BE%E7%89%87.png?imageView/2/w/300/
[robot-demo-login]: http://7xrip4.com1.z0.glb.clouddn.com/ItChat%2FScreenshots%2F%E7%99%BB%E5%BD%95%E7%95%8C%E9%9D%A2%E6%88%AA%E5%9B%BE.jpg?imageView/2/w/450/
[fields.py-2]: https://gist.github.com/littlecodersh/9a0c5466f442d67d910f877744011705
[fields.py-3]: https://gist.github.com/littlecodersh/e93532d5e7ddf0ec56c336499165c4dc
[littlecodersh]: https://github.com/littlecodersh
[Chyroc]: https://github.com/Chyroc
[liuwons-wxBot]: https://github.com/liuwons/wxBot
[zixia-wechaty]: https://github.com/zixia/wechaty
[issue#1]: https://github.com/littlecodersh/ItChat/issues/1
