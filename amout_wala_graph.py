#! /usr/bin/python
import statistics
import numpy
from matplotlib import pyplot as plt
f = open("user_edges.txt", "r")
x = []
y = []
z = []
for line in f:
        val = line.split(",")
#       print(val[3])
#       print(val)
        x.append(val[3])
        y.append(float(val[4]))
print(len(x),len(y))

peak = 49.9378768165 + 1399.2004138
#print(statistics.mean(y))
#print(statistics.stdev(y))
p = []
q = []
p1 = []
q1 = []
cnt = 0
for val in y:
        if val >peak and cnt <100000:
                z.append(val)
		p.append(cnt)
		q.append(val)
		cnt = cnt + 1
	else:
		p1.append(cnt)
		q1.append(val)
		cnt = cnt + 1
		if cnt==100000:
			break
print(len(p),len(q), len(p1), len(q1))
print(len(z))

t1 = [5,8,10]
t2 = [12,16,6]
t3 = [6,9,11]
t4 = [6,15,7]
plt.scatter(p,q)
plt.scatter(p1,q1, color="g")
plt.title("outliers")
plt.ylabel("y axis")
plt.xlabel("x axis")
plt.show()

