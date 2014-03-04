import impala.dbapi
import time
import MySQLdb
import string
import sys

def query(content):
	nearby = 3600
	result = []
	if "join" in content.lower() or "time" not in content.lower():
		print "EXISTS JION!"
		return result
	else:
		my = content.lower().strip().split()
#		print my
		p = my.index('from')
		name = my[p+1]
		print name
		start_time = 0
		end_time = 0

		first = my.index('time')
		if my[first+1]==">=" or my[first+1]==">":
			start_time = int(my[first+2])
		elif my[first+1]=="<=" or my[first+1]=="<":
			end_time = int(my[first+2])
		newmy = my[first+1:]
		if 'time' in newmy:
			second = newmy.index('time')
			if newmy[second+1]==">=" or newmy[second+1]==">":
				start_time = int(newmy[second+2])
			elif newmy[second+1]=="<=" or newmy[second+1]=="<":
				end_time = int(newmy[second+2])

		print "start_time:"+str(start_time)
		print "end_time:"+str(end_time)


		conn = MySQLdb.connect(host='localhost',user='root',passwd='881230',db='snmp') 
		curs = conn.cursor()
		exits = curs.execute('show tables like "%s"'%name)

		if exits >= 1:
		#if table name exits in mysql
			curs.execute('select start_time from record_time where name="%s"'%name)
			tmp_time = curs.fetchall()
			actual_start_time = tmp_time[0][0]
			print "actual_start_time:"+str(actual_start_time)
			timediff = actual_start_time - start_time
			if actual_start_time <= start_time:
				#alltime include in mysql type 1
				print "TYPE 1"
				curs.execute(content)
				result = curs.fetchall()
				conn.commit()
				curs.close()
				conn.close()
				return result
			elif timediff <= nearby:
				#now nearby 3600second
				print "TYPE 2"
				conn = impala.dbapi.connect(host='master', port=21050)
				cursor = conn.cursor()
				cursor.execute('use snmp')
				cursor.execute('select * from %s where time<%d and time>=%d',%(name,actual_start_time,start_time))
				result = cursor.fetchall()
				conn.commit()
				cursor.close()
				conn.close()
				# select from Banya 

				conn = MySQLdb.connect(host='localhost',user='root',passwd='881230')
				curs = conn.cursor()
				conn.select_db('snmp')
				columns = curs.execute("desc %s"%name)
				print columns

				values_len = "values("
				for i in range(columns-1):
					values_len += "%s,"
				values_len += "%s)"
				print values_len

				# Insert into mysql
				curs.executemany("insert into %s"%name+" %s"%values_len,result)
				# Update the table record_time
				timeArray = time.localtime(start_time)
				start_time_read = time.strftime("%Y-%m-%d %H:%M:%S",timeArray )

				olddata = curs.execute('select * from record_time where name="%s"'%name)
				if olddata >= 1:
					curs.execute('SELECT numbers from record_time where name="%s"'%name)
					tmp_numbers = curs.fetchall()
					numbers = int(tmp_numbers[0][0]) + 1
					curs.execute('update record_time set start_time=%d ,last_time=now() ,numbers=%d ,start_time_read="%s" where name="%s"'%(start_time,numbers,start_time_read,name))
				else:
					curs.execute('insert into record_time values("%s",%d,now(),1,"%s")'%(name,start_time,start_time_read))
				curs.execute('truncate table countavg')
				
				curs.execute(content)
				result = curs.fetchall()

				conn.commit()
				curs.close()
				conn.close()

				return result

		
		#Banya Here
		print "Banya time!"
		conn = impala.dbapi.connect(host='master', port=21050)
		cursor = conn.cursor()
		cursor.execute('use snmp')
		cursor.execute(content)
	#	for row in cursor:
	#		result.append(row)
		
		result = cursor.fetchall()
		conn.commit()
		cursor.close()
		conn.close()
		return result

if __name__ == '__main__':
	
#	cursor = query("select * from yongqian limit 100")
	result = query("select * from yongqian where time  < 1388527210 AND time  >= 1388527105 ")
	print result
