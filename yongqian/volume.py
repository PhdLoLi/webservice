import os
import sys
import commands
import string
#me = os.path.getsize("yongqian.txt")
#print "haha"+str(me)
if len(sys.argv) >1:
	merge_period = sys.argv[1]
else:
	merge_period = 200000000
output = os.popen('hdfs dfs -ls /user/hive/warehouse/snmp.db')
#line = lines.split()
#print "HERE"

lines = output.read()
#wakaka = commands.getstatusoutput('hdfs dfs -ls /user/hive/warehouse/snmp.db')
#print wakaka
linesplit = lines.split("\n")
for l in linesplit:
	if l!="":
		tmp = l.split()
		table = tmp[-1]
		tmp2 = table.split('/')
		name = tmp2[-1]
		if table!="" and table!="items" and name[-3:]!="par" and name[-3:] != "nyi":
		#	print table
			#print name[-3:]
			resulttmp = os.popen('hdfs dfs -count %s'%table)
			resulttmp2 = resulttmp.read()
			resulttmp3 = resulttmp2.split()
			quantity = int(resulttmp3[2])
			#print quantity
			if quantity >= merge_period:
				print "HERE"
				os.system('impala-shell.sh -i master -d snmp -q "insert into table %spar select * from %s; drop table %s; create table %s like %spar stored as textfile; "'%(name,name,name,name,name))
