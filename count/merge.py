import os
import sys
import commands
import string
#me = os.path.getsize("yongqian.txt")
#print "haha"+str(me)
if len(sys.argv) >1:
	merge_period = int(sys.argv[1])
else:
	merge_period = 200000000
dbname = 'new'
output = os.popen('hdfs dfs -ls /user/hive/warehouse/%s.db'%dbname)
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
		if table!="" and name[-3:]="tmp":
		#	print table
			#print name[-3:]
			name = name[:-3]
			resulttmp = os.popen('hdfs dfs -count %s'%table)
			resulttmp2 = resulttmp.read()
			resulttmp3 = resulttmp2.split()
			quantity = int(resulttmp3[2])
			print name
			print quantity
			if quantity >= merge_period:
				print "HERE"
				os.system('impala-shell.sh -i master -d %s -q "create table IF NOT EXISTS  %s like %stmp stored as parquetfile; insert into table %s select * from %stmp; drop table %stmp; create table %stmp like %s stored as textfile; "'%(dbname,name,name,name,name,name,name,name))
