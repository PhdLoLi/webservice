import os
import sys

if len(sys.argv) > 1:
	name = sys.argv[1]
else:
	print "Please input the name!"
	exit(-1)
os.system('hdfs dfs -put %s.txt /data/%s'%(name,name))
os.system('true >  %s.txt'%name)
os.system('impala-shell.sh -i master -d snmp -q "load data inpath \'/data/%s/%s.txt\' into table %s; "'%(name,name,name))
os.system('impala-shell.sh -i master -d snmp -q "insert into table %spar select * from %s; drop table  %s; create table %s like %spar stored;insert into table %s select * from %spar; "'%(name,name,name,name,name,name,name))
