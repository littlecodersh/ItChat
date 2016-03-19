import os, sqlite3, time
import config
from plugin.Sqlite3Client import Sqlite3Client

class Storage:
    def __init__(self):
        self.userName = None
        self.nickName = None
        self.historyMsg = []
        self.memberList = {}
        self.msgList = []
        self.lastInputUserName = None
    def find_msg_list(self, userName, count):
        r = []
        for msg in self.historyMsg:
            if msg['UserName'] == userName:
                r.append(msg)
            if len(r) >= count: break
        return r
    def updateMemberList(memberList):
        for member in memberList: self.update_user(member)
    def store_msg(self, msg, fromto = 'from'):
        msg['fromto'] = fromto
        self.historyMsg.append(msg)
    def update_user(self, user):
        self.memberList[user['UserName']] = user
    def find_username(self, n):
        r = []
        for userName, member in memberList.items():
            if member['NickName'] == n: r.append(member['UserName'])
        return r
    def find_nickname(self, u):
        r = []
        for userName, member in memberList.items():
            if member['UserName'] == u: return member['NickName']
