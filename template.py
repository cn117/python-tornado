import os, sys, string
import MySQLdb
try:
    conn=MySQLdb.connect(host="${host}",user="${user}",passwd="${passwd}",db="${db}")
except Exception, e:
    print e
    sys.exit()
  
cursor=conn.cursor()
sql="insert into ${from_table} (${from_table_column}) values(${values})"
n = cursor.execute("select ${to_table_column} from ${to_table}")
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
