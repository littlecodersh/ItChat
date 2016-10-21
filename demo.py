#!/usr/bin/env python
# coding:utf8
"""
Demo of itchat
"""

import itchat


@itchat.msg_register(itchat.content.TEXT)
def text_reply(msg):
    itchat.send(msg['Text'], msg['FromUserName'])


def main():
    itchat.auto_login()
    itchat.run()


if __name__ == '__main__':
    main()
