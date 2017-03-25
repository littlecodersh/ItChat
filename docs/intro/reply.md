# 回复

itchat提供五种回复方法，建议直接使用`send`方法。

## send方法

* 方法：
```python
send(msg='Text Message', toUserName=None)
```
* 所需值：
    * msg：消息内容
    * '@fil@文件地址'将会被识别为传送文件，'@img@图片地址'将会被识别为传送图片，'@vid@视频地址'将会被识别为小视频
    * toUserName：发送对象，如果留空将会发送给自己
* 返回值：发送成功->True, 失败->False
* 程序示例：使用的素材可以在[这里][attachment]下载

```python
#coding=utf8
import itchat

itchat.auto_login()
itchat.send('Hello world!')
# 请确保该程序目录下存在：gz.gif以及xlsx.xlsx
itchat.send('@img@%s' % 'gz.gif')
itchat.send('@fil@%s' % 'xlsx.xlsx')
itchat.send('@vid@%s' % 'demo.mp4')
```

## send_msg方法

* 方法：
```python
send_msg(msg='Text Message', toUserName=None)
```
* 所需值：
    * msg：消息内容
    * toUserName：发送对象，如果留空将会发送给自己
* 返回值：发送成功->True, 失败->False
* 程序示例：

```python
import itchat

itchat.auto_login()
itchat.send_msg('Hello world')
```

## send_file方法

* 方法：
```python
send_file(fileDir, toUserName=None)
```
* 所需值：
    * fileDir：文件路径（不存在该文件时将打印无此文件的提醒）
    * toUserName：发送对象，如果留空将会发送给自己
* 返回值：发送成功->True, 失败->False
* 程序示例：使用的素材可以在[这里][attachment]（提取码：eaee）下载

```python
#coding=utf8
import itchat

itchat.auto_login()
# 请确保该程序目录下存在：xlsx.xlsx
itchat.send_file('xlsx.xlsx')
```

## send_img方法

* 方法：
```python
send_img(fileDir, toUserName=None)
```
* 所需值：
    * fileDir：文件路径（不存在该文件时将打印无此文件的提醒）
    * toUserName：发送对象，如果留空将会发送给自己
* 返回值：发送成功->True, 失败->False
* 程序示例：使用的素材可以在[这里][attachment]（提取码：eaee）下载

```python
#coding=utf8
import itchat

itchat.auto_login()
# 请确保该程序目录下存在：gz.gif
itchat.send_img('gz.gif')
```

## send_video方法

* 方法：
```python
send_video(fileDir, toUserName=None)
```
* 所需值：
    * fileDir：文件路径（不存在该文件时将打印无此文件的提醒）
    * toUserName：发送对象，如果留空将会发送给自己
* 返回值：发送成功->True, 失败->False
* 需要保证发送的视频为一个实质的mp4文件

```python
#coding=utf8
import itchat

itchat.auto_login()
# 请确保该程序目录下存在：demo.mp4
itchat.send_file('demo.mp4')
```

[attachment]: http://7xrip4.com1.z0.glb.clouddn.com/ItChat/%E4%B8%8A%E4%BC%A0%E7%B4%A0%E6%9D%90.zip
