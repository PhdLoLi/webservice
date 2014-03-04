import web
import sys
import os
import string
import MySQLdb

# now using
urls = (
		'/','Index'
		)

global buffer 

global file
global values
global dbname
dbname = 'new'
values = []
'''
if len(sys.argv) > 3:
	banya_period = int(sys.argv[2])
	merge_period = int(sys.argv[3])
#	print "here"+str(banya_period)
else:
#	cache_period =     500
	banya_period =   40000
	merge_period = 7320000
'''
#os.system('true >  yongqian.txt')

buffer = ""

app = web.application(urls, globals())

class Index:

	def POST(self):
		
		global buffer 
		global file
		global values
		global dbname
	
		i =  web.input() 

		name = (i.get('name',None)).encode("utf-8")
		data = (i.get('data',None)).encode("utf-8")

		lines = data.split('\t')

		for record in lines:

			if record!=[]:
				records = record.split('|')
				
				if records!=['']:
					
					buffer = record + '\n'
					file = open('%s.txt'%name,'a')
					file.write(buffer)
					file.close()
					buffer = ""
						
				#connect mysql
					conn = MySQLdb.connect(host='localhost',user='root',passwd='881230')
					curs = conn.cursor()
					conn.select_db(dbname)
					curs.execute("insert into %s"%name+" values(%s,%s,%s,%s)",records)
					conn.commit()
					curs.close()
					conn.close()

					if os.path.getsize("%s.txt"%name) >= 2000000: #>=2M 
					#	print "buffer" + buffer

						os.system('hdfs dfs -put %s.txt /data/kexi/%s' %(name,name) )
						os.system('true > %s.txt'%name)
						os.system('impala-shell.sh -i master -d %s -q "load data inpath \'/data/kexi/%s/%s.txt\' into table %stmp; "' %(dbname,name,name,name))


if __name__ == "__main__":
	#buffer = ""
	app.run()
