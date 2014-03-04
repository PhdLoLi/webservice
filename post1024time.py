import web
import sys
import os
import string
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
if len(sys.argv) > 2:
	length = int(sys.argv[2])
	print "here"+str(length)
else:
	length = 3000

app = web.application(urls, globals())
class Index:

	def POST(self):
		
		global count
		global buffer 
		global length
		global allnum

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
				i_list = "("
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

				i_list +=  "\'"+router +"\'"+","+port + ","

				for i in range(0,4):
					i_list = i_list + records[i] + ","
				i_list = i_list + records[4] + ")"
				#print i_list
				count = count + 1
				allnum += 1
				print allnum
				if (allnum%10000) == 0:
					print "allnum:" + str(allnum)
				#print "count now" + str(count)
				if count < length:
					buffer = buffer + i_list + ","
				#	print "buffer" + buffer
				elif count == length:
					buffer = buffer + i_list
				#	print length
				#	print "just OK buffer" + buffer
					os.system('impala-shell.sh -i master -d snmp -q "insert into tmp  values %s"'%buffer)
					count = 0 
					buffer = ""
				else:
					buffer = "," + buffer + i_list
					print "That's is too strange! > length countnow: "  
					print count
				#	print buffer
					os.system('impala-shell.sh -i master -d snmp -q "insert into tmp  values %s"'%buffer)
					#os.system('impala-shell.sh -i master -d snmp -q "insert into testdat partition(router=\'%s\', port=%s) values %s"'%(router,port,buffer))
					count = 0 
					buffer = ""



if __name__ == "__main__":
	#buffer = ""
	app.run()
