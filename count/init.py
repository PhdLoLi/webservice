import sys
import os
import string
import MySQLdb

class initDBHDFS:
	name = ''
	mysqltable = ''
	banyatable = ''
	def _init_(self,name,mysqltable,banyatable):
		self.name = name
		self.mysqltable = mysqltable
		self.banyatable = banyatable
	def DB(self):
	conn = MySQLdb.connect(host='localhost',user='root',passwd='881230')
	curs = conn.cursor()
	conn.select_db('snmp')
	curs.execute("%s"%self.mysqltable)
	conn.commit()
	curs.close()
	conn.close()
	os.system('impala-shell.sh -i mster -d snmp -q "%s"'%banyatable)

		

