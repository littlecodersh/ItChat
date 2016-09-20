import os, time, copy

class Storage:
    def __init__(self):
        self.userName          = None
        self.nickName          = None
        self.memberList        = []
        self.mpList            = []
        self.chatroomList      = []
        self.msgList           = []
        self.lastInputUserName = None
    def dumps(self):
        return {
            'userName'          : self.userName,
            'nickName'          : self.nickName,
            'memberList'        : self.memberList,
            'mpList'            : self.mpList,
            'chatroomList'      : self.chatroomList,
            'lastInputUserName' : self.lastInputUserName, }
    def loads(self, j):
        self.userName          = j.get('userName', None)
        self.nickName          = j.get('nickName', None)
        del self.memberList[:]
        for i in j.get('memberList', []): self.memberList.append(i)
        del self.mpList[:]
        for i in j.get('mpList', []): self.mpList.append(i)
        del self.chatroomList[:]
        for i in j.get('chatroomList', []): self.chatroomList.append(i)
        self.lastInputUserName = j.get('lastInputUserName', None)
    def search_friends(self, name=None, userName=None, remarkName=None, nickName=None,
            wechatAccount=None):
        if (name or userName or remarkName or nickName or wechatAccount) is None:
            return copy.deepcopy(self.memberList[0]) # my own account
        elif userName: # return the only userName match
            for m in self.memberList:
                if m['UserName'] == userName: return copy.deepcopy(m)
        else:
            matchDict = {
                'RemarkName' : remarkName,
                'NickName'   : nickName,
                'Alias'      : wechatAccount, }
            for k in ('RemarkName', 'NickName', 'Alias'):
                if matchDict[k] is None: del matchDict[k]
            if name: # select based on name
                contract = []
                for m in self.memberList:
                    if any([m.get(k) == name for k in ('RemarkName', 'NickName', 'Alias')]):
                        contract.append(m)
            else:
                contract = self.memberList[:]
            if matchDict: # select again based on matchDict
                friendList = []
                for m in contract:
                    if all([m.get(k) == v for k, v in matchDict.items()]):
                        friendList.append(m)
                return copy.deepcopy(friendList)
            else:
                return copy.deepcopy(contract)
    def search_chatrooms(self, name=None, userName=None):
        if userName is not None:
            for m in self.chatroomList:
                if m['UserName'] == userName: return copy.deepcopy(m)
        elif name is not None:
            matchList = []
            for m in self.chatroomList:
                if name in m['NickName']: matchList.append(copy.deepcopy(m))
            return matchList
    def search_mps(self, name=None, userName=None):
        if userName is not None:
            for m in self.mpList:
                if m['UserName'] == userName: return copy.deepcopy(m)
        elif name is not None:
            matchList = []
            for m in self.mpList:
                if name in m['NickName']: matchList.append(copy.deepcopy(m))
            return matchList
