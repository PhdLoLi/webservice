#Compute now and mysql table
import MySQLdb
import time
import sys
import os
import string

#conn = MySQLdb.connect(host='localhost',user='root',passwd='881230')
conn = MySQLdb.connect(host='localhost',user='root',passwd='881230',db='snmp')
#curs = conn.cursor(cursorclass = MySQLdb.cursors.DictCursor)
curs = conn.cursor()
#conn.select_db('information_schema')
#tables = curs.execute('select table_schema,table_name from tables where table_schema = "snmp"')
#conn.select_db('snmp')
number = curs.execute('show tables')
tables = curs.fetchall()
period = "1hour"
buffer = []
for i in range(number):
	name = tables[i][0]
	curs.execute('select count(*) from %s'%name)
	newnum = curs.fetchall()
	olddata = curs.execute('select * from countnow where name="%s"'%name)
	curs.execute('SELECT DATA_LENGTH FROM information_schema.TABLES WHERE TABLE_SCHEMA="snmp" AND TABLE_NAME="%s"'%name)
	newstorage = curs.fetchall()

	if olddata >= 1:
		curs.execute('SELECT allnum from countnow where name ="%s"'%name)
		oldnum = curs.fetchall()
		curs.execute('SELECT allstorage from countnow where name ="%s"'%name)
		oldstorage = curs.fetchall() 
		curs.execute('SELECT timediff(now(),time) from countnow where name="%s"'%name)
		periodtmp = curs.fetchall()
		period = periodtmp[0][0]
		curs.execute('update countnow set allnum=%d,allstorage=%d,avgnum=%d,avgstorage=%d,period="%s" , time=now() where name="%s" '%(newnum[0][0],newstorage[0][0],newnum[0][0]-oldnum[0][0],newstorage[0][0]-oldstorage[0][0],period,name));
	else:
		curs.execute('insert into countnow values("%s",%d,%d,0,0,"%s",now())'%(name,newnum[0][0],newstorage[0][0],period));
	lines = name+":"+'\t'+str(newnum[0][0])+'\t'+str(newstorage[0][0])+'\t'+str(newnum[0][0]-oldnum[0][0])+'\t'+str(newstorage[0][0]-oldstorage[0][0])
	print lines
	buffer.append(lines+'\n')

#print buffer
#	print tables[i][0]
#print tables
conn.commit()
curs.close()
conn.close()
now = time.strftime('%Y/%m/%d-%H:%M:%S',time.localtime(time.time()))
print now
print period
print period.minute

file = open('now.txt','w')
file.write('time:\t'+now+'\tperiod: '+str(period)+'\n')
file.writelines(buffer)
file.close

