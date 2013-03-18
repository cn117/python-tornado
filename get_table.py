'''
Created on 2013-3-14

@author: niuhao
'''
import sys
import time,MySQLdb

try:
    conn=MySQLdb.connect(host="localhost",user="root",passwd="123",db="test")
except Exception, e:
    print e
    sys.exit()

cursor=conn.cursor()

n = cursor.execute("SHOW TABLES")
for table in cursor.fetchall():
    print table[0]

cursor.execute('DESCRIBE books')

for columns in cursor.fetchall():
    print columns[0] 
    







