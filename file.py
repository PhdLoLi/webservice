import os
buffer = "ceshi"
file = open('file.txt','w')
file.write(buffer)
file.close()
print "OK\n"
print buffer
