# ItChat [![Gitter](https://badges.gitter.im/littlecodersh/ItChat.svg)](https://gitter.im/littlecodersh/ItChat?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge) ![python](https://img.shields.io/badge/python-2.7-ff69b4.svg)

ItChat是一个个人微信号的机器人，他实现了一个机器人需要实现的绝大部分功能。自动加好友、认人、发送图片、发送文件、简单的外部接口都可以轻松的完成。ItChat各模块与插件有着明确的模块化，易于扩展功能编写自己的插件。ItChat配置及其方便，甚至不需要图形界面就可以完成安装。

顺带的，如果把ItChat.py文件中的ROBOT改为False，该程序也可以当命令行的微信聊天软件使用。

##Have a try

我将我的微信号挂上了这个小机器人，百闻不如一见，有兴趣可以尝试一下。

![QRCode](http://7xrip4.com1.z0.glb.clouddn.com/ItChat%2FQRCode2.jpg?imageView/2/w/400/)

##Screenshot

###WeChat robot

![Demo](http://7xrip4.com1.z0.glb.clouddn.com/ItChat%2FDemo2.png?imageView/2/w/300/)

你可以在[wiki](https://github.com/littlecodersh/ItChat/wiki/Screenshots)看到更多的功能截图

###Command Line wechat

![cmd_wechat_chat](http://7xrip4.com1.z0.glb.clouddn.com/ItChat%2FScreenshots%2F%E5%91%BD%E4%BB%A4%E8%A1%8C%E8%81%8A%E5%A4%A9%E7%AA%97%E5%8F%A3.jpg)

命令行微信的输入操作经过特殊的处理，显示输出的同时**不会影响**正在进行的输入，而且**三平台**支持。

![change_to_cmd_wechat](http://7xrip4.com1.z0.glb.clouddn.com/ItChat%2FScreenshots%2F%E5%88%87%E6%8D%A2%E5%88%B0%E5%91%BD%E4%BB%A4%E8%A1%8C%E5%BE%AE%E4%BF%A1.jpg)

通过修改`ItChat.py`中第七行的True为False，可以登入命令行微信。

###Login Page

![login_page](http://7xrip4.com1.z0.glb.clouddn.com/ItChat%2FScreenshots%2F%E7%99%BB%E5%BD%95%E7%95%8C%E9%9D%A2%E6%88%AA%E5%9B%BE.jpg?imageView/2/w/300/)

和登陆网页端微信一样，扫码即可登录。

##Installation

可以通过本命令安装依赖库：

`pip install requests Image`

将本项目clone到本地安装依赖库后即可直接运行：

`python ItChat.py`

本项目基于python 2.7.11开发，使用python 3可能发生异常。

##Plugins

本项目默认开启投票插件与自定义回复插件

若需要开启其他插件，可以参照[wiki](https://github.com/littlecodersh/ItChat/wiki/Plugin)，或者运行`python PluginTest.py`一键检测插件

若需要支持中文文件传输，需要将plugin/config/fields.py文件放入requests包的packages/urllib3下，否则上传的文件将无法下载

##Comments

如果有什么问题或者建议都可以在这个[Issue](https://github.com/littlecodersh/ItChat/issues/1)和我讨论

或者也可以在gitter上交流：[![Gitter](https://badges.gitter.im/littlecodersh/ItChat.svg)](https://gitter.im/littlecodersh/ItChat?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge)
