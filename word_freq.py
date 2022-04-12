#!/usr/bin/python3
import sys
a = sys.argv[1]
b = sys.argv[2]

f = open(a, 'r')

file = f.read()
#print(file)
file1 = file.replace("?","")
file2 = file1.replace("!","")
file3 = file2.replace(".","")
#print(file3)

file4 = file3.split()
print(file4)




f.close()
