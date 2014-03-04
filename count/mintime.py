import MySQLdb
import time
import sys
import os
import string
import datetime

dbname ='new'
conn = MySQLdb.connect(host='localhost',user='root',passwd='881230',db=dbname)
curs = conn.cursor()
number = curs.execute('show tables')
tables = curs.fetchall()

for i in range(number):
	name = tables[i][0]
	exits = curs.execute('select * from information_schema.COLUMNS where TABLE_SCHEMA="%s" AND TABLE_NAME="%s" AND COLUMN_NAME="time"'%(dbname,name))

	if exits >= 1:
		print name
		print exits
		curs.execute('SELECT MIN(time) from %s'%name)
		tmp_start_time = curs.fetchall()
		start_time = tmp_start_time[0][0]
		timeArray = time.localtime(start_time)
		start_time_read = time.strftime("%Y-%m-%d %H:%M:%S",timeArray )
		olddata = curs.execute('select * from record_time where name="%s"'%name)
		if olddata < 1:
			curs.execute('insert into record_time values("%s",%d,now(),0,"%s")'%(name,start_time,start_time_read))
			print "here"
		

conn.commit()
curs.close()
conn.close()
