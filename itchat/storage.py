import os, time
import config

class Storage:
    def __init__(self):
        self.userName = None
        self.nickName = None
        self.memberList = []
        self.chatroomList = []
        self.msgList = []
        self.groupDict = {}
        self.lastInputUserName = None
    def find_username(self, n):
        r = []
        for member in self.memberList:
            if member['NickName'] == n: r.append(member['UserName'])
        return r
    def find_nickname(self, u):
        r = []
        for  member in self.memberList:
            if member['UserName'] == u: return member['NickName']
