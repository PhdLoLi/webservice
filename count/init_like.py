import sys
import os
import string
import MySQLdb

class useDBHDFS:
	name = ''
	likename =''
	def __init__(self,name,likename):
		self.name = name
		self.likename = likename

	def create(self):
		conn = MySQLdb.connect(host='localhost',user='root',passwd='881230')
		curs = conn.cursor()
		conn.select_db('snmp')
		curs.execute("create table %s like %s;"%(self.name,self.likename))
		conn.commit()
		curs.close()
		conn.close()
		os.system('impala-shell.sh -i master -d snmp -q "create table %s like %s; create table %spar like %spar; "'%(self.name,self.likename,self.name,self.likename))
		os.system('hdfs dfs -mkdir /data/%s'%self.name)
	def drop(self):
		conn = MySQLdb.connect(host='localhost',user='root',passwd='881230')
		curs = conn.cursor()
		conn.select_db('snmp')
		curs.execute("drop table %s;"%self.name)
		conn.commit()
		curs.close()
		conn.close()
		os.system('impala-shell.sh -i master -d snmp -q "drop table %s; drop table %spar"'%(self.name,self.name))
		os.system('hdfs dfs -rm -r /data/%s'%self.name)

'''	
if __name__ == "__main__":
	t = initDBHDFS('lala','yongqian')
#	t = initDBHDFS()
	t.DB()
'''
