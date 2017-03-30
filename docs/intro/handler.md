# 注册消息方法

itchat将根据接收到的消息类型寻找对应的已经注册的方法。

如果一个消息类型没有对应的注册方法，该消息将会被舍弃。

在运行过程当中也可以动态注册方法，注册方式与结果不变。

## 注册

你可以通过两种方式注册消息方法

```python
import itchat
from itchat.content import *

# 不带具体对象注册，将注册为普通消息的回复方法
@itchat.msg_register(TEXT)
def simple_reply(msg):
    return 'I received: %s' % msg['Text']

# 带对象参数注册，对应消息对象将调用该方法
@itchat.msg_register(TEXT, isFriendChat=True, isGroupChat=True, isMpChat=True)
def text_reply(msg):
    msg.user.send('%s: %s' % (msg.type, msg.text))
```

## 消息类型

向注册方法传入的msg包含微信返回的字典的所有内容。

本api增加`Text`、`Type`（也就是参数）键值，方便操作。

itchat.content中包含所有的消息类型参数，内容如下表所示：

参数       |类型       |Text键值        
:----------|:----------|:---------------
TEXT       |文本       |文本内容        
MAP        |地图       |位置文本        
CARD       |名片       |推荐人字典      
NOTE       |通知       |通知文本        
SHARING    |分享       |分享名称        
PICTURE    |图片/表情  |下载方法        
RECORDING  |语音       |下载方法        
ATTACHMENT |附件       |下载方法        
VIDEO      |小视频     |下载方法        
FRIENDS    |好友邀请   |添加好友所需参数
SYSTEM     |系统消息   |更新内容的用户或群聊的UserName组成的列表

比如你需要存储发送给你的附件：

```python
@itchat.msg_register(ATTACHMENT)
def download_files(msg):
    msg['Text'](msg['FileName'])
```

值得注意的是，群消息增加了三个键值：

* isAt: 判断是否@本号
* ActualNickName: 实际NickName
* Content: 实际Content

可以通过本程序测试：

```python
import itchat
from itchat.content import TEXT

@itchat.msg_register(TEXT, isGroupChat=True)
def text_reply(msg):
    print(msg.isAt)
    print(msg.actualNickName)
    print(msg.text)

itchat.auto_login()
itchat.run()
```

## 注册消息的优先级

优先级分别为：后注册消息先于先注册消息，带参数消息先于不带参数消息。

以下面的两个程序为例：

```python
import itchat
from itchat.content import *

itchat.auto_login()

@itchat.msg_register(TEXT)
def text_reply(msg):
    return 'This is the old register'
    
@itchat.msg_register(TEXT)
def text_reply(msg):
    return 'This is a new one'

itchat.run()
```

在私聊发送文本时将会回复`This is a new one`。
```python
import itchat
from itchat.content import *

itchat.auto_login()

@itchat.msg_register
def general_reply(msg):
    return 'I received a %s' % msg.type
    
@itchat.msg_register(TEXT)
def text_reply(msg):
    return 'You said to me one to one: %s' % msg.text

itchat.run()
```

仅在私聊发送文本时将会回复`You said to me one to one`，其余情况将会回复`I received a ...`。

## 动态注册消息

动态注册时可以选择将`itchat.run()`放入另一线程或使用`configured_reply()`方法处理消息。

两种方法分别是：

```python
# 使用另一线程，但注意不要让程序运行终止
import thread

thread.start_new_thread(itchat.run, ())

# 使用configured_reply方法
while 1:
    itchat.configured_reply()
    # some other functions
    time.sleep(1)
```

以下给出一个动态注册的例子：

```python
#coding=utf8
import thread

import itchat
from itchat.content import *

replyToGroupChat = True
functionStatus = False

def change_function():
    if replyToGroupChat != functionStatus:
        if replyToGroupChat:
            @itchat.msg_register(TEXT, isGroupChat=True)
            def group_text_reply(msg):
                if u'关闭' in msg['Text']:
                    replyToGroupChat = False
                    return u'已关闭'
                elif u'开启' in msg['Text']:
                    return u'已经在运行'
                return u'输入"关闭"或者"开启"测试功能'
        else:
            @itchat.msg_register(TEXT, isGroupChat=True)
            def group_text_reply(msg):
                if u'开启' in msg['Text']:
                    replyToGroupChat = True
                    return u'重新开启成功'
        functionStatus = replyToGroupChat

thread.start_new_thread(itchat.run, ())

while 1:
    change_function()
    time.sleep(.1)
```
