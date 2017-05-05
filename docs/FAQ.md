## 稳定性

Q: itchat稳定性如何？

A: 测试用机器人能稳定在线多个月。如果你在测试过程中发现无法稳定登陆，请检查**登陆手机**及主机是否稳定连接网络。如果你需要最稳定的消息环境，建议使用[itchatmp][itchatmp]项目，两者使用方法类似。

## 中文文件名文件上传

Q: 为什么中文的文件没有办法上传？

A: 这是由于`requests`的编码问题导致的。若需要支持中文文件传输，将[fields.py][fields.py-2](py3版本见[这里][fields.py-3])文件放入requests包的packages/urllib3下即可

## 命令行显示二维码

Q: 为什么我在设定了`itchat.auto_login()`的`enableCmdQR`为`True`后还是没有办法在命令行显示二维码？

A: 这是由于没有安装可选的包`pillow`，可以使用右边的命令安装：`pip install pillow`

## 如何通过itchat实现控制器

Q: 如何通过这个包将自己的微信号变为控制器？

A: 有两种方式：发送、接受自己UserName的消息；发送接收文件传输助手（filehelper）的消息

## 无法给自己发送消息

Q: 为什么我发送信息的时候部分信息没有成功发出来？

A: 有些账号是天生无法给自己的账号发送信息的，建议使用`filehelper`代替。

[fields.py-2]: https://gist.github.com/littlecodersh/9a0c5466f442d67d910f877744011705
[fields.py-3]: https://gist.github.com/littlecodersh/e93532d5e7ddf0ec56c336499165c4dc
[itchatmp]: https://github.com/littlecodersh/itchatmp
