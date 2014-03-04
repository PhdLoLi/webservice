import web
import sys
import os
import string
# now using
urls = (
		'/','Index'
		)
global buffer 
buffer = {}
global count
count = {}
global length
if len(sys.argv) > 2:
	length = int(sys.argv[2])
	print "here"+str(length)
else:
	length = 120

app = web.application(urls, globals())
class Index:

	def POST(self):
		
		global count
		global buffer 
		global length

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

		key = router+":"+port
		print key
		#if exits this key if not init it
		if key in buffer:
			pass
		else:
			buffer[key] = ""
			count[key] = 0

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

				for i in range(0,4):
					i_list = i_list + records[i] + ","
				i_list = i_list + records[4] + ")"
				#print i_list
				count[key] = count[key] + 1
				print count[key]
				print "length:"+str(length)
				if count[key] < length:
					buffer[key] = buffer[key] + i_list + ","
					print buffer[key]
				elif count[key] == length:
					buffer[key] = buffer[key] + i_list
				#	print length
					print buffer[key]
					os.system('impala-shell.sh -i master -d snmp -q "insert into testdat partition(router=\'%s\', port=%s) values %s"'%(router,port,buffer[key]))
					count[key] = 0 
					buffer[key] = ""
				else:
					buffer[key] = "," + buffer[key] + i_list
					print "That's is too strange! > length countnow: "  
					print count[key]
					print buffer[key]
					os.system('impala-shell.sh -i master -d snmp -q "insert into testdat partition(router=\'%s\', port=%s) values %s"'%(router,port,buffer[key]))
					count[key] = 0 
					buffer[key] = ""



if __name__ == "__main__":
	#buffer = ""
	app.run()
