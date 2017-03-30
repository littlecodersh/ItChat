# 登陆

在上一章中你看到了基本的注册与登陆，而显然登陆使用的是itchat提供了`auto_login`方法，调用即可完成登录。

一般而言，我们都会在完成消息的注册后登陆。

当然这里需要特别强调的是三点，分别是短时间关闭重连、命令行二维码与自定义登陆内容。

* itchat提供了登陆状态暂存，关闭程序后一定时间内不需要扫码即可登录。
* 由于目前微信网页版提供上一次登录的微信号不扫码直接手机确认登陆，所以如果开启登陆状态暂存将会自动使用这一功能。
* 为了方便在无图形界面使用itchat，程序内置了命令行二维码的显示。
* 如果你需要就登录状态就一些修改（例如更改提示语、二维码出现后邮件发送等）。

## 短时间关闭程序后重连

这样即使程序关闭，一定时间内重新开启也可以不用重新扫码。

最简单的用法就是给`auto_login`方法传入值为真的hotReload。

该方法会生成一个静态文件`itchat.pkl`，用于存储登陆的状态。

```python
import itchat
from itchat.content import TEXT

@itchat.msg_register(TEXT)
def simple_reply(msg):
    print(msg.text)

itchat.auto_login(hotReload=True)
itchat.run()
```

通过设置statusStorageDir可以将静态文件指定为其他的值。

这一内置选项其实就相当于使用了以下两个函数的这一段程序：

```python
import itchat
from itchat.content import TEXT

if itchat.load_login_status():
    @itchat.msg_register(TEXT)
    def simple_reply(msg):
        print(msg['Text'])
    itchat.run()
    itchat.dump_login_status()
else:
    itchat.auto_login()
    itchat.dump_login_status()
    print('Config stored, so exit.')
```

其中load_login_status与dump_login_status分别对应读取与导出设置。

通过设置传入的fileDir的值可以设定导入导出的文件。

## 命令行二维码显示

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

## 自定义登录过程

如果需要控制登录的过程，可以阅读下面的内容。

同时itchat也提供了登陆所需的每一步的方法，登陆的过程按顺序为：

* 获取二维码uuid
* 获取二维码
* 判断是否已经登陆成功
* 获取初始化数据
* 更新微信相关信息（通讯录、手机登陆状态）
* 循环扫描新信息（开启心跳）

### 获取二维码uuid

获取生成二维码所需的uuid，并返回。

* 方法名称：`get_QRuuid`
* 所需值：无
* 返回值：成功->uuid，失败->None

### 获取二维码

根据uuid获取二维码并打开，返回是否成功。

* 方法名称：`get_QR`
* 所需值：uuid
* 返回值：成功->True，失败->False

### 判断是否已经登陆成功

判断是否已经登陆成功，返回扫描的状态码。

* 方法名称：`check_login`
* 所需值：uuid
* 返回值：登陆成功->'200'，已扫描二维码->'201'，二维码失效->'408'，未获取到信息->'0'

### 获取初始化数据

获取微信用户信息以及心跳所需要的数据。

* 方法名称：`web_init`
* 所需值：无
* 返回值：存储登录微信用户信息的字典

### 获取微信通讯录

获取微信的所有好友信息并更新。

* 方法名称：`get_friends`（曾用名：`get_contact`）
* 所需值：无
* 返回值：存储好友信息的列表

### 更新微信手机登陆状态

在手机上显示登录状态。

* 方法名称：`show_mobile_login`
* 所需值：无
* 返回值：无

### 循环扫描新信息（开启心跳）

循环扫描是否有新的消息，开启心跳包。

* 方法名称：`start_receiving`
* 所需值：无
* 返回值：无

## 示例

itchat自带的`auto_login`通过如下代码可以实现：

```python
import itchat, time, sys

def output_info(msg):
    print('[INFO] %s' % msg)

def open_QR():
    for get_count in range(10):
        output_info('Getting uuid')
        uuid = itchat.get_QRuuid()
        while uuid is None: uuid = itchat.get_QRuuid();time.sleep(1)
        output_info('Getting QR Code')
        if itchat.get_QR(uuid): break
        elif get_count >= 9:
            output_info('Failed to get QR Code, please restart the program')
            sys.exit()
    output_info('Please scan the QR Code')
    return uuid

uuid = open_QR()
waitForConfirm = False
while 1:
    status = itchat.check_login(uuid)
    if status == '200':
        break
    elif status == '201':
        if waitForConfirm:
            output_info('Please press confirm')
            waitForConfirm = True
    elif status == '408':
        output_info('Reloading QR Code')
        uuid = open_QR()
        waitForConfirm = False
userInfo = itchat.web_init()
itchat.show_mobile_login()
itchat.get_friends(True)
output_info('Login successfully as %s'%userInfo['NickName'])
itchat.start_receiving()

# Start auto-replying
@itchat.msg_register
def simple_reply(msg):
    if msg['Type'] == 'Text':
        return 'I received: %s' % msg['Content']
itchat.run()
```
