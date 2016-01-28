class Storage:
    def __init__(self):
        self.userName = None
        self.memberList = []
        self.msgStorage = {}
        self.lastInputUserName = None
    def find_msg_list(self, userName):
        if not self.msgStorage.has_key(userName): self.msgStorage[userName] = []
        return self.msgStorage[userName]
    def add_msg(self, l,  msg):
        l.append(msg)
        self.lastInputUserName = msg['FromUserName']
    def find_user(self, n):
        for i in self.memberList:
            if i['NickName'] == n: return i['UserName']
    def find_nickname(self, u):
        for i in self.memberList:
            if i['UserName'] == u: return i['NickName']
    def search_nickname(self, n):
        r = []
        for i in self.memberList:
            if n in i['NickName']: r.append(i['NickName'])
        return r

