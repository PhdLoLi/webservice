#SNMPSTRAPS DATA
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
#		data = web.data()
		#print data
		i =  web.input() 

#		snmp = i.data
#		table = i.name
		name = (i.get('name',None)).encode("utf-8")
		data = (i.get('data',None)).encode("utf-8")
#		print snmp
	#	lines = data.split('\t')
#		print data
		print name
		print data
	#	print lines	
		return "Yes!"

if __name__ == "__main__":
	#buffer = ""
	app.run()
