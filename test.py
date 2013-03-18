'''
Created on 2013-3-14

@author: niuhao
'''
import os
import tornado.ioloop
import tornado.web
from mako.template import Template
from mako.runtime import Context
from StringIO import StringIO


class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("test.html")

    def post(self):
        #self.set_header("Content-Type", "text/plain")
        print os.getcwd()
        path=os.getcwd()+'/template.py';
        path_template=os.getcwd()+'/mako_modules'
        #t = Template(filename=path,module_directory=path_template)
        t=Template(filename=path)
        #print t.render(host=self.get_argument("host"),user=self.get_argument("user"),passwd=self.get_argument("passwd"),db=self.get_argument("db"))
        file_name='test_mako2.py'
        file_object = open(file_name, 'w')
        file_object.write(t.render(host=self.get_argument("host"),user=self.get_argument("user"),passwd=self.get_argument("passwd"),db=self.get_argument("db")))
        file_object.close( )
        self.write("You wrote " + self.get_argument("host"))

application = tornado.web.Application([
    (r"/", MainHandler),
])


if __name__ == "__main__":
    application.listen(8888)
    tornado.ioloop.IOLoop.instance().start()
