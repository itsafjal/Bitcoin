#! /usr/bin/python

f = open("user_edges.txt", "r")
#cnt = 0
'''
for line in f:
	print(line)
	if cnt==5:
		break
	cnt = cnt + 1
'''
val = {}
x =[]
y = []
cnt = 0
for line in f:
	line = line.split(",")
#	y.append(int(float(line[1])))
	x.append(int(float(line[2])))
	cnt = cnt + 1
	if cnt==1000:
		break
cnt = 0
for line in f:
        line = line.split(",")
        y.append(int(float(line[1])))
 #       x.append(int(float(line[2])))
        cnt = cnt + 1
        if cnt==10000:
                break
#print(x)

for i in range(len(min(x,y))):
        print(x[i],y[i])


val = {}


for i in range(len(x)):
 	if x[i] not in val.keys():
		 val[x[i]] = []
		 for j in range(i+1, len(x)):
			 #print (j)
			 if x[i]==x[j]:
				 val[x[i]].append(y[j])

for key in val.keys():
	print(len(val[key]))

