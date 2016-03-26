import os, time
import config

class Storage:
    def __init__(self):
        self.userName = None
        self.nickName = None
        self.memberList = []
        self.msgList = []
        self.lastInputUserName = None
    def find_msg_list(self, userName, count):
        r = []
        for msg in self.historyMsg:
            if msg['UserName'] == userName:
                r.append(msg)
            if len(r) >= count: break
        return r
    def find_username(self, n):
        r = []
        for member in self.memberList:
            if member['NickName'] == n: r.append(member['UserName'])
        return r
    def find_nickname(self, u):
        r = []
        for  member in self.memberList:
            if member['UserName'] == u: return member['NickName']
