#SNMPSTRAPS DATA 8087 post just one & no fixed time 
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
	length = 40000

os.system('true >  datakexi.txt')
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
	
	#	data = web.data()
		#print data
		i =  web.input() 

		name = (i.get('name',None)).encode("utf-8")
		data = (i.get('data',None)).encode("utf-8")

		if data!=[]:
			count = count + 1
			allnum += 1

		#	values.append(data)
			buffer = data + "\n"
			file = open('datakexi.txt','w+')
			file.write(buffer)
			file.close()
			#connect mysql
			conn = MySQLdb.connect(host='localhost',user='root',passwd='881230')
			curs = conn.cursor()
			conn.select_db('snmp')
			curs.execute("insert into %s values(%s,%s,)",name,data)
		#	curs.executemany("insert into tmp values(%s,%s,%s,%s,%s,%s,%s)",values)
			print("Mysql OK!")
			conn.commit()
			curs.close()
			conn.close()
	#		values = []

		for records in lines:
	#		records = l.split()
			print records 
			if records!=[]:
				
				print allnum
				if (allnum%10000) == 0:
					print "allnum:" + str(allnum)
				if count < length:
					buffer  += records + "\n"
					if  (count%2)==0:
				#	print length
				#	print "just OK buffer" + buffer
						print "2OK"
				elif count == length:
					buffer  += records + "\n"
					file = open('datakexi.txt','w+')
					file.write(buffer)
					file.close()
					os.system('hdfs dfs -put datakexi.txt /data/snmp/buffer')
					os.system('true >  datakexi.txt')
					os.system('impala-shell.sh -i master -d snmp -q "load data inpath \'/data/snmp/buffer/datakexi.txt\' into table buffer; "')
					count = 0 
					buffer = ""
				else:
					print "That's is too strange! > length countnow: "  
					print count
				#	print buffer
			#		os.system('impala-shell.sh -i master -d snmp -q "insert into tmp  values %s"'%buffer)
					#os.system('impala-shell.sh -i master -d snmp -q "insert into testdat partition(router=\'%s\', port=%s) values %s"'%(router,port,buffer))
					count =  1
					buffer = records + "\n"
				if allnum == 7320000:
					os.system('impala-shell.sh -i master -d snmp -q "insert into table par select * from buffer; drop table  buffer; create table buffer like par stored as textfile; "')
					allnum = 0;


if __name__ == "__main__":
	#buffer = ""
	app.run()
