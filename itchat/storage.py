import os, sqlite3, time
import config

class SqlStorage:
    def __enter__(self):
        return self
    def __init__(self, name):
        self.sqlStorage = sqlite3.connect(os.path.join(config.ACC_DIR, '%s.db'%name))
        self.sqlStorage.execute('create table if not exists message (time integer, message text, nickname text, fromto text)')
        self.cursor = self.sqlStorage.cursor()
        self.sqlStorage.commit()
    def __exit__(self, *args):
        if self.cursor: self.cursor.close()
        if self.sqlStorage: self.sqlStorage.close()

class Storage:
    def __init__(self):
        self.userName = None
        self.memberList = []
        self.msgList = []
        self.lastInputUserName = None
    def find_msg_list(self, userName, count):
        with SqlStorage(self.find_nickname(self.userName)) as sql:
            sql.cursor.execute('select * from message where nickname=\'%s\' order by time desc limit %s'%(self.find_nickname(userName), count))
            l = sql.cursor.fetchall()
        return l
    def store_msg(self, userName, msg, fromto):
        with SqlStorage(self.find_nickname(self.userName)) as sql:
            sql.sqlStorage.execute('insert into message values (?,?,?,?)',
                (int(time.time()), msg, self.find_nickname(userName), fromto))
            sql.sqlStorage.commit()
        if fromto == 'from': self.lastInputUserName = userName
    def find_user(self, n):
        for i in self.memberList:
            if i['RemarkName'] == n: return i['UserName']
        for i in self.memberList:
            if i['NickName'] == n: return i['UserName']
    def find_nickname(self, u):
        for i in self.memberList:
            if i['UserName'] == u: return i['RemarkName'] if i['RemarkName'] else i['NickName']
    def search_nickname(self, n):
        r = []
        for i in self.memberList:
            if n in i['RemarkName']: r.append(i['RemarkName'])
        for i in self.memberList:
            if n in i['NickName']: r.append(i['NickName'])
        return r
