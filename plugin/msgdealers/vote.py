#coding=utf8
import re, json, time, os
from plugin.Sqlite3Client import Sqlite3Client

VOTE_KEYWORD = u'投票'

def load_vote_list():
    with open(os.path.join('plugin', 'config', 'vote.json')) as f: voteList = json.loads(f.read())
    if not voteList: raise Exception
    for voteItem in voteList: # test json format
        if not (voteItem.has_key('name') and voteItem.has_key('candidates')): raise Exception
        if not (isinstance(voteItem['candidates'], list) and voteItem['candidates']): raise Exception
    return voteList

def get_status(storageClass, userName):
    r = storageClass.get_other(userName)
    return storageClass.get_dict_of_other(r)

def store_status(storageClass, userName, other):
    PYQuanPin = storageClass.find_PYQuanPin(userName)
    storageClass.update_user(PYQuanPin, Other = storageClass.get_str_of_other(other))

def vote(msg, storageClass, userName):
    if not VOTE_KEYWORD in msg: return False
    # key in sqlite3->other: vote
    # value in sqlite3->other: 0 for voted, 1 for not voted
    # values should be strings
    voteList = load_vote_list()
    if voteList is None: return False
    status = get_status(storageClass, userName)
    for voteItem in voteList:
        # load vote details
        if not voteItem['name'] in msg: continue
        if voteItem.has_key('maxvote'):
            maxVote = voteItem['maxvote']
        else:
            maxVote = 1
        # load user details
        if status.has_key('vote@' + voteItem['name']):
            currentVote = int(status['vote@' + voteItem['name']])
            if currentVote <= 0:
                return u'你已经在“%s”中完成了投票'%voteItem['name']
        else:
            currentVote = maxVote
        # check vote
        candidate = None
        for c in voteItem['candidates']:
            # bug will occur if one candidates's name contains another's
            if c in msg: candidate = c;break
        if candidate is None: return u'投票选项包括: ' + ', '.join(voteItem['candidates'])
        # update vote database
        with Sqlite3Client(storageClass.sqlDir) as s3c:
            s3c.execute('create table if not exists vote (name text, candidate text, PYQuanPin text, time text)')
            PYQuanPin = storageClass.find_PYQuanPin(userName)
            s3c.insert_data('vote', items = [voteItem['name'], candidate, PYQuanPin, int(time.time())])
        # update user status
        status['vote@' + voteItem['name']] = str(currentVote - 1)
        store_status(storageClass, userName, status)
        return u'已经成功投票给“%s”%s'%(candidate, '' if currentVote == 1 else u'，你还可以投%s票'%(currentVote - 1))
    return u'目前进行的投票有: ' + ', '.join([voteItem['name'] for voteItem in voteList])

if __name__ != '__main__':
    load_vote_list()
