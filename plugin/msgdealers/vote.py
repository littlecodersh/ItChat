import re
from plugin.Sqlite3Client import Sqlite3Client

def get_status(storageClass, userName):
    r = storageClass.get_other(userName)
    return storageClass.get_dict_of_other(r)

def store_status(storageClass, userName, other):
    PYQuanPin = storageClass.find_PYQuanPin(userName)
    storageClass.update_user(PYQuanPin, Other = storageClass.get_str_of_other(other))

def vote(storageClass, userName, msg):
    # key in sqlite3->other: vote
    # value in sqlite3->other: -1 for voted, 0 for waiting for vote, 1 for not voted
    regex = re.compile('.*vote.* num ([0-9]+)')
    r = re.findall(regex, msg)
    if not r: return False
    status = get_status(storageClass, userName)
    if not status.has_key('vote'): status['vote'] = '1'
    if status['vote'] == '-1': return 'You have voted'
    with Sqlite3Client(storageClass.sqlDir) as s3c:
        s3c.execute('create table if not exists vote (a text, b text, c text)')
        q = s3c.query('select * from vote')
        if not q:
            s3c.insert_data('vote', items = ['0','0','0'])
            q = s3c.query('select * from vote')
        if r[0] in ('1','2','3'):
            s3c.execute('delete from vote')
            index = int(r[0]) - 1
            insert_data = list(q[0])
            insert_data[index] = str(int(insert_data[index]) + 1)
            s3c.insert_data('vote', items = insert_data)
            status['vote'] = '-1'
            store_status(storageClass, userName, status)
            return 'Vote for %s successfully'%r[0]
        else:
            return 'There is no candidate %s'%r[0]
