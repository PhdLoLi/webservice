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
if len(sys.argv) > 4:
	cache_period = int(sys.argv[2])
	banya_period = int(sys.argv[3])
	merge_period = int(sys.argv[4])
else:
	cache_period =   5
	banya_period =   400
	merge_period = 7320

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
	#	print name 
	#	print data
		if name in buffer:
			pass
		else:
			
			buffer[name] = ""
			count[name] = 0
			allnum[name] = 0
			values[name] = []
			os.system('true >  %s.txt'%name)

		for record in lines:

			if record !=[]:
				#range~!
				records = record.split('|')
#				values.append((name,records[0],records[1],records[2]))
				if records!=['']:
					values[name].append(records)
					count[name] += 1
					allnum[name] += 1
					buffer[name] += record + '\n'

					print name+ str( allnum[name])

					if  (count[name]%cache_period)==0:
				#	print "just OK buffer" + buffer
			#		print "cache_period OK"
						file = open('%s.txt'%name,'a')
						file.write(buffer[name])
			#		print name;
			#		print buffer;
						file.close()
						buffer[name] = ""
			#		print "writeOK!"

					#connect mysql
						conn = MySQLdb.connect(host='localhost',user='root',passwd='881230')
						curs = conn.cursor()
						conn.select_db('snmp')
					#	print buffer[name]
				#		print name+"\nEEEEEEEEEEEEEEEEEEEEEEEEEEEE\n"
					
					#	print values[name]
				#		print records
						curs.executemany("insert into %s"%name+" values(%s,%s,%s,%s)",values[name])
	#					curs.execute("insert into %s"%name+" values(%s,%s,%s,%s)",records)
						conn.commit()
						curs.close()
						conn.close()
						values[name] = []
	
					if count[name] >= banya_period:
					#	print "buffer" + buffer
						os.system('hdfs dfs -put %s.txt /data/kexi/%s' %(name,name) )
						os.system('true > %s.txt'%name)
						os.system('impala-shell.sh -i master -d snmp -q "load data inpath \'/data/kexi/%s/%s.txt\' into table %s; "' %(name,name,name))
						count[name] = banya_period%cache_period 

					if allnum[name] >= merge_period:
						os.system('impala-shell.sh -i master -d snmp -q "insert into table %spar select * from %s; drop table  %s; create table %s like %spar stored as textfile; "'%(name,name,name,name,name))
						allnum[name] = 0;

if __name__ == "__main__":
	#buffer = ""
	app.run()
