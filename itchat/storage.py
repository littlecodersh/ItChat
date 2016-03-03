import os, sqlite3, time
import config
from plugin.Sqlite3Client import Sqlite3Client

import traceback

class Storage:
    def __init__(self):
        self.userName = None
        self.nickName = None
        self.msgList = []
        self.lastInputUserName = None
    def load_sql_storage(self):
        self.sqlDir = os.path.join(config.ACC_DIR, '%s.db'%self.nickName)
        with Sqlite3Client(self.sqlDir) as s3c:
            s3c.execute('create table if not exists message (time integer, message text, nickname text, fromto text)')
            s3c.execute('create table if not exists memberList (alias text, content text)')
    def find_msg_list(self, userName, count):
        with Sqlite3Client(self.sqlDir) as s3c:
            r = s3c.query('select * from message where nickname=\'%s\' order by time desc limit %s'
                %(self.find_nickname(userName), count))
        return r
    def store_msg(self, userName, msg, fromto):
        with Sqlite3Client(self.sqlDir) as s3c:
            s3c.insert_data('message', 
                [int(time.time()), msg, self.find_nickname(userName), fromto])
        if fromto == 'from': self.lastInputUserName = userName
    def update_user(self, alias, newDict = None, **kwargs):
        with Sqlite3Client(self.sqlDir) as s3c:
            dataInStorage = s3c.query('select count(*) from memberList where alias = "%s"'%alias)[0][0]
            if newDict is None: newDict = {}
            for key, value in kwargs.items(): newDict[key] = value
            if dataInStorage == 0:
                try:
                    s3c.insert_data('memberList', items = [alias, repr(newDict)])
                except:
                    pass
                    # print str(newDict)
                    # traceback.print_exc()
                    # raw_input()
            else:
                oldDict = eval(s3c.query('select * from memberList where alias = "%s"'%alias)[0][1])
                for key, value in newDict.items(): oldDict[key] = value
                try:
                    s3c.execute('update memberList set content = "%s" where alias = "%s"'%(
                        repr(oldDict), alias))
                except:
                    pass
                    # print str(oldDict)
                    # traceback.print_exc()
                    # raw_input()
    def find_user(self, n):
        with Sqlite3Client(self.sqlDir) as s3c:
            members = s3c.data_source('select * from memberList')
            for member in members:
                member = eval(member[1])
                if member['RemarkName'] == n: return i['UserName']
            members = s3c.data_source('select * from memberList')
            for member in members:
                member = eval(member[1])
                if member['NickName'] == n: return member['UserName']
    def find_nickname(self, u):
        with Sqlite3Client(self.sqlDir) as s3c:
            members = s3c.data_source('select * from memberList')
            for member in members:
                member = eval(member[1])
                if member['UserName'] == u: return member['RemarkName'] if member['RemarkName'] else member['NickName']
    def find_nickname1(self, u):
        with Sqlite3Client(self.sqlDir) as s3c:
            members = s3c.data_source('select * from memberList')
            for member in members:
                print member
                member = eval(member[1])
                if member['UserName'] == u: return member['RemarkName'] if member['RemarkName'] else member['NickName']
    def search_nickname(self, n):
        r = []
        with Sqlite3Client(self.sqlDir) as s3c:
            members = s3c.data_source('select * from memberList')
            for member in members:
                member = eval(member[1])
                if n in member['RemarkName']: r.append(member['RemarkName'])
            members = s3c.data_source('select * from memberList')
            for member in members:
                member = eval(member[1])
                if n in member['NickName']: r.append(member['NickName'])
        return r
