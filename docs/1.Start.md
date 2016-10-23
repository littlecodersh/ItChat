# 入门

## 最简单的回复

通过如下代码，可以完成回复所有文本信息（包括群聊，公众号）。

```python
import itchat
from itchat.content import TEXT

@itchat.msg_register(TEXT, isFriendChat=True, isGroupChat=True, isMpChat=True)
def simple_reply(msg):
    return 'I received: %s' % msg['Content']

itchat.auto_login()
itchat.run()
```

## 常用消息的配置

itchat支持所有的消息类型与群聊，下面的示例中演示了对于这些消息类型简单的配置。

```python
#coding=utf8
import itchat
from itchat.content import *

@itchat.msg_register([TEXT, MAP, CARD, NOTE, SHARING])
def text_reply(msg):
    itchat.send('%s: %s' % (msg['Type'], msg['Text']), msg['FromUserName'])

# 以下四类的消息的Text键下存放了用于下载消息内容的方法，传入文件地址即可
@itchat.msg_register([PICTURE, RECORDING, ATTACHMENT, VIDEO])
def download_files(msg):
    msg['Text'](msg['FileName'])
    return '@%s@%s' % ({'Picture': 'img', 'Video': 'vid'}.get(msg['Type'], 'fil'), msg['FileName'])

# 收到好友邀请自动添加好友
@itchat.msg_register(FRIENDS)
def add_friend(msg):
    itchat.add_friend(**msg['Text']) # 该操作会自动将新好友的消息录入，不需要重载通讯录
    itchat.send_msg('Nice to meet you!', msg['RecommendInfo']['UserName'])

# 在注册时增加isGroupChat=True将判定为群聊回复
@itchat.msg_register(TEXT, isGroupChat = True)
def groupchat_reply(msg):
    if msg['isAt']:
        itchat.send(u'@%s\u2005I received: %s' % (msg['ActualNickName'], msg['Content']), msg['FromUserName'])

itchat.auto_login(True)
itchat.run()
```

当然这里不需要深究为什么这些东西可以这么写，我在这里放出了示例程序只是为了给你一个该sdk相关代码大概样子的概念。

有了大概的模式的了解之后我们就可以进入下一部分的介绍。
