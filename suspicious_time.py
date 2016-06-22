#! /usr/bin/python
import statistics
import numpy
import statistics
import numpy
from matplotlib import pyplot as plt

f = open("user_edges.txt", "r")
x = []
y = []
z = []
tid = []
v = 0
for line in f:
        val = line.split(",")
#	print(val)
	tid.append(int(val[0]))
	x.append(int(float(val[1])))
	y.append(int(float(val[2])))
	z.append(int(val[3]))
	if v==100000:
		break
	v = v + 1
print(len(x), len(y), len(z))
x.sort()
y.sort()	
val = {}
for i in range(len(x)):
	if x[i] not in val.keys():
		val[x[i]] = []
		for j in range(i+1,len(x)):
			if x[i]==x[j]:
				val[x[i]].append(y[j])
#print(val)
for keys in val.keys():
	tt = set(val[keys])
	val[keys] = list(tt)
#print(val)
count = 0
susp = []
normal = []
number = []
number1 = []
num = 1
max = 0
for key in val.keys():
	mydata = val[key]
	kk = len(mydata)
	i = 0
	while i <kk-1:
		cnt = 0
		j = i + 1
		while j<kk and abs(mydata[j] - mydata[j-1]) == 1:
			j = j + 1
			cnt = cnt + 1
		i = j
		if cnt >=2:
			count = count + 1
	num = num + 1
	if max < count:
		susp.append(key)
		number.append(num)
		max = count
	else:
		normal.append(key)
		number1.append(num)
	
	
print(count, len(susp), len(normal))		
'''
cnt = 0
for i in range(len(x)-1):
	for j in range(i+1, len(x)):
		if x[i]==x[j] and abs(y[i]-y[j])==1:
			if abs(tid[j]-tid[i])==0:
				cnt = cnt + 1
print(cnt)
'''
p = number
q = susp
p1 = number1
q1 = normal
plt.scatter(p,q)
plt.scatter(p1,q1, color="g")
plt.title("outliers")
plt.ylabel("y axis")
plt.xlabel("x axis")
plt.show()
