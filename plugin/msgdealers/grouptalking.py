import os, re, time
from plugin.Sqlite3Client import Sqlite3Client

SQL_DIR = os.path.join('storage', 'grouptalk')
SQL_NAME = 'grouptalk.db'

if not os.path.exists(SQL_DIR): os.mkdir(SQL_DIR)
with Sqlite3Client(os.path.join(SQL_DIR, SQL_NAME)) as s3c:
    s3c.execute('create table if not exists messages (groupname text, time integer, message text, username text, fromto text)')
    s3c.execute('create table if not exists memberlist (groupname text, username text, nickname text)')

class GroupRobot:
    def __init__(self):
        pass
    def clear_table(self):
        with Sqlite3Client(os.path.join(SQL_DIR, SQL_NAME)) as s3c:
            s3c.execute('delete from memberlist')
    def touch_user(self, groupName, userName):
        with Sqlite3Client(os.path.join(SQL_DIR, SQL_NAME)) as s3c:
            r = s3c.query('select count(*) from memberlist where groupname=? and username=?',
                [groupName, userName])[0][0]
            return True if r else False
    def update_group(self, client, groupName):
        memberList = client.get_batch_contract(groupName)
        memberDict = {member['UserName']: member for member in memberList}
        with Sqlite3Client(os.path.join(SQL_DIR, SQL_NAME)) as s3c:
            q = s3c.query('select * from memberlist where groupname=?', (groupName,))
            for member in q: del memberDict[member[1]]
            for userName, member in memberDict.items():
                s3c.insert_data('memberlist', (groupName, member['UserName'], member['NickName']))
    def store_msg(self, content, groupName, userName, fromto):
        with Sqlite3Client(os.path.join(SQL_DIR, SQL_NAME)) as s3c:
            s3c.insert_data('messages', [groupName, int(time.time()), content, userName, fromto])
    def change_msg_format(self, groupName, userName, msg):
        if msg[:5] in ['@fil@', '@img@']: return msg
        with Sqlite3Client(os.path.join(SQL_DIR, SQL_NAME)) as s3c:
            nickName = s3c.query('select * from memberlist where groupname=? and username=?',
                [groupName, userName])[0][2]
            # return ('%s:<br/>@%s\342\200\205%s'%(userName.encode('utf8'),
            #     nickName.encode('utf8'), msg.encode('utf8'))).decode('utf8')
            return ('@%s\342\200\205%s'%(nickName.encode('utf8'), msg.encode('utf8'))).decode('utf8')

def get_msg_from_raw(msg):
    regex = re.compile('(@[0-9a-z]*?):<br/>(.*)$')
    r = re.findall(regex, msg)
    if r:
        return r[0][0], r[0][1]
    else:
        return '', ''

gr = GroupRobot()
gr.clear_table()

def grouptalking(msg, s, client, get_reply, replyToAll = False):
    # here needs an emoji test
    groupName = msg['FromUserName']
    userName, msg['Content'] = get_msg_from_raw(msg['Content'])
    if not(client.storageClass.nickName in msg['Content'] or replyToAll): return
    msg['Content'] = msg['Content'].replace('@%s'%client.storageClass.nickName, '')
    reply = get_reply(msg, s, client, isGroupChat = True)
    if not gr.touch_user(groupName, userName): gr.update_group(client, groupName)
    gr.store_msg(msg['Content'], groupName, userName, 'from')
    gr.store_msg(reply, groupName, userName, 'to')
    return gr.change_msg_format(groupName, userName, reply)
