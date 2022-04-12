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
file4 = file3.replace(",","")
file5 = file4.replace("-","")
#print(file5)

file6 = file5.split()
#print(file4)

counts = dict()
for i in file6:
	if i not in counts:
		counts[i] = 1
	else:
		counts[i] += 1

#print(file6)
#print(counts)

word = sorted(counts.items(), key = lambda item: item[1] ,reverse=True)

#print(word)

#print(word[:int(b)])

for key, value  in word[:int(b)]:
	print("{0:15}".format(key), value)



	

f.close()
