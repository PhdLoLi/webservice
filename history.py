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
global length

global file
global values
values = []

if len(sys.argv) > 2:
	length = int(sys.argv[2])
	print "here"+str(length)
else:
	length = 732000

os.system('true >  data2.txt')
app = web.application(urls, globals())
class Index:

	def POST(self):
		
		global count
		global buffer 
		global length
		global allnum
		global file
		global values
		#print length	
	
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
				#print i_list
				
#				value = [router,int(port),int(records[0]),int(records[1]),int(records[2]),int(records[3]),int(records[4])]
#				value = [router,port,records[0],records[1],records[2],records[3],records[4]]
#				conn = MySQLdb.connect(host='localhost',user='root',passwd='881230')
#				curs = conn.cursor()
#				conn.select_db('snmp')
#				curs.execute("insert into tmp values(%s,%s,%s,%s,%s,%s,%s)",value)
#				echo("Mysql One OK!")
#				conn.commit()
#				curs.close()
#				conn.close()

				values.append((router,port,records[0],records[1],records[2],records[3],records[4]))
				#print values
				count = count + 1
				allnum += 1

			#	print allnum
				if (allnum%1000000) == 0:
					print "allnum:" + str(allnum)
				#print "count now" + str(count)
				if count < length:
				#	print "buffer" + buffer
					buffer  += i_list
					if  (count%4000)==0:
				#	print length
				#	print "just OK buffer" + buffer
					#	print "4000OK"
						file = open('data2.txt','w+')
						file.write(buffer)
						file.close()
						#connect mysql
						conn = MySQLdb.connect(host='localhost',user='root',passwd='881230')
						curs = conn.cursor()
						conn.select_db('snmp')
						curs.executemany("insert into history values(%s,%s,%s,%s,%s,%s,%s)",values)
				#		print("Mysql OK!")
						conn.commit()
						curs.close()
						conn.close()
						values = []
				elif count == length:
					buffer  += i_list
					file = open('data2.txt','w+')
					file.write(buffer)
					file.close()
					os.system('hdfs dfs -put data2.txt /data/snmp/buffer')
					os.system('true >  data2.txt')
					os.system('impala-shell.sh -i master -d snmp -q "load data inpath \'/data/snmp/buffer/data2.txt\' into table history; "')
					count = 0 
					buffer = ""
				else:
					print "That's is too strange! > length countnow: "  
					print count
				#	print buffer
			#		os.system('impala-shell.sh -i master -d snmp -q "insert into tmp  values %s"'%buffer)
					#os.system('impala-shell.sh -i master -d snmp -q "insert into testdat partition(router=\'%s\', port=%s) values %s"'%(router,port,buffer))
					count =  1
					buffer = i_list
				if allnum == 7320000:
					os.system('impala-shell.sh -i master -d snmp -q "insert into table hispar select * from history; drop table  history; create table history like hispar stored as textfile; "')
					allnum = 0;


if __name__ == "__main__":
	#buffer = ""
	app.run()
