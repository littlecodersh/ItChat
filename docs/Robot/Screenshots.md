##微信投票

![wechat_vote](http://7xrip4.com1.z0.glb.clouddn.com/ItChat%2FScreenshots%2F%E5%BE%AE%E4%BF%A1%E4%B8%AD%E6%96%87%E6%8A%95%E7%A5%A8.png?imageView/2/w/300/)

投票的选项可以通过更改`plugin/config/vote.json`修改，但记得修改过以后使用`python PluginTest.py`测试是否能顺利启动哦！

![plugin/config/vote.json](http://7xrip4.com1.z0.glb.clouddn.com/ItChat%2FScreenshots%2F%E8%87%AA%E5%AE%9A%E4%B9%89%E6%8A%95%E7%A5%A8%E5%86%85%E5%AE%B9.png)

##自定义回复

![plain_text_autoreply](http://7xrip4.com1.z0.glb.clouddn.com/ItChat%2FScreenshots%2F%E5%BE%AE%E4%BF%A1%E8%87%AA%E5%AE%9A%E4%B9%89%E5%9B%9E%E5%A4%8D.png?imageView/2/w/300/)

文件也是自定义回复的一种哦！

![file_autoreply](http://7xrip4.com1.z0.glb.clouddn.com/ItChat%2FScreenshots%2F%E5%BE%AE%E4%BF%A1%E8%8E%B7%E5%8F%96%E6%96%87%E4%BB%B6%E5%9B%BE%E7%89%87.png?imageView/2/w/300/)

回复的规则可以通过更改`plugin/config/autoreply.db`修改，但记得修改或以后使用`python PluginTest.py`看看新规则是否能正常回复哦！

![plugin/config/autoreply.db](http://7xrip4.com1.z0.glb.clouddn.com/ItChat%2FScreenshots%2F%E6%95%B0%E6%8D%AE%E5%BA%93%E8%87%AA%E5%AE%9A%E4%B9%89%E5%9B%9E%E5%A4%8D.png)
##登录界面

![login_page](http://7xrip4.com1.z0.glb.clouddn.com/ItChat%2FScreenshots%2F%E7%99%BB%E5%BD%95%E7%95%8C%E9%9D%A2%E6%88%AA%E5%9B%BE.jpg?imageView/2/w/300/)

和登陆网页端微信一样，扫码即可登录。

##命令行微信

![cmd_wechat_chat](http://7xrip4.com1.z0.glb.clouddn.com/ItChat%2FScreenshots%2F%E5%91%BD%E4%BB%A4%E8%A1%8C%E8%81%8A%E5%A4%A9%E7%AA%97%E5%8F%A3.jpg)

命令行微信的输入操作经过特殊的处理，显示输出的同时不会影响正在进行的输入，而且三平台支持。

![change_to_cmd_wechat](http://7xrip4.com1.z0.glb.clouddn.com/ItChat%2FScreenshots%2F%E5%88%87%E6%8D%A2%E5%88%B0%E5%91%BD%E4%BB%A4%E8%A1%8C%E5%BE%AE%E4%BF%A1.jpg)

通过修改`ItChat.py`中第七行的True为False，可以登入命令行微信。

##其他

其他功能建议自己下载或者加测试号好友自己尝试啦！
