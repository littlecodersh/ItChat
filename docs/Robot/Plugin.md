#已有插件介绍

该微信机器人提供了完备的接口，可以很容易的加入新的插件。

先就两个简单的插件做一个介绍，若想要了解具体如何编写新的插件，可以快速阅读这一节。

##vote

该插件实现了基于用户识别的投票功能，即使机器人下线也不会影响用户的投票数据。

###配置

* 配置投票选项：在plugin/config/vote.json中更改投票选项
* 若要更改文字说明，可以在plugin/msgdealers/vote.py中修改
* 投票记录在storage/account/用户名.db的表vote中

##autoreply

该插件实行了基于正则表达式匹配的自动回复。

###配置

* 配置自动回复的内容与匹配规则：在plugin/config/autoreply.db中增加或删除
* 以`@fil@`开头后面接具体路径（一般建议放在storage/upload/文件夹下）可以自动回复文件
* 以`@img@`开头后面接具体路径（一般建议放在storage/upload/文件夹下）可以自动回复图片
* 若以文件方式发送图片将不会以缩略图方式收到信息

#自定义插件配置

##编写插件

编写插件并不困难，具体的调用可以参照已有的两个插件。

需要注意，文件的相对路径以ItChat.py所在位置为起始。

###编写插件的流程
1. 编写插件、编写插件测试与样例
1. 更新itchat/robot.py、PluginTest.py、pluginlist.json中的插件与测试文件
1. 使用`python PluginTest.py`测试插件是否正常工作

第一步将在下面具体介绍。

其中第二步的配置是指：

在itchat/robot.py中以`(方法名，方法)`的元组加入插件序列（次序代表优先匹配）

![setting_itchat/robot.py](http://7xrip4.com1.z0.glb.clouddn.com/ItChat%2FPlugin%2Frobot.py%E4%B8%AD%E8%AE%BE%E7%BD%AE%E6%8F%92%E4%BB%B6.jpg?imageView/2/w/400/)

在PluginTest.py中加入编写好的测试方法：

![add_test_into_PluginTest.py](http://7xrip4.com1.z0.glb.clouddn.com/ItChat%2FPlugin%2F%E5%B0%86%E6%B5%8B%E8%AF%95%E5%91%BD%E4%BB%A4%E5%8A%A0%E5%85%A5PluginTest.jpg?imageView/2/w/400/)

若需要测试，将插件插入PluginTest.py的测试名单中：

![add_plugin_into_PluginTest.py_pluginlist](http://7xrip4.com1.z0.glb.clouddn.com/ItChat%2FPlugin%2F%E5%B0%86%E6%8F%92%E4%BB%B6%E5%8A%A0%E5%85%A5PluginTest.jpg?imageView/2/w/400)

在pluginlist.json中加入改插件名字：

![add_plugin_name_into_pluginlist.json](http://7xrip4.com1.z0.glb.clouddn.com/ItChat%2FPlugin%2Fpluginlist%E9%85%8D%E7%BD%AE.png?imageView/2/w/400/)

至此第二步配置就完成了。

##给出的接口

插件需要提供一个方法并通过这个方法返回值。

该方法将会获得三个输入，分别为文本内容、全局存储对象、发送人的UserName

这样就可以基于用户发送过来的消息作出反馈

通过全局存储对象，可以获得所有用户的信息与来往消息，下面以获取用户信息为例：

```python
# 全局存储对象存储为storageClass, 发送人UserName存储为userName
# 更多的方法可以在itchat/storage.py中获取

# 获取昵称、唯一标示符
nickName = storageClass.find_nickname(userName)
pyid = storageClass.find_PYQuanPin(userName)

# 获取用户个人数据
status = storageClass.get_dict_of_other(storageClass.get_other(userName))

# 存储用户个人数据
storageClass.update_user(pyid, Other = storageClass.get_str_of_other(status))
```

##返回类型
* 插件需要返回一个Unicode格式的文本或是False
* 若匹配该插件成功，那么回复用户要通过返回Unicode格式的文本完成
* 回复内容同样可以以`@fil@`等标示符开头，但请一定记得配置相关测试以免运行出现意外
* 若匹配插件失败，回复False即可

##插件放置位置
* 插件本身需要被放置于plugin/msgdealers/文件夹中
* 插件调用的文件内容原则上建议存储在plugin文件夹中

![place_for_configs](http://7xrip4.com1.z0.glb.clouddn.com/ItChat%2FPlugin%2F%E9%85%8D%E7%BD%AE%E5%AD%98%E6%94%BE%E5%A4%84.png?imageView/2/w/400)

##测试相关配置

如果涉及到活动用户信息的设置暂时没有编写完成，建议可以基于已有用户信息模拟测试。

测试中的异常情况通过`sys_print('WARN', msg)`输出信息，系统将会识别出测试出现了问题。

测试中的普通输出可以通过`sys_print`方法输出信息。

运行`python PluginTest.py`将会进入交互的测试，你可以测试返回内容是否如你所愿。

#结语

只是一个简单的介绍，若有错误或是任何建议，我会很高兴收到你的邮件！
