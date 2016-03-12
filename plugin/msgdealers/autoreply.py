#coding=utf8
import re, json, time, os
import traceback
from plugin.Sqlite3Client import Sqlite3Client

SQLITE_DIR = os.path.join('plugin', 'config')
FILE_DIR = os.path.join('storage', 'upload')

def compileRegex(tableName, regexList):
    regex = ''
    try:
        with Sqlite3Client(os.path.join(SQLITE_DIR, 'autoreply.db')) as s3c:
            for qa in s3c.data_source('select * from %s'%tableName):
                regex = qa[0]
                regexList.append((re.compile(qa[0]), qa[1]))
    except:
        raise Exception('Error occured when loading regex table %s: %s is not a correct regex'%(
            tableName, regex))

def detectFiles(tableName):
    if not os.path.exists(FILE_DIR): os.makedirs(FILE_DIR)
    fileName = ''
    try:
        with Sqlite3Client(os.path.join(SQLITE_DIR, 'autoreply.db')) as s3c:
            for qa in s3c.data_source('select * from %s'%tableName):
                if qa[1][:5] == '@fil@':
                    fileName = qa[1][5:]
                    with open(os.path.join(FILE_DIR, fileName)): pass
    except:
        raise Exception('Error occured when loading "%s" in table %s, it should be in storage/upload'%(
            fileName, tableName))

def getreply():
    regexAnsList = []
    tableNameList = ['default_reply']
    for tableName in tableNameList:
        detectFiles(tableName)
        compileRegex(tableName, regexAnsList)
    while 1:
        msg = (yield)
        r = False
        for regexAns in regexAnsList:
            if not re.search(regexAns[0], msg) is None: r = regexAns[1]; break
        yield r

getreplyiter = getreply()
getreplyiter.next()

def autoreply(msg):
    r = getreplyiter.send(msg)
    if r and r[:5] == '@fil@': r = '@fil@%s'%(os.path.join(FILE_DIR, r[5:]))
    getreplyiter.next()
    return r
