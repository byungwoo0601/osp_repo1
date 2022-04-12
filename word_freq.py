#!/usr/bin/python3

import sys
a = sys.argv[1]
b = sys.argv[2]
#print(a)
f = open(a, 'r')
line=None
while line != ' ':
	line=f.readline()
	print(line,end='')
f.close()
