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
allnum = 0
global buffer 
buffer = ""
global count
count = 0 
#global cache_period
global banya_period
global merge_period

global file
global values
values = []

if len(sys.argv) > 3:
#	cache_period = int(sys.argv[2])
	banya_period = int(sys.argv[2])
	merge_period = int(sys.argv[3])
#	print "here"+str(banya_period)
else:
#	cache_period =  5000
	banya_period = 4000000
	merge_period =16000000 

os.system('true >  yongqianhislong.txt')
app = web.application(urls, globals())

class Index:

	def POST(self):
		
		global count
		global buffer 
		global allnum
		global file
		global values
#		global cache_period
		global banya_period
		global merge_period
		#print banya_period	
	
		data = web.data()
		#print data
		i =  web.input() 

		snmp = (i.get('snmp',None)).encode("utf-8")
	#	snmp = i.get('snmp',None)
#		print snmp
	#	lines = list(snmp.encode("utf-8")).readlines()
		lines = snmp.split('\n')
#		print lines
		router = (lines[0].split())[1]
		port = (lines[1].split())[1]

		#if exits this key if not init it

		l_list = lines[6:]
#		print l_list
		for l in l_list:
			records = l.split()
			#print records 
			if records!=[]:
				i_list = ""
				#range~!
				#print int(records[1])
				if int(records[1])>=pow(2,63):
				#	print int(records[1])
					records[1]="-1"
				if int(records[2])>=pow(2,31):
				#	print int(records[2])
					records[2]="-1"
				if int(records[3])>=pow(2,63):
				#	print int(records[3])
					records[3]="-1"
				if int(records[4])>=pow(2,31):
				#	print int(records[4])
					records[4]="-1"

				i_list +=  router +","+port + ","

				for i in range(0,4):
					i_list = i_list + records[i] + ","
				i_list = i_list + records[4] + "\n"

			#	values.append((router,port,records[0],records[1],records[2],records[3],records[4]))
				values = [router,port,records[0],records[1],records[2],records[3],records[4]]
				count += 1
				allnum += 1
				buffer = i_list

			#	print allnum

			#		print "cache_period OK"
				file = open('yongqianhislong.txt','a')
				file.write(buffer)
				file.close()
				buffer = ""

				#connect mysql
				conn = MySQLdb.connect(host='localhost',user='root',passwd='881230')
				curs = conn.cursor()
				conn.select_db('snmp')
				curs.execute("insert into yongqianhislong values(%s,%s,%s,%s,%s,%s,%s)",values)
				conn.commit()
				curs.close()
				conn.close()
				values = []

				if count >= banya_period:
				#	print "buffer" + buffer
					os.system('hdfs dfs -put yongqianhislong.txt /data/yongqianhislong')
					os.system('true >  yongqianhislong.txt')
					os.system('impala-shell.sh -i master -d snmp -q "load data inpath \'/data/yongqianhislong/yongqianhislong.txt\' into table yongqianhislong; "')
					count = count%banya_period

				if allnum >= merge_period:
					os.system('impala-shell.sh -i master -d snmp -q "insert into table yongqianhislongpar select * from yongqianhislong; drop table  yongqianhislong; create table yongqianhislong like yongqianhislongpar stored as textfile; "')
					allnum = 0;


if __name__ == "__main__":
	#buffer = ""
	app.run()
