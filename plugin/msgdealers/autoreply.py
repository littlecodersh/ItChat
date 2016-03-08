#coding=utf8
import re, json, time, os
import traceback
from plugin.Sqlite3Client import Sqlite3Client

def compileRegex(tableName, regexList):
    try:
        with Sqlite3Client(os.path.join('plugin', 'config', 'autoreply.db')) as s3c:
            for qa in s3c.data_source('select * from %s'%tableName):
                regexList.append((re.compile(qa[0]), qa[1]))
    except:
        print 'Error occured when loading regex table %s'%tableName
        traceback.print_exc()

def getreply():
    regexAnsList = []
    tableNameList = ['default_reply']
    for tableName in tableNameList: compileRegex(tableName, regexAnsList)
    while 1:
        msg = (yield)
        r = False
        for regexAns in regexAnsList:
            if not re.search(regexAns[0], msg) is None: r = regexAns[1]; break
        yield r

getreplyiter = getreply()

def autoreply(msg):
    getreplyiter.next()
    return getreplyiter.send(msg)
