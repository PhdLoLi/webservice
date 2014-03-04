import web
import os
import string

urls = (
		'/','Index'
		)
global buffer 
buffer = ""
global count
count = 0
app = web.application(urls, globals())

class Index:

	def POST(self):
		
		global count
		global buffer 
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

		l_list = lines[6:]
#		print l_list
		for l in l_list:
			records = l.split()
			#print records 
			if records!=[]:
				i_list = "("
				for i in range(0,4):
					i_list = i_list + records[i] + ","
				i_list = i_list + records[4] + ")"
				#print i_list
				count = count + 1
				if count!=30:
					buffer = buffer + i_list + ","
				else:
					buffer = buffer + i_list
					print "30"
					print buffer
	#				os.system('impala-shell.sh -i master -d snmp -q "insert into dat partition(router=\'%s\', port=%s) values %s"'%(router,port,buffer))
					count = 0 
					buffer = ""


	#	i_list = "("+i.get('time', None)+","+i.get('Octs_in', None)+","+i.get('Pkts_in', None)+","+i.get('Octs_out', None) + "," + i.get('Pkts_out', None) + ")"
	#	os.system('impala-shell.sh -i master -d snmp -q "insert into dat partition(router=\'202.112.36.20\', port=113) values %s"'%i_list)
	#	if count!=10:
	#		buffer = buffer + i_list + ","
	#	else:
	#		buffer = buffer + i_list
	#		print i_list;
	#		print buffer
	#		os.system('impala-shell.sh -i master -d snmp -q "insert into dat partition(router=\'202.112.36.20\', port=23) values %s"'%buffer)
	#		buffer = ""
	#		count = 0
	#print form.d.name

if __name__ == "__main__":
	#buffer = ""
	app.run()
