import web
import sys
import os
import string
import MySQLdb

# now using
urls = (
		'/','Index'
		)
global allnum
allnum = {}
global buffer 
buffer = {}
global count
count = {}
global cache_period
global banya_period
global merge_period

global file
global values
#values = []
values = {}
if len(sys.argv) > 2:
	dbname = sys.argv[2]
#	print "here"+str(banya_period)
else:
	dbname = "new"

app = web.application(urls, globals())

class Index:

	def POST(self):
		
		global count
		global buffer 
		global allnum
		global file
		global values
		global cache_period
		global banya_period
		global merge_period
	
		i =  web.input() 

		name = (i.get('name',None)).encode("utf-8")
		data = (i.get('data',None)).encode("utf-8")

		lines = data.split('\t')
		print name 
		if name in buffer:
			pass
		else:
			
			buffer[name] = ""
			count[name] = 0
			allnum[name] = 0
			values[name] = []
			os.system('true >  %s.txt'%name)
			os.system('hdfs dfs -mkdir /data/kexi/%s'%name )
		#	os.system('impala-shell.sh -i master -d %s -q " drop table if exists %stmp; create table %stmp(time bigint,oid string,ip string, value string); drop table if exists %s; create table %s like %stmp stored as parquetfile;"' %(dbname,name,name,name,name,name))
			os.system('impala-shell.sh -i master -d %s -q "create table %stmp(time bigint,oid string,ip string, value string); create table %s like %stmp stored as parquetfile;"' %(dbname,name,name,name))

			conn = MySQLdb.connect(host='localhost',user='root',passwd='881230')
			curs = conn.cursor()
			conn.select_db('%s'%dbname)
			curs.execute("CREATE TABLE %s(time bigint, oid VARCHAR(100), ip VARCHAR(100), value VARCHAR(100));"%name)
		#	curs.execute("DROP TABLE IF EXISTS %s; CREATE TABLE %s(time bigint, oid VARCHAR(100), ip VARCHAR(100), value VARCHAR(100));"%(name,name))
			conn.commit()
			curs.close()
			conn.close()
			print "INIT OK!%s"%name

if __name__ == "__main__":
	#buffer = ""
	os.system('hdfs dfs -mkdir /data/kexi' )
	app.run()
