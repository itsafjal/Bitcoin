#! /usr/bin/python

f = open("user_edges.txt", "r")
val = {}
x =[]
y = []
for line in f:
	line = line.split(",")
	x.append(int(float(line[1])))
	y.append(int(float(line[2])))

print(len(set(x)), len(set(y)))

'''x = [1,2,3,1,2,3]
y=[32,423,42,52,523,5232]'''
val = {}

cnt = 0
for i in range(len(x)):
 	j = i + 1
	#print (j)
 	if x[i] not in val.keys():
		 val[x[i]] = []
		 for j in range(i, len(x)):
			 #print (j)
			 if x[i]==x[j]:
				 val[x[i]].append(y[j])
			 j=j+1
	print(val[x[i]])

print(val)
