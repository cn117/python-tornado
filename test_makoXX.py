import os, sys, string
import MySQLdb
try:
    conn=MySQLdb.connect(host="localhost",user="root",passwd="123",db="test")
except Exception, e:
    print e
    sys.exit()
  
cursor=conn.cursor()
sql="insert into books (name,booktext) values(%s,%s)"
n = cursor.execute("select booklistname,booklisttext from booklist")
list=[]    
for row in cursor.fetchall():    
    #for r in row:
        list.append(row)
        
#print list[0][0]       
for param in list:
    try:
        cursor.execute(sql,param)
        #cursor.executemany(sql)
        conn.commit()
    except Exception, e:
        print e

cursor.close()
conn.close()
