# ItChat [![Gitter](https://badges.gitter.im/littlecodersh/ItChat.svg)](https://gitter.im/littlecodersh/ItChat?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge)

ItChat是一个个人微信号的机器人，他实现了一个机器人需要实现的绝大部分功能。自动加好友、认人、发送图片、发送文件、简单的外部接口都可以轻松的完成。ItChat各模块与插件有着明确的模块化，易于扩展功能编写自己的插件。ItChat配置及其方便，甚至不需要图形界面就可以完成安装。

顺带的，如果把ItChat.py文件中的ROBOT改为False，该程序也可以当命令行的微信聊天软件使用。

##Have a try

我将我的微信号挂上了这个小机器人，百闻不如一见，有兴趣可以尝试一下。

![QRCode](http://7xrip4.com1.z0.glb.clouddn.com/ItChat%2FQRCode.jpg?imageView/2/w/400/)

##Screenshot

![Demo](http://7xrip4.com1.z0.glb.clouddn.com/ItChat%2FDemo.jpg?imageView/2/w/300/)

你可以在[wiki](https://github.com/littlecodersh/ItChat/wiki/Screenshots)看到更多的功能截图

##Installation

可以通过本命令安装依赖库：

`pip install requests Image`

将本项目clone到本地安装依赖库后即可直接运行：

`python ItChat.py`

本项目基于python 2.7.11开发，使用python 3可能发生异常。

##Plugins

本项目默认开启投票插件与自定义回复插件

若需要开启其他插件，可以参照[wiki](https://github.com/littlecodersh/ItChat/wiki/Plugin)，或者运行`python PluginTest.py`一键检测插件

若需要支持中文文件传输，需要将plugin/config/fields.py文件放入requests包的packages\urllib3下，否则上传的文件将无法下载

##Comments

如果有什么问题或者建议都可以在这个[Issue](https://github.com/littlecodersh/ItChat/issues/1)和我讨论

或者也可以在gitter上交流：[![Gitter](https://badges.gitter.im/littlecodersh/ItChat.svg)](https://gitter.im/littlecodersh/ItChat?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge)
