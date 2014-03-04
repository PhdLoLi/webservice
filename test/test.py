import impala.dbapi
conn = impala.dbapi.connect(host='master', port=21050)
cursor = conn.cursor()
cursor.execute('use snmp')
cursor.execute('SELECT * FROM yongqian LIMIT 100')
print cursor
cursor.execute('SELECT count(*) from yongqian')
#print cursor
for row in cursor:
	print row
conn.commit()
cursor.close()
conn.close()
