itchat
======

|Python2| |Python3|

itchat is an open source api for WeChat, a commonly-used Chinese social networking app.

Accessing your personal wechat account through itchat in python has never been easier.

A wechat robot can handle all the basic messages with only less than 30 lines of codes.

And it's similiar to itchatmp (api for wechat massive platform), learn once and get two tools.

Now Wechat is an important part of personal life, hopefully this repo can help you extend your personal wechat account's functionality and enbetter user's experience with wechat.

**Installation**

.. code:: bash

    pip install itchat

**Simple uses**

With itchat, if you want to send a message to filehelper, this is how:

.. code:: python

    import itchat

    itchat.auto_login()

    itchat.send('Hello, filehelper', toUserName='filehelper')

And you only need to write this to reply personal text messages.

.. code:: python
    
    import itchat

    @itchat.msg_register(itchat.content.TEXT)
    def text_reply(msg):
        return msg.text

    itchat.auto_login()
    itchat.run()

For more advanced uses you may continue on reading or browse the `document <https://itchat.readthedocs.org/zh/latest/>`__.

**Try**

You may have a try of the robot based on this project first:

|QRCodeOfRobot|

Here is the `code <https://gist.github.com/littlecodersh/ec8ddab12364323c97d4e36459174f0d>`__.

**Advanced uses**

*Special usage of message dictionary*

You may find out that all the users and messages of itchat are dictionaries by printing them out onto the screen.

But actually they are useful classes itchat created.

They have useful keys and useful interfaces, like:

.. code:: python
    
    @itchat.msg_register(TEXT)
    def _(msg):
        # equals to print(msg['FromUserName'])
        print(msg.fromUserName)

And like:

.. code:: python

    author = itchat.search_friends(nickName='LittleCoder')[0]
    author.send('greeting, littlecoder!')

*Message register of various types*

The following is a demo of how itchat is configured to fetch and reply daily information.

.. code:: python

    import itchat, time
    from itchat.content import *

    @itchat.msg_register([TEXT, MAP, CARD, NOTE, SHARING])
    def text_reply(msg):
        msg.user.send('%s: %s' % (msg.type, msg.text))

    @itchat.msg_register([PICTURE, RECORDING, ATTACHMENT, VIDEO])
    def download_files(msg):
        msg.download(msg.fileName)
        typeSymbol = {
            PICTURE: 'img',
            VIDEO: 'vid', }.get(msg.type, 'fil')
        return '@%s@%s' % (typeSymbol, msg.fileName)

    @itchat.msg_register(FRIENDS)
    def add_friend(msg):
        msg.user.verify()
        msg.user.send('Nice to meet you!')

    @itchat.msg_register(TEXT, isGroupChat=True)
    def text_reply(msg):
        if msg.isAt:
            msg.user.send(u'@%s\u2005I received: %s' % (
                msg.actualNickName, msg.text))

    itchat.auto_login(True)
    itchat.run(True)

*Command line QR Code*

You can access the QR Code in command line through using this command:

.. code:: python

    itchat.auto_login(enableCmdQR=True)

Because of width of some character differs from systems, you may adjust the enableCmdQR to fix the problem.

.. code:: python

    # for some linux system, width of block character is one instead of two, so enableCmdQR should be 2
    itchat.auto_login(enableCmdQR=2)

Default background color of command line is dark (black), if it's not, you may set enableCmdQR to be negative:

.. code:: python

    itchat.auto_login(enableCmdQR=-1)

*Hot reload*

By using the following command, you may reload the program without re-scan QRCode in some time.

.. code:: python

    itchat.auto_login(hotReload=True)

*User search*

By using `search_friends`, you have four ways to search a user:

1. Get your own user information
2. Get user information through `UserName`
3. Get user information whose remark name or wechat account or nickname matches name key of the function
4. Get user information whose remark name, wechat account and nickname match what are given to the function

Way 3, 4 can be used together, the following is the demo program:

.. code:: python

    # get your own user information
    itchat.search_friends()
    # get user information of specific username
    itchat.search_friends(userName='@abcdefg1234567')
    # get user information of function 3
    itchat.search_friends(name='littlecodersh')
    # get user information of function 4
    itchat.search_friends(wechatAccount='littlecodersh')
    # combination of way 3, 4
    itchat.search_friends(name='LittleCoder机器人', wechatAccount='littlecodersh')

There are detailed information about searching and getting of massive platforms and chatrooms in document.

*Download and send attachments*

The attachment download function of itchat is in Text key of msg

Name of the file (default name of picture) is in FileName key of msg

Download function accept one location value (include the file name) and store attachment accordingly.

.. code:: python

    @itchat.msg_register([PICTURE, RECORDING, ATTACHMENT, VIDEO])
    def download_files(msg):
        msg.download(msg.fileName)
        itchat.send('@%s@%s' % (
            'img' if msg['Type'] == 'Picture' else 'fil', msg['FileName']),
            msg['FromUserName'])
        return '%s received' % msg['Type']

If you don't want a local copy of the picture, you may pass nothing to the function to get a binary string.

.. code:: python

    @itchat.msg_register([PICTURE, RECORDING, ATTACHMENT, VIDEO])
    def download_files(msg):
        with open(msg.fileName, 'wb') as f:
            f.write(msg.download())

*Multi instance*

You may use the following commands to open multi instance.

.. code:: python

    import itchat

    newInstance = itchat.new_instance()
    newInstance.auto_login(hotReload=True, statusStorageDir='newInstance.pkl')

    @newInstance.msg_register(itchat.content.TEXT)
    def reply(msg):
        return msg['Text']

    newInstance.run()

*Set callback after login and logout*

Callback of login and logout are set through `loginCallback` and `exitCallback`.

.. code:: python

    import time

    import itchat

    def lc():
        print('finish login')
    def ec():
        print('exit')

    itchat.auto_login(loginCallback=lc, exitCallback=ec)
    time.sleep(3)
    itchat.logout()

If loginCallback is not set, qr picture will be deleted and cmd will be cleared.

If you exit through phone, exitCallback will also be called.

**FAQ**

Q: Why I can't send files whose name is encoded in utf8?

A: That's because of the upload setting of requests, you can put `this file <https://gist.github.com/littlecodersh/9a0c5466f442d67d910f877744011705>`__ (for py3 you need `this <https://gist.github.com/littlecodersh/e93532d5e7ddf0ec56c336499165c4dc>`__) into packages/urllib3 of requests package.

Q: How to use this package to use my wechat as an monitor?

A: There are two ways: communicate with your own account or with filehelper.

Q: Why sometimes I can't send messages?

A: Some account simply can't send messages to yourself, so use `filehelper` instead.

**Comments**

If you have any problems or suggestions, you can talk to me in this `issue <https://github.com/littlecodersh/ItChat/issues/1>`__

Or on `gitter <https://badges.gitter.im/littlecodersh/ItChat.svg>`__.

.. |QRCodeOfRobot| image:: http://7xrip4.com1.z0.glb.clouddn.com/ItChat%2FQRCode2.jpg?imageView/2/w/200/
.. |Python2| image:: https://img.shields.io/badge/python-2.7-ff69b4.svg
.. |Python3| image:: https://img.shields.io/badge/python-3.5-red.svg
