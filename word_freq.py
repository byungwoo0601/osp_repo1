#!/usr/bin/python3
import sys
a = sys.argv[1]
b = sys.argv[2]

f = open(a, 'r')

file = f.read()
#print(file)
file1 = file.replace("?","")

print(file1)
f.close()
