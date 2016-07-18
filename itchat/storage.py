import os, time
import config

class Storage:
    def __init__(self):
        self.userName          = None
        self.nickName          = None
        self.memberList        = []
        self.chatroomList      = []
        self.msgList           = []
        self.groupDict         = {}
        self.lastInputUserName = None
    def dumps(self):
        return {
            'userName'          : self.userName,
            'nickName'          : self.nickName,
            'memberList'        : self.memberList,
            'chatroomList'      : self.chatroomList,
            'groupDict'         : self.groupDict,
            'lastInputUserName' : self.lastInputUserName, }
    def loads(self, j):
        self.userName          = j.get('userName', None)
        self.nickName          = j.get('nickName', None)
        del self.memberList[:]
        for i in j.get('memberList', []): self.memberList.append(i)
        del self.chatroomList[:]
        for i in j.get('chatroomList', []): self.chatroomList.append(i)
        self.groupDict.clear()
        for k, v in j.get('groupDict', {}).iteritems(): self.groupDict[k] = v
        self.lastInputUserName = j.get('lastInputUserName', None)
    def find_username(self, n):
        r = []
        for member in self.memberList:
            if member['NickName'] == n: r.append(member['UserName'])
        return r
    def find_nickname(self, u):
        r = []
        for  member in self.memberList:
            if member['UserName'] == u: return member['NickName']
