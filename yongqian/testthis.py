import os
import sys
my = os.system('impala-shell.sh -i master -d snmp -q "select count(*) from yongqian;"')
print "HAHA"
print my
