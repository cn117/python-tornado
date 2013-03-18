from mako.template import Template
from mako.runtime import Context
import gl
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
value=""
for i in range(n):
	value=value+"%s"
file_object.write(t.render(host="dfas",user="dfas",passwd="dfas",db="dfas"),from_table=gl.from_table,to_table=gl.to_table,from_table_column=gl.from_sys,to_table_column=gl.to_sys,values=value)
file_object.close( )
