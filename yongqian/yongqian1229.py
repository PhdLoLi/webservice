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

conn = MySQLdb.connect(host='localhost',user='root',passwd='881230')
curs = conn.cursor()
conn.select_db('snmp')
curs.execute("select count(*) from yongqian")
numtmp = curs.fetchall()
allnum = numtmp[0][0]
conn.commit()
curs.close()
conn.close()

global buffer 
global count
#count = 0 
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
#	cache_period =     500
	banya_period =   40000
	merge_period = 7320000

#os.system('true >  yongqian.txt')
count = 0
thefile = open('yongqian.txt','rb')
while 1:
	buffer = thefile.read(65536)
	if not buffer:break
	count += buffer.count('\n')

buffer = ""

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
				file = open('yongqian.txt','a')
				file.write(buffer)
				file.close()
				buffer = ""

				#connect mysql
				conn = MySQLdb.connect(host='localhost',user='root',passwd='881230')
				curs = conn.cursor()
				conn.select_db('snmp')
				curs.execute("insert into yongqian values(%s,%s,%s,%s,%s,%s,%s)",values)
				conn.commit()
				curs.close()
				conn.close()
				values = []

				if os.path.getsize("yongqian.txt") >= 2000000: #>=2M 
	#			if count >= banya_period:
				#	print "buffer" + buffer
					os.system('hdfs dfs -put yongqian.txt /data/yongqian')
					os.system('true >  yongqian.txt')
					os.system('impala-shell.sh -i master -d snmp -q "load data inpath \'/data/yongqian/yongqian.txt\' into table yongqian; "')
		#			count = count%banya_period
					count = 0

				if allnum >= merge_period:
					os.system('impala-shell.sh -i master -d snmp -q "insert into table yongqianpar select * from yongqian; drop table  yongqian; create table yongqian like yongqianpar stored as textfile; "')
					allnum = 0;


if __name__ == "__main__":
	#buffer = ""
	app.run()
