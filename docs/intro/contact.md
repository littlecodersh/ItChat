在使用个人微信的过程当中主要有三种账号需要获取，分别为：

* 好友
* 公众号
* 群聊

itchat为这三种账号都提供了整体获取方法与搜索方法。

而群聊多出获取用户列表方法以及创建群聊、增加、删除用户的方法。

这里我们分这三种分别介绍如何使用。

在本章的最后还介绍了如何通过Uin唯一的确定好友与群聊。

## 好友

好友的获取方法为`get_friends`，将会返回完整的好友列表。

* 其中每个好友为一个字典
* 列表的第一项为本人的账号信息
* 传入update键为True将可以更新好友列表并返回

好友的搜索方法为`search_friends`，有四种搜索方式：
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

更新用户信息的方法为`update_friend`。

* 该方法需要传入用户的`UserName`，返回指定用户的最新信息
* 同样也可以传入`UserName`组成的列表，那么相应的也会返回指定用户的最新信息组成的列表

```python
memberList = itchat.update_friend('@abcdefg1234567')
```

## 公众号

公众号的获取方法为`get_mps`，将会返回完整的公众号列表。

* 其中每个公众号为一个字典
* 传入update键为True将可以更新公众号列表并返回

公众号的搜索方法为`search_mps`，有两种搜索方法：
1. 获取特定`UserName`的公众号
2. 获取名字中含有特定字符的公众号

如果两项都做了特定，将会仅返回特定`UserName`的公众号，下面是示例程序：

```python
# 获取特定UserName的公众号，返回值为一个字典
itchat.search_mps(userName='@abcdefg1234567')
# 获取名字中含有特定字符的公众号，返回值为一个字典的列表
itchat.search_mps(name='LittleCoder')
# 以下方法相当于仅特定了UserName
itchat.search_mps(userName='@abcdefg1234567', name='LittleCoder')
```

## 群聊

群聊的获取方法为`get_chatrooms`，将会返回完整的群聊列表。

* 其中每个群聊为一个字典
* 传入update键为True将可以更新群聊列表并返回通讯录中保存的群聊列表
* 群聊列表为后台自动更新，如果中途意外退出存在极小的概率产生本地群聊消息与后台不同步
* 为了保证群聊信息在热启动中可以被正确的加载，即使不需要持续在线的程序也需要运行`itchat.run()`
* 如果不想要运行上述命令，请在退出程序前调用`itchat.dump_login_status()`，更新热拔插需要的信息

群聊的搜索方法为`search_chatrooms`，有两种搜索方法：
1. 获取特定`UserName`的群聊
2. 获取名字中含有特定字符的群聊

如果两项都做了特定，将会仅返回特定`UserName`的群聊，下面是示例程序：

```python
# 获取特定UserName的群聊，返回值为一个字典
itchat.search_chatrooms(userName='@@abcdefg1234567')
# 获取名字中含有特定字符的群聊，返回值为一个字典的列表
itchat.search_chatrooms(name='LittleCoder')
# 以下方法相当于仅特定了UserName
itchat.search_chatrooms(userName='@@abcdefg1234567', name='LittleCoder')
```

群聊用户列表的获取方法为`update_chatroom`。

* 同样，如果想要更新该群聊的其他信息也可以用该方法
* 群聊在首次获取中不会获取群聊的用户列表，所以需要调用该命令才能获取群聊的成员
* 该方法需要传入群聊的`UserName`，返回特定群聊的详细信息
* 同样也可以传入`UserName`组成的列表，那么相应的也会返回指定用户的最新信息组成的列表

```python
memberList = itchat.update_chatroom('@@abcdefg1234567', detailedMember=True)
```

创建群聊、增加、删除群聊用户的方法如下所示：

* 由于之前通过群聊检测是否被好友拉黑的程序，目前这三个方法都被严格限制了使用频率
* 删除群聊需要本账号为群管理员，否则会失败
* 将用户加入群聊有直接加入与发送邀请，通过`useInvitation`设置
* 超过40人的群聊无法使用直接加入的加入方式，特别注意

```python
memberList = itchat.get_friends()[1:]
# 创建群聊，topic键值为群聊名
chatroomUserName = itchat.create_chatroom(memberList, 'test chatroom')
# 删除群聊内的用户
itchat.delete_member_from_chatroom(chatroomUserName, memberList[0])
# 增加用户进入群聊
itchat.add_member_into_chatroom(chatroomUserName, memberList[0], useInvitation=False)
```

## Uins

Uin 就是微信中用于标识用户的方式，每一个用户、群聊都有唯一且不同的Uin。

那么通过Uin，即使退出了重新登录，也可以轻松的确认正在对话的是上一次登陆的哪一个用户。

但注意，Uin与其他值不同，微信后台做了一定的限制，必须通过特殊的操作才能获取。

最简单来说，首次点开登陆用的手机端的某个好友或者群聊，itchat就能获取到该好友或者群聊的Uin。

如果想要通过程序获取，也可以用程序将某个好友或者群聊置顶（取消置顶）。

这里提供一个提示群聊更新的程序：

```python
import re, sys, json

import itchat
from itchat.content import *

itchat.auto_login(True)

@itchat.msg_register(SYSTEM)
def get_uin(msg):
    if msg['SystemInfo'] != 'uins': return
    ins = itchat.instanceList[0]
    fullContact = ins.memberList + ins.chatroomList + ins.mpList
    print('** Uin Updated **')
    for username in msg['Text']:
        member = itchat.utils.search_dict_list(
            fullContact, 'UserName', username)
        print(('%s: %s' % (
            member.get('NickName', ''), member['Uin']))
            .encode(sys.stdin.encoding, 'replace'))

itchat.run(True)
```

每当Uin更新了，就会打印相应的更新情况。

同样的，如果你想要获取Uin更新的情况也通过获取SYSTEM类型消息实现。
