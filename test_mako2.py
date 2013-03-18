import os, sys, string
import MySQLdb
try:
    conn=MySQLdb.connect(host="11",user="11",passwd="11",db="11")
except Exception, e:
    print e
    sys.exit()
  
cursor=conn.cursor()
sql="insert into booklist (booklistname,booklisttext) values(%s,%s)"
n = cursor.execute("select name,booktext from books")
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