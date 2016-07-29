itchat
======

|Python2| |Python3|

itchat is a open souce wechat api project for personal account.

It enables you to access your personal wechat account through command line.

Here is the `document <https://itchat.readthedocs.org/zh/latest/>`__.

So enjoy:)

**Try**

You may have a try of the robot based on this project first:

|QRCodeOfRobot|

Here is the `code <https://github.com/littlecodersh/ItChat/tree/robot>`__.

**Installation**

.. code:: bash

    pip install itchat

**Simple uses**

.. code:: python
    
    import itchat, time

    @itchat.msg_register(['Text', 'Map', 'Card', 'Note', 'Sharing'])
    def text_reply(msg):
        itchat.send('%s: %s'%(msg['Type'], msg['Text']), msg['FromUserName'])

    @itchat.msg_register(['Picture', 'Recording', 'Attachment', 'Video'])
    def download_files(msg):
        msg['Text'](msg['FileName'])
        itchat.send('@%s@%s'%('img' if msg['Type'] == 'Picture' else 'fil', msg['FileName']), msg['FromUserName'])
        return '%s received'%msg['Type']

    @itchat.msg_register('Friends')
    def add_friend(msg):
        itchat.add_friend(**msg['Text']) # new friend will be automatically added into storage, you don't need to reload the memberList
        itchat.send_msg('Nice to meet you!', msg['RecommendInfo']['UserName'])

    @itchat.msg_register('Text', isGroupChat = True)
    def text_reply(msg):
        if msg['isAt']:
            itchat.send(u'@%s\u2005I received: %s'%(msg['ActualNickName'], msg['Content']), msg['FromUserName'])

    itchat.auto_login()
    itchat.run()

**Advanced uses**

*Command line QR Code*

You can access the QR Code in command line through using this command:

.. code:: python

    itchat.auto_login(enableCmdQR = True)

Because of width of some character differs from systems, you may adjust the enableCmdQR to fix the problem.

.. code:: python

    # for some linux system, width of block character is one instead of two, so enableCmdQR should be 2
    itchat.auto_login(enableCmdQR = 2)

*Hot reload*

By using the following command, you may reload the program without re-scan QRCode in some time.

.. code:: python

    itchat.auto_login(hotReload = True)

*User search*

By using `get_friends`, you have four ways to search a user:

1. Get your own user information
2. Get user information through `UserName`
3. Get user information whose remark name or wechat account or nickname matches name key of the function
4. Get user information whose remark name, wechat account and nickname match what are given to the function

Way 3, 4 can be used together, the following is the demo program:

.. code:: python

    # get your own user information
    itchat.get_friends()
    # get user information of specific username
    itchat.get_friends(userName = '@abcdefg1234567')
    # get user information of function 3
    itchat.get_friends(name = 'littlecodersh')
    # get user information of function 4
    itchat.get_friends(wechatAccount = 'littlecodersh')
    # combination of way 3, 4
    itchat.get_friends(name = 'LittleCoder机器人', wechatAccount = 'littlecodersh')

*Download and send attachments*

The attachment download function of itchat is in Text key of msg

Name of the file (default name of picture) is in FileName key of msg

Download function accept one location value (include the file name) and store attachment accordingly.

.. code:: python

    @itchat.msg_register(['Picture', 'Recording', 'Attachment', 'Video'])
    def download_files(msg):
        msg['Text'](msg['FileName'])
        itchat.send('@%s@%s'%('img' if msg['Type'] == 'Picture' else 'fil', msg['FileName']), msg['FromUserName'])
        return '%s received'%msg['Type']

**FAQ**

Q: Why I can't send files whose name is encoded in utf8?

A: That's because of the upload setting of requests, you can put `this file <https://github.com/littlecodersh/ItChat/blob/robot/plugin/config/fields.py>`__ 
into packages/urllib3 of requests package.

Q: Why I still can't show QRCode with command line after I set enableCmdQr key to True in itchat.auto_login()?

A: That's because you need to install optional site-package pillow, try this script: pip install pillow

**Comments**

If you have any problems or suggestions, you can talk to me in this `issue <https://github.com/littlecodersh/ItChat/issues/1>`__

Or on `gitter <https://badges.gitter.im/littlecodersh/ItChat.svg>`__.

.. |QRCodeOfRobot| image:: http://7xrip4.com1.z0.glb.clouddn.com/ItChat%2FQRCode2.jpg?imageView/2/w/200/
.. |Python2| image:: https://img.shields.io/badge/python-2.7-ff69b4.svg
.. |Python3| image:: https://img.shields.io/badge/python-3.5-red.svg
