# 入门

## 最简单的回复

通过如下代码，可以完成回复所有文本信息（包括群聊，公众号）。

```python
import itchat
from itchat.content import TEXT

@itchat.msg_register(TEXT, isFriendChat=True, isGroupChat=True, isMpChat=True)
def simple_reply(msg):
    return 'I received: %s' % msg.text

itchat.auto_login(True)
itchat.run()
```

## 常用消息的配置

itchat支持所有的消息类型与群聊，下面的示例中演示了对于这些消息类型简单的配置。

```python
import itchat, time
from itchat.content import *

@itchat.msg_register([TEXT, MAP, CARD, NOTE, SHARING])
def text_reply(msg):
    msg.user.send('%s: %s' % (msg.type, msg.text))

@itchat.msg_register([PICTURE, RECORDING, ATTACHMENT, VIDEO])
def download_files(msg):
    msg.download(msg.fileName)
    typeSymbol = {
        PICTURE: 'img',
        VIDEO: 'vid', }.get(msg.type, 'fil')
    return '@%s@%s' % (typeSymbol, msg.fileName)

@itchat.msg_register(FRIENDS)
def add_friend(msg):
    msg.user.verify()
    msg.user.send('Nice to meet you!')

@itchat.msg_register(TEXT, isGroupChat=True)
def text_reply(msg):
    if msg.isAt:
        msg.user.send(u'@%s\u2005I received: %s' % (
            msg.actualNickName, msg.text))

itchat.auto_login(True)
itchat.run(True)
```

当然这里不需要深究为什么这些东西可以这么写，我在这里放出了示例程序只是为了给你一个该sdk相关代码大概样子的概念。

有了大概的模式的了解之后我们就可以进入下一部分的介绍。
