# 消息内容

## 微信一般消息内容

```python
{
    "FromUserName": "",
    "ToUserName": "",
    "Content": "",
    "StatusNotifyUserName": "",
    "ImgWidth": 0,
    "PlayLength": 0,
    "RecommendInfo": {},
    "StatusNotifyCode": 0,
    "NewMsgId": "",
    "Status": 0,
    "VoiceLength": 0,
    "ForwardFlag": 0,
    "AppMsgType": 0,
    "Ticket": "",
    "AppInfo": {},
    "Url": "",
    "ImgStatus": 0,
    "MsgType": 0,
    "ImgHeight": 0,
    "MediaId": "",
    "MsgId": "",
    "FileName": "",
    "HasProductId": 0,
    "FileSize": "",
    "CreateTime": 0,
    "SubMsgType": 0
}
```

微信回复的所有消息都遵循这一格式，下面将就每种消息类型具体分析。

## 消息的具体内容

本段部分参考[Urinx的Github](https://github.com/Urinx/WeixinBot)并修改。

### 微信初始化消息

```
MsgType: 51
FromUserName: 自己ID
ToUserName: 自己ID
StatusNotifyUserName: 最近联系的联系人ID
Content:
    <msg>
        <op id='4'>
            <username>
                # 最近联系的联系人
                filehelper,xxx@chatroom,wxid_xxx,xxx,...
            </username>
            <unreadchatlist>
                <chat>
                    <username>
                    # 朋友圈
                        MomentsUnreadMsgStatus
                    </username>
                    <lastreadtime>
                        1454502365
                    </lastreadtime>
                </chat>
            </unreadchatlist>
            <unreadfunctionlist>
            # 未读的功能账号消息，群发助手，漂流瓶等
            </unreadfunctionlist>
        </op>
    </msg>
```

### 文本消息

```
MsgType: 1
FromUserName: 发送方ID
ToUserName: 接收方ID
Content: 消息内容
```

### 图片消息

```
MsgType: 3
FromUserName: 发送方ID
ToUserName: 接收方ID
MsgId: 用于获取图片
Content:
    <msg>
        <img length="6503" hdlength="0" />
        <commenturl></commenturl>
    </msg>
```

itchat添加了Text键，键值为下载该图片的方法。

### 小视频消息

```
MsgType: 62
FromUserName: 发送方ID
ToUserName: 接收方ID
MsgId: 用于获取小视频
Content:
    <msg>
        <img length="6503" hdlength="0" />
        <commenturl></commenturl>
    </msg>
```

itchat添加了Text键，键值为下载该视频的方法。

### 地理位置消息

```
MsgType: 1
FromUserName: 发送方ID
ToUserName: 接收方ID
Content: http://weixin.qq.com/cgi-bin/redirectforward?args=xxx
```

itchat添加了Text键，键值为该地点的文本形式。

### 名片消息

```
MsgType: 42
FromUserName: 发送方ID
ToUserName: 接收方ID
Content:
    <?xml version="1.0"?>
    <msg bigheadimgurl="" smallheadimgurl="" username="" nickname=""  shortpy="" alias="" imagestatus="3" scene="17" province="" city="" sign="" sex="1" certflag="0" certinfo="" brandIconUrl="" brandHomeUrl="" brandSubscriptConfigUrl="" brandFlags="0" regionCode="" />

RecommendInfo:
    {
        "UserName": "xxx", # ID
        "Province": "xxx", 
        "City": "xxx", 
        "Scene": 17, 
        "QQNum": 0, 
        "Content": "", 
        "Alias": "xxx", # 微信号
        "OpCode": 0, 
        "Signature": "", 
        "Ticket": "", 
        "Sex": 0, # 1:男, 2:女
        "NickName": "xxx", # 昵称
        "AttrStatus": 4293221, 
        "VerifyFlag": 0
    }
```

itchat添加了Text键，键值为该调用`add_friend`需要的属性。

### 语音消息

```
MsgType: 34
FromUserName: 发送方ID
ToUserName: 接收方ID
MsgId: 用于获取语音
Content:
    <msg>
        <voicemsg endflag="1" cancelflag="0" forwardflag="0" voiceformat="4" voicelength="1580" length="2026" bufid="216825389722501519" clientmsgid="49efec63a9774a65a932a4e5fcd4e923filehelper174_1454602489" fromusername="" />
    </msg>
```

itchat添加了Text键，键值为下载该语音文件的方法。

### 动画表情

```
MsgType: 47
FromUserName: 发送方ID
ToUserName: 接收方ID
Content:
    <msg>
        <emoji fromusername = "" tousername = "" type="2" idbuffer="media:0_0" md5="e68363487d8f0519c4e1047de403b2e7" len = "86235" productid="com.tencent.xin.emoticon.bilibili" androidmd5="e68363487d8f0519c4e1047de403b2e7" androidlen="86235" s60v3md5 = "e68363487d8f0519c4e1047de403b2e7" s60v3len="86235" s60v5md5 = "e68363487d8f0519c4e1047de403b2e7" s60v5len="86235" cdnurl = "http://emoji.qpic.cn/wx_emoji/eFygWtxcoMF8M0oCCsksMA0gplXAFQNpiaqsmOicbXl1OC4Tyx18SGsQ/" designerid = "" thumburl = "http://mmbiz.qpic.cn/mmemoticon/dx4Y70y9XctRJf6tKsy7FwWosxd4DAtItSfhKS0Czr56A70p8U5O8g/0" encrypturl = "http://emoji.qpic.cn/wx_emoji/UyYVK8GMlq5VnJ56a4GkKHAiaC266Y0me0KtW6JN2FAZcXiaFKccRevA/" aeskey= "a911cc2ec96ddb781b5ca85d24143642" ></emoji> 
        <gameext type="0" content="0" ></gameext>
    </msg>
```

itchat添加了Text键，键值为下载该图片表情的方法。

由于版权问题，部分微信商店提供的表情是无法下载的，注意。

### 普通链接或应用分享消息

```
MsgType: 49
AppMsgType: 5
FromUserName: 发送方ID
ToUserName: 接收方ID
Url: 链接地址
FileName: 链接标题
Content:
    <msg>
        <appmsg appid=""  sdkver="0">
            <title></title>
            <des></des>
            <type>5</type>
            <content></content>
            <url></url>
            <thumburl></thumburl>
            ...
        </appmsg>
        <appinfo>
            <version></version>
            <appname></appname>
        </appinfo>
    </msg>
```

### 音乐链接消息

```
MsgType: 49
AppMsgType: 3
FromUserName: 发送方ID
ToUserName: 接收方ID
Url: 链接地址
FileName: 音乐名

AppInfo: # 分享链接的应用
    {
        Type: 0, 
        AppID: wx485a97c844086dc9
    }

Content:
    <msg>
        <appmsg appid="wx485a97c844086dc9"  sdkver="0">
            <title></title>
            <des></des>
            <action></action>
            <type>3</type>
            <showtype>0</showtype>
            <mediatagname></mediatagname>
            <messageext></messageext>
            <messageaction></messageaction>
            <content></content>
            <contentattr>0</contentattr>
            <url></url>
            <lowurl></lowurl>
            <dataurl>
                http://ws.stream.qqmusic.qq.com/C100003i9hMt1bgui0.m4a?vkey=6867EF99F3684&amp;guid=ffffffffc104ea2964a111cf3ff3edaf&amp;fromtag=46
            </dataurl>
            <lowdataurl>
                http://ws.stream.qqmusic.qq.com/C100003i9hMt1bgui0.m4a?vkey=6867EF99F3684&amp;guid=ffffffffc104ea2964a111cf3ff3edaf&amp;fromtag=46
            </lowdataurl>
            <appattach>
                <totallen>0</totallen>
                <attachid></attachid>
                <emoticonmd5></emoticonmd5>
                <fileext></fileext>
            </appattach>
            <extinfo></extinfo>
            <sourceusername></sourceusername>
            <sourcedisplayname></sourcedisplayname>
            <commenturl></commenturl>
            <thumburl>
                http://imgcache.qq.com/music/photo/album/63/180_albumpic_143163_0.jpg
            </thumburl>
            <md5></md5>
        </appmsg>
        <fromusername></fromusername>
        <scene>0</scene>
        <appinfo>
            <version>29</version>
            <appname>摇一摇搜歌</appname>
        </appinfo>
        <commenturl></commenturl>
    </msg>
```

### 群消息

```
MsgType: 1
FromUserName: @@xxx
ToUserName: @xxx
Content:
    @xxx:<br/>xxx
```

itchat增加了三个群聊相关的键值：

* isAt: 判断是否@本号
* ActualNickName: 实际NickName
* Content: 实际Content

### 红包消息

```
MsgType: 49
AppMsgType: 2001
FromUserName: 发送方ID
ToUserName: 接收方ID
Content: 未知
```

### 系统消息

```
MsgType: 10000
FromUserName: 发送方ID
ToUserName: 自己ID
Content:
    "你已添加了 xxx ，现在可以开始聊天了。"
    "如果陌生人主动添加你为朋友，请谨慎核实对方身份。"
    "收到红包，请在手机上查看"
```
