# 手把手教你扩展个人微信号（2）

现在的日常生活已经离不开微信，本文将会抛砖引玉演示如何使用Python调用微信API做一些有意思的东西。

看完这一系列教程，你就能从头开始实现自己关于微信的想法。

本文为教程的第二部分，主要以微信控制器、群发助手、好友删除检测为例演示如何调用微信API。

Python基础并不困难，所以即使没有这方面基础辅助搜索引擎也完全可以学习本教程。

关于本教程有任何建议或者疑问，都欢迎邮件与我联系（i7meavnktqegm1b@qq.com），或者在[github][main-page]上提出。

## 教程流程简介

这一系列教程从如何分析微信协议开始，[第一部分][tutoral#1]教你如何从零开始获取并模拟扩展个人微信号所需要的协议。

第二部分将会就这些协议进行利用，以各项目为例介绍一些微信有意思功能的实现。

第三部分就协议的一些高级用法进行介绍，对框架做进一步介绍与扩展。

本文为教程的第二部分。

## 简单成果展示

完成了本文的学习，你将会完成三个小项目：（出于方便二次阅读，括号中都放上了源码链接）

* 通过微信操作的音乐播放器（[源码][demo-pcmusicviawechat]）
* 消息内容与对象可自定义的消息群发助手（[源码][demo-wechatsmartwish]）
* 特定好友删除检测（[源码][demo-wechatcheckfriend]）

使用微信协议完成机器人较为平常，如果对具体细节感兴趣，可以添加个人号`littlecodersh`并回复“源代码”。

本文主要基于微信API的第三方包itchat，你可以在[项目主页][main-page]获取更多信息。

## 本部分所需环境

本文是这一教程的第二部分，需要基本的pip可用的Python环境。

本教程使用的环境如下：

* Windows 8.1 （其他平台也可用）
* Python 2 or 3
* 微信版本6.3.25

## 微信控制器

![pic0][demo-pcmusicviawechat-0] ![pic1][demo-pcmusicviawechat-1]

在项目主页上，专门有人就微信作为智能家居入口向我提出了很多想法。

如果微信可以作为控制器，就可以不必自制手机端客户端的麻烦。

其实这个需求实现起来非常简单，这里我借鉴了yaphone的[RasWxMusicbox][yaphone-raswxmusicbox]，使用了其中部分的代码作为演示。

这是一个通过微信控制电脑播放音乐的小项目，那么主要就是三个功能：
* 输入“帮助”，显示帮助
* 输入“关闭”，关闭音乐播放
* 输入具体歌名，进入歌曲的选择

换成代码就是这样一个逻辑：
```python
if msg == u'关闭':
    close_music()
    print(u'音乐已关闭')
if msg == u'帮助':
    print(u'帮助信息')
else:
    print(interact_select_song(msg))
```

那么现在需要解决的就是如何关闭音乐，如何选择音乐和如何使用微信交互。

关闭音乐我们这里使用打开空文件的方式，而选择音乐我们使用网易云音乐的API完成：
```python
import os
# 通过该命令安装该API： pip install NetEaseMusicApi
from NetEaseMusicApi import interact_select_song

with open('stop.mp3', 'w') as f: pass
def close_music():
    os.startfile('stop.mp3')
```

而微信的调用可以通过itchat包简单的完成，这里要注意的是：

* 有些账号无法与自己通信，所以我们选择与文件传输助手（filehelper）通信
* 为了防止对于其他消息的响应，我们在第一行过滤了无关信息
* itchat.run的选项分别为允许热拔插，方便调试

```python
# 接上段程序
# 通过该命令安装该API： pip install itchat
import itchat

@itchat.msg_register(itchat.content.TEXT)
def music_player(msg):
    if msg['ToUserName'] != 'filehelper': return
    if msg['Text'] == u'关闭':
        close_music()
        itchat.send(u'音乐已关闭', 'filehelper')
    if msg['Text'] == u'帮助':
        itchat.send(u'帮助信息', 'filehelper')
    else:
        itchat.send(interact_select_song(msg['Text']), 'filehelper')

itchat.auto_login(True)
itchat.send(HELP_MSG, 'filehelper') 
itchat.run()
```

itchat对常用功能都做好了封装，调用还是非常容易的。

完整的程序我放在了[gist][demo-pcmusicviawechat]上面，使用时不要忘记安装第三方包。

通过与文件传输助手的交互，微信就能够轻松变成其他程序的入口。

## 群发助手

在短信的时代，逢年过节都会需要接收和发送大量的短信。

虽然自己也看到短信就烦，但不发又怕会错过什么。

所以当时就产生了各式各样的群发工具，最简单的比如在消息中加入昵称，让人感觉不像群发。

不过可惜的是，微信自带的群发助手真的只是群发。

当然，稍加操作，一切皆有可能。

例如在消息中加入昵称：

* 通过`get_friends`方法可以轻松获取所有的好友（好友首位是自己）
* 基于不同的好友可以发送不同的消息
* 这条程序运行后是真的会发消息出去，如果只是演示目的，把`itchat.send`改为`print`即可

```python
#coding=utf8
import itchat, time

itchat.auto_login(True)

SINCERE_WISH = u'祝%s新年快乐！'

friendList = itchat.get_friends(update=True)[1:]
for friend in friendList:
    # 如果是演示目的，把下面的方法改为print即可
    itchat.send(SINCERE_WISH % (friend['DisplayName']
        or friend['NickName']), friend['UserName'])
    time.sleep(.5)
```

又例如给特定的人发送特定的消息。

我们这里通过群聊实现，划定一个群聊，在群聊内则私信发送祝福。

* 如果仅是创建群聊不说话，对方是不会有提示的
* 群聊如果不**保存到通讯录**，是无法在各设备之间同步的（所以itchat也无法读取到）
* 群聊在被获取的时候不会自带用户列表，所以需要使用`update_chatroom`更新用户列表
* 当然，如果只是演示目的，把`itchat.send`改为`print`即可

```python
#coding=utf8
import itchat, time

itchat.auto_login(True)

REAL_SINCERE_WISH = u'祝%s新年快乐！！'

chatroomName='wishgroup'
itchat.get_chatrooms(update=True)
chatrooms = itchat.search_chatrooms(name=chatroomName)
if chatrooms is None:
    print(u'没有找到群聊：' + chatroomName)
else:
    chatroom = itchat.update_chatroom(chatrooms[0]['UserName'])
    for friend in chatroom['MemberList']:
        friend = itchat.search_friends(userName=friend['UserName'])
        # 如果是演示目的，把下面的方法改为print即可
        itchat.send(REAL_SINCERE_WISH % (friend['DisplayName']
            or friend['NickName']), friend['UserName'])
        time.sleep(.5)
```

所以我的通讯录里会有从来不用的客户群、教师群什么的。

完整的程序我放在了[gist][demo-wechatsmartwish]上面，使用时不要忘记安装第三方包。

当然，为了防止误操作，完整程序中我把所有的`itchat.send`换成了`print`。

另外，不只有文字可以发送，文件、图片也都是可行的，具体操作见itchat的[文档][document]了。

itchat获取微信可以获取到的各种内容也都非常方便。

其余的例如生日，节日什么的就看具体需求了。

## 好友删除检测

![pic][demo-wechatcheckfriend-0]

有时候我们会想知道某个好友有没有删除自己或者把自己拉入黑名单。

这一操作使用itchat也会变的非常简单。

原理的话，在于将好友拉入群聊时，非好友和黑名单好友不会被拉入群聊。

所以群聊的返回值中就有了好友与你关系的数据。

另外，群聊在第一次产生普通消息时才会被除创建者以外的人发现的（系统消息不算普通消息）。

这样，就可以隐蔽的完成好友检测。

写成代码的话，这个操作就是这样的：（只是演示，不能运行，运行版本在段末）

```python
chatroomUserName = '@1234567'
friend = itchat.get_friends()[1]

r = itchat.add_member_into_chatroom(chatroomUserName, [friend])
if r['BaseResponse']['ErrMsg'] == '':
    status = r['MemberList'][0]['MemberStatus']
    itchat.delete_member_from_chatroom(chatroom['UserName'], [friend])
    return { 3: u'该好友已经将你加入黑名单。',
        4: u'该好友已经将你删除。', }.get(status,
        u'该好友仍旧与你是好友关系。')
```

其中，通过`add_member_into_chatroom`操作获取我们需要的返回值，即可得到好友的状态。

同样的，这次我们也将文件传输助手作为终端，具体方法与控制器一节类似。

这次我们确定的交互方式是接收“名片”消息，并判断名片中的好友与自己的关系。

那么获取名片信息的内容可以这么写：

```python
import itchat

@itchat.msg_register(itchat.content.CARD)
def get_friend(msg):
    if msg['ToUserName'] != 'filehelper': return
    friendStatus = get_friend_status(msg['RecommendInfo'])
    itchat.send(friendStatus['NickName'], 'filehelper')

itchat.auto_login(True)
itchat.run()
```

那么我们所需要的所有部分就都解决了，下面将他们组合起来即可。

完整的程序我放在了[gist][demo-wechatcheckfriend]上面，使用时不要忘记安装第三方包。

在网页版微信的接口受到限制之前完全可以批量进行这一操作，检测哪些好友删除了自己。

但目前显然操作存在频率限制，所以只能做一些变通了。

## 之后的内容

到这里这一篇文章的主要内容就结束了。

主要从微信作为终端使用、自定义的消息交互、微信协议研究三方面开了一个简单的头。

其余有一些过于大众，如机器人，就不再赘述。

而另一些，需要一定的基础或者不适合分享，就留给各位自行研究。

如果要留个悬念，可以想象添加好友的方法status传2，轻松实现好友病毒式扩张。

利用微信的API可以做很多事情，文档我放在[这里][document]，祝好运！

## 结束语

希望读完这篇文章能对你有帮助，有什么不足之处万望指正（鞠躬）。

有什么想法或者想要关注我的更新，欢迎来[**Github**](https://github.com/littlecodersh/ItChat)上***Star***或者***Fork***。

160928

LittleCoder

EOF


[document]: http://itchat.readthedocs.io/zh/latest/
[main-page]: https://github.com/littlecodersh/ItChat
[tutoral#1]: http://python.jobbole.com/84918/
[yaphone-raswxmusicbox]: https://github.com/yaphone/RasWxMusicbox
[demo-pcmusicviawechat]: https://gist.github.com/littlecodersh/8468afbbb8d34c0c0e6848b6f9009c4c
[demo-wechatsmartwish]: https://gist.github.com/littlecodersh/ae13ed93e0e8f3c820226fc6871f436d
[demo-wechatcheckfriend]: https://gist.github.com/littlecodersh/3fef7d2afb2d502e4735be083c9f79e1
[demo-pcmusicviawechat-0]: http://7xrip4.com1.z0.glb.clouddn.com/ItChat/Tutorial/2/demo-pcmusicviawechat-0.png?imageView/2/w/200/
[demo-pcmusicviawechat-1]: http://7xrip4.com1.z0.glb.clouddn.com/ItChat/Tutorial/2/demo-pcmusicviawechat-1.png?imageView/2/w/200/
[demo-wechatcheckfriend-0]: http://7xrip4.com1.z0.glb.clouddn.com/ItChat/Tutorial/2/demo-wechatcheckfriend.png?imageView/2/w/200/
