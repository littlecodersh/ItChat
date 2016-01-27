class Storage:
    def __init__(self):
        self.userName = None
        self.memberList = []
        self.msgList = {}
    def find_user(self, n):
        for i in self.memberList:
            if i['NickName'] == n: return i['UserName']
    def find_nickname(self, u):
        for i in self.memberList:
            if i['UserName'] == u: return i['NickName']
