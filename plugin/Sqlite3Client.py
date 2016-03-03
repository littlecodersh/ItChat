import sqlite3, re, thread
import json, sys

MAX_NUM = int(2e4)

class Sqlite3Client:
    def __enter__(self):
        return self
    def __init__(self, sqlDir):
        self.sqlDir = sqlDir
        self._connection = sqlite3.connect(sqlDir)
        self._cursor = self._connection.cursor()
        self._storedDataSource = None
    def execute(self, sql):
        self._cursor.execute(sql)
        self._connection.commit()
    def query(self, sql):
        self._cursor.execute(sql)
        return self._cursor.fetchall()
    def insert_data(self, tableName, items = []):
        items = ['"%s"'%item for item in items]
        self._cursor.execute('insert into %s values(%s)'%(tableName,', '.join(items)))
        self._connection.commit()
    def restruct_table(self, tableName, orderBy, restructedTableName = None):
        if restructedTableName is None: restructedTableName = 'restructed_' + tableName
        orderByString = ', '.join(['%s %s'%(key[0], key[1]) for key in orderBy])
        self.query(self.query('show create table %s'%tableName)[0][1].replace(tableName, restructedTableName, 1))
        sys.stdout.write('Restructuring the data storage...\r')
        totalNum = self.query('select count(*) from %s'%tableName)[0][0]
        s = self.data_source('select * from %s order by %s'%(tableName, orderByString))
        count = 0
        totalCount = 0
        process = -1
        for data in s:
            insertSql = 'insert into %s values (%s)'%(restructedTableName, ', '.join(['%s' for i in range(len(data))]))
            self._cursor.execute(insertSql, data)
            count += 1
            totalCount += 1
            if process < totalCount * 100 / totalNum:
                process = totalCount * 100 / totalNum
                sys.stdout.flush()
                sys.stdout.write('Restructuring the data storage: %s%s\r'%(process, '%'))
            if count >= MAX_NUM:
                count = 0
                self._connection.commit()
        self._connection.commit()
        print 'Restructuring Finished'
        return restructedTableName
    def simple_data_source(self, sql): # return a function to provide one data at a time
        c = self._connection.cursor()
        c.execute(sql)
        for item in c.fetchall(): yield item
    def parallel_get_source_of_data_source(self, sql, beginNumber = 0):
        regex = re.compile('from (\S+)')
        tableName = re.findall(regex, sql)[0]
        totalNum = self.query('select count(*) from %s'%tableName)[0][0]
        unitNumber = totalNum / MAX_NUM + 1
        self._storedDataSource = self.simple_data_source('%s limit %s, %s'%(sql, beginNumber, MAX_NUM))
        def get(i):
            self._storedDataSource = self.simple_data_source('%s limit %s, %s'%(sql, i * MAX_NUM, MAX_NUM))
        if unitNumber == beginNumber / MAX_NUM: yield self._storedDataSource
        for i in range(beginNumber / MAX_NUM + 1, unitNumber + 1):
            while self._storedDataSource is None: print 'Thread sucks'
            r = self._storedDataSource
            self._storedDataSource = None
            thread.start_new_thread(get, (i,))
            yield r
    def data_source(self, sql): # limit is now useless here
        regex = re.compile('(select .*? from .*?)(?: limit (\S+),.*)?$')
        r = re.findall(regex, sql)[0]
        sourceOfDataSource = self.parallel_get_source_of_data_source(r[0], int(r[1]) if r[1] else 0)
        for dataSource in sourceOfDataSource:
            for data in dataSource: yield data
    def __exit__(self, *args):
        if self._cursor: self._cursor.close()
        if self._connection: self._connection.close()

if __name__ == '__main__':
    with Sqlite3Client('wcStorage.db') as s3c:
        s3c.insert_data('message', items = [{'a':'a'},'a','a','a'])
        r = s3c.data_source('select * from message')
        for item in r:
            print type(eval(item[0]))
