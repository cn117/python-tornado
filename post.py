'''
Created on 2013-3-14

@author: niuhao
'''
import os
import tornado.ioloop
import tornado.web
import sys
import gl
import time,MySQLdb
import string
#import mako
from mako.template import Template
from mako.runtime import Context
from StringIO import StringIO


class MainHandler(tornado.web.RequestHandler):
    def get(self):
        #self.render("test.html")        
        self.render("test.html",valus="456257")



class http(tornado.web.RequestHandler):
	def post(self):
        #self.set_header("Content-Type", "text/plain")
        
		gl.connect_info.append(self.get_argument("host"))
		gl.connect_info.append(self.get_argument("user"))
		gl.connect_info.append(self.get_argument("passwd"))
		gl.connect_info.append(self.get_argument("db"))        
		#self.render("test-1.html",connect_items=gl.connect_info)
		
		try:
			conn=MySQLdb.connect(host=gl.connect_info[0],user=gl.connect_info[1],passwd=gl.connect_info[2],db=gl.connect_info[3])
			#conn=MySQLdb.connect(host="localhost",user="root",passwd="123",db="test")
		except Exception, e:
			print e
			#self.redirect(self.get_argument('error', '/'))
			self.render("error.html",error="DB conncetion error!~~")
			gl.connect_info=[]

		cursor=conn.cursor()

		n = cursor.execute("SHOW TABLES")
		for table in cursor.fetchall():
			print table[0]
			gl.table_info.append(table[0])
		cursor.close()
		conn.close()       
		self.render("test-1.html",connect_items=gl.connect_info,table_items=gl.table_info)

class next1(tornado.web.RequestHandler):
	def post(self):
		print "##################################"
		#print connect_info[0]
		print "##################################"
		try:
			conn=MySQLdb.connect(host=gl.connect_info[0],user=gl.connect_info[1],passwd=gl.connect_info[2],db=gl.connect_info[3])
			#conn=MySQLdb.connect(host="localhost",user="root",passwd="123",db="test")
		except Exception, e:
			print e
			#self.redirect(self.get_argument('error', '/'))
			self.render("error.html",error="DB conncetion error!~~")
			gl.connect_info=[]
		cursor=conn.cursor()
		gl.from_table=self.get_argument("from_table")
		gl.to_table=self.get_argument("to_table")
		sql='DESCRIBE'+' '+gl.from_table		
		cursor.execute(sql)
		for columns in cursor.fetchall():
    		#print columns[0]
			gl.from_table_column.append(columns[0])
		cursor.execute('DESCRIBE '+gl.to_table)
		for columns in cursor.fetchall():
    		#print columns[0]
			gl.to_table_column.append(columns[0]) 
		cursor.close()
		conn.close()
		self.render("test-2.html",connect_items=gl.connect_info,table_items=gl.table_info,from_table=gl.from_table,to_table=gl.to_table,from_table_items=gl.from_table_column,to_table_items=gl.to_table_column)

class next2(tornado.web.RequestHandler):
	def post(self):
		gl.from_sys=self.get_argument("from_table_column")
		gl.to_sys=self.get_argument("to_table_column")
		self.render("test-3.html",connect_items=gl.connect_info,table_items=gl.table_info,from_table=gl.from_table,to_table=gl.to_table,from_table_items=gl.from_table_column,to_table_items=gl.to_table_column,from_table_sys=gl.from_sys,to_table_sys=gl.to_sys)

class finish(tornado.web.RequestHandler):
	def post(self):
		print "##################################"
		#print connect_info[0]
		print "##################################"
        #self.set_header("Content-Type", "text/plain")
		self.set_header("Content-Type", "text/plain")
		print os.getcwd()
		path=os.getcwd()+'/template.py';
		#t = Template(filename=path,module_directory=path_template)
		print "##############@@@@@##############"
		t=Template(filename=path)
		print "##############@@@@@###############"
		file_name='test_makoXX.py'
		file_object = open(file_name, 'w')
		n= string.count(gl.from_sys,",")
		print n
		print "@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@"
		value="%s"
		for i in range(n):
			value=value+",%s"
		file_object.write(t.render(host=gl.connect_info[0],user=gl.connect_info[1],passwd=gl.connect_info[2],db=gl.connect_info[3],from_table=gl.from_table,to_table=gl.to_table,from_table_column=gl.from_sys,to_table_column=gl.to_sys,values=value))
		file_object.close( )
		#file_object_read=open(file_name,'r')
		self.write("You template is \n " +os.getcwd()+"/"+file_name )
		#self.render("test-finish.html",path=os.getcwd()+"/"+file_name,file_Context="dddd")
		
		#self.write("You template is /n " +path+"/"+file_name )
		#self.write(file_object.read())
application = tornado.web.Application([
    (r"/", MainHandler),(r"/next",http),(r"/next/next",next1),(r"/next/next/next",next2),(r"/finish",finish)
])

if __name__ == "__main__":
    application.listen(8888)
    tornado.ioloop.IOLoop.instance().start()
