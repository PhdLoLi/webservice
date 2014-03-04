import MySQLdb
import time
import sys
import os
import string
import datetime

if len(sys.argv) > 1:
	mysql_period = int(sys.argv[1])
else:
	mysql_period = 10000000

dbname = 'new'
conn = MySQLdb.connect(host='localhost',user='root',passwd='881230',db=dbname)
curs = conn.cursor()
number = curs.execute('show tables')
tables = curs.fetchall()

for i in range(number):
	name = tables[i][0]
	exits = curs.execute('select * from information_schema.COLUMNS where TABLE_SCHEMA="%s" AND TABLE_NAME="%s" AND COLUMN_NAME="time"'%(dbname,name))

	if exits >= 1:
		print name;
		curs.execute('SELECT count(*) from %s'%name)
		tmp_allnum = curs.fetchall()
		allnum = tmp_allnum[0][0]
		print allnum
		print mysql_period

		if allnum - mysql_period>=0 : 
			print "HERE!"
			curs.execute('SELECT MIN(time) from %s'%name)
			tmp_start_time = curs.fetchall()
			start_time = tmp_start_time[0][0]
			curs.execute('SELECT MAX(time) from %s'%name)
			tmp_end_time = curs.fetchall()
			end_time = tmp_end_time[0][0]
			mid_time = int((start_time+end_time)/2)
			timeArray = time.localtime(mid_time)
			mid_time_read = time.strftime("%Y-%m-%d %H:%M:%S",timeArray )

			olddata = curs.execute('select * from record_time where name="%s"'%name)
			if olddata >= 1:
				curs.execute('SELECT numbers from record_time where name="%s"'%name)
				tmp_numbers = curs.fetchall()
				numbers = int(tmp_numbers[0][0]) + 1
				curs.execute('update record_time set start_time=%d ,last_time=now() ,numbers=%d ,start_time_read="%s" where name="%s"'%(mid_time,numbers,mid_time_read,name))
			else:
				curs.execute('insert into record_time values("%s",%d,now(),1,"%s")'%(name,mid_time,mid_time_read))
			curs.execute('delete from %s where time<%d;truncate table countavg'%(name,mid_time))
		

conn.commit()
curs.close()
conn.close()
