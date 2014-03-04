import os
buffer = "one\n"
file= open("test.txt",'a')
file.write(buffer)
file.close()
buffer = "two\n"

file= open("test.txt",'a')
file.write(buffer)
file.close()
