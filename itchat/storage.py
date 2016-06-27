import os, sqlite3, time
import config
from plugin.Sqlite3Client import Sqlite3Client

class Storage:
    def __init__(self):
        self.userName = None
        self.nickName = None
        self.msgList = []
        self.groupDict = {}
        self.lastInputUserName = None
    def load_sql_storage(self):
        self.sqlDir = os.path.join(config.ACC_DIR, '%s.db'%self.nickName)
        with Sqlite3Client(self.sqlDir) as s3c:
            s3c.execute('create table if not exists message (time integer, message text, nickname text, fromto text)')
            s3c.execute('create table if not exists memberList (PYQuanPin text, NickName text, UserName text, Other text)')
    def find_msg_list(self, userName, count):
        with Sqlite3Client(self.sqlDir) as s3c:
            r = s3c.query('select * from message where nickname=? order by time desc limit ?',
                (self.find_nickname(userName), count))
        return r
    def store_msg(self, userName, msg, fromto):
        with Sqlite3Client(self.sqlDir) as s3c:
            s3c.insert_data('message', 
                [int(time.time()), msg, self.find_nickname(userName), fromto])
        if fromto == 'from': self.lastInputUserName = userName
    def update_user(self, PYQuanPin, **kwargs):
        with Sqlite3Client(self.sqlDir) as s3c:
            dataInStorage = s3c.query('select count(*) from memberList where PYQuanPin = ?', (PYQuanPin,))[0][0]
            if dataInStorage == 0:
                dataDict = {'NickName': '', 'UserName': '', 'Other': ''}
            else:
                dataTuple = s3c.query('select * from memberList where PYQuanPin = ?', (PYQuanPin,))[0]
                dataDict = {'NickName': dataTuple[1], 'UserName': dataTuple[2], 'Other': dataTuple[3]}
                s3c.execute('delete from memberList where PYQuanPin = ?', (PYQuanPin,))
            for key, value in kwargs.items(): dataDict[key] = value
            try:
                s3c.insert_data('memberList', items = [PYQuanPin, dataDict['NickName'], dataDict['UserName'], dataDict['Other']])
            except:
                return dataDict
        return True
    def find_PYQuanPin(self, userName):
        with Sqlite3Client(self.sqlDir) as s3c:
            members = s3c.query('select * from memberList where UserName = ?', (userName,))
            for member in members: return member[0]
    def find_user(self, n):
        with Sqlite3Client(self.sqlDir) as s3c:
            members = s3c.query('select * from memberList where NickName = ?', (n,))
            for member in members: return member[2]
    def find_nickname(self, u):
        with Sqlite3Client(self.sqlDir) as s3c:
            members = s3c.query('select * from memberList where UserName = ?', (u,))
            for member in members: return member[1]
    def search_nickname(self, n):
        r = []
        with Sqlite3Client(self.sqlDir) as s3c:
            members = s3c.query('select * from memberList where NickName like ?', ('%' + n + '%',))
            for member in members: r.append(member[1])
        return r
    def get_other(self, userName):
        with Sqlite3Client(self.sqlDir) as s3c:
            members = s3c.query('select * from memberList where UserName = ?', (userName,))
            for member in members: return member[3]
    def get_dict_of_other(self, s):
        d = {}
        for item in s.split(';'):
            if len(item.split(',')) == 2: d[item.split(',')[0]] = item.split(',')[1]
        return d
    def get_str_of_other(self, d):
        return ';'.join(['%s,%s'%(key, value) for key, value in d.items()])
