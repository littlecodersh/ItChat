#!/usr/bin/env python3
import sys
import itchat

def lc():
    itchat.start_rpc_server('localhost', 9000, block=True)

def ec():
    itchat.logout()
    sys.exit(1)


if __name__ == '__main__':
    itchat.login(enableCmdQR=True, loginCallback=lc, exitCallback=ec)
