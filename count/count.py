import MySQLdb
import time
import sys
import os
import string
import datetime

if len(sys.argv) > 1:
	period = sys.argv[1]
else:
	period = "1minute"
#conn = MySQLdb.connect(host='localhost',user='root',passwd='881230')
dbname ='new'
conn = MySQLdb.connect(host='localhost',user='root',passwd='881230',db=dbname)
#curs = conn.cursor(cursorclass = MySQLdb.cursors.DictCursor)
curs = conn.cursor()
#conn.select_db('information_schema')
#tables = curs.execute('select table_schema,table_name from tables where table_schema = "snmp"')
#conn.select_db('snmp')
number = curs.execute('show tables')
tables = curs.fetchall()
actual_timediff = datetime.timedelta(seconds=0)
buffer = []
for i in range(number):
	name = tables[i][0]
	curs.execute('select count(*) from %s'%name)
	newnum = curs.fetchall()
	olddata = curs.execute('select * from countavg where name="%s" and period="%s"'%(name,period))
	curs.execute('SELECT TABLE_ROWS*AVG_ROW_LENGTH  FROM information_schema.TABLES WHERE TABLE_SCHEMA="%s" AND TABLE_NAME="%s"'%(dbname,name))
	newstorage = curs.fetchall()

	if olddata >= 1:
		curs.execute('SELECT allnum from countavg where name ="%s" and period="%s"'%(name,period))
		oldnum = curs.fetchall()
		curs.execute('SELECT allstorage from countavg where name ="%s" and period="%s"'%(name,period))
		oldstorage = curs.fetchall() 
		curs.execute('SELECT timediff(now(),last_time) from countavg where name="%s" and period="%s"'%(name,period))
		periodtmp = curs.fetchall()
		actual_timediff = periodtmp[0][0]
		curs.execute('update countavg set allnum=%d,allstorage=%d,avgnum=%d,avgstorage=%d,last_time=now(),actual_timediff="%s" where name="%s" and period="%s" '%(newnum[0][0],newstorage[0][0],newnum[0][0]-oldnum[0][0],newstorage[0][0]-oldstorage[0][0],actual_timediff ,name,period));
	else:
		curs.execute('insert into countavg values("%s",%d,%d,0,0,"%s",now(),"%s")'%(name,newnum[0][0],newstorage[0][0],period,actual_timediff));
	print name+":"+str(newnum[0][0])
	buffer.append(name+":"+'\t'+str(newnum[0][0])+'\t'+str(newstorage[0][0])+'\t'+str(newnum[0][0]-oldnum[0][0])+'\t'+str(newstorage[0][0]-oldstorage[0][0])+'\n')
#	print tables[i][0]
#print tables
conn.commit()
curs.close()
conn.close()
now = time.strftime('%Y/%m/%d-%H:%M:%S',time.localtime(time.time()))
print now
file = open('speed.txt','w')
file.write('last_time:\t'+now+'\tperiod: '+period+'\n')
file.writelines(buffer)
file.close
