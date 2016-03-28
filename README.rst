itchat
======

itchat is a open souce wechat api project for personal account.

It enables you to access your personal wechat account through command line.

So enjoy:)

**Try:**

You may have a try of the robot based on this project first:

|QRCodeOfRobot|

Here are some screenshots of this robot:

You may visit `Screenshots <https://github.com/littlecodersh/ItChat/wiki/Screenshots>`__ for more demos.

|Demo|

**Installation**

.. code:: bash

    pip install itchat

**Simple uses**

.. code:: python
    
    import itchat, time

    itchat.auto_login()

    @itchat.msg_dealer(['Text', 'Map', 'Card', 'Note', 'Sharing'])
    def text_reply(msg):
        itchat.send('%s: %s'%(msg['Type'], msg['Text']), msg['FromUserName'])

    @itchat.msg_dealer(['Picture', 'Recording', 'Attachment', 'Video'])
    def download_files(msg):
        fileDir = '%s%s'%(msg['Type'], int(time.time()))
        msg['Text'](fileDir)
        itchat.send('%s received'%msg['Type'], msg['FromUserName'])
        itchat.send('@%s@%s'%('img' if msg['Type'] == 'Picture' else 'fil', fileDir), msg['FromUserName'])

    @itchat.msg_dealer('Friends')
    def add_friend(msg):
        itchat.add_friend(**msg['Text'])
        itchat.get_contract()
        itchat.send_msg(msg['RecommendInfo']['UserName'], 'Nice to meet you!')

    @itchat.msg_dealer('Text', isGroupChat = True)
    def text_reply(msg):
        itchat.send(u'@%s\u2005I received: %s'%(msg['ActualNickName'], msg['Content']), msg['FromUserName'])

    itchat.run()

**FAQ**

Why I can't send files whose name is encoded in utf8?

That's because of the upload setting of requests, you can put `this file <https://github.com/littlecodersh/ItChat/blob/robot/plugin/config/fields.py>`__ 
into packages/urllib3 of requests package.

**Comments**

If you have any problems or suggestions, you can talk to me in this `issue <https://github.com/littlecodersh/ItChat/issues/1>`__

Or on `gitter <https://badges.gitter.im/littlecodersh/ItChat.svg>`__.

.. |QRCodeOfRobot| image:: http://7xrip4.com1.z0.glb.clouddn.com/ItChat%2FQRCode2.jpg?imageView/2/w/400/
.. |Demo| image:: http://7xrip4.com1.z0.glb.clouddn.com/ItChat%2FDemo2.png?imageView/2/w/300/
