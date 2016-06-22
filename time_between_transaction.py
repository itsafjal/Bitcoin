#! /usr/bin/python
import statistics
import numpy
f = open("user_edges.txt", "r")
x = []
y = []
z = []
for line in f:
	val = line.split(",")
#	print(val[3])
#	print(val)
	x.append(val[3])
	y.append(float(val[4]))
print(len(x),len(y))

peak = 49.9378768165 + 1399.2004138
#print(statistics.mean(y))
#print(statistics.stdev(y))
for val in y:
	if val >peak:
		z.append(val)

print(len(z))

import matplotlib.pyplot as plt
import numpy as np
spread = z
flier_high = [statistics.median_high(z)]
flier_low = [statistics.median_low(z)]

print(flier_high, flier_low)

data = np.concatenate((spread, flier_high, flier_low), 0)

plt.boxplot(data,1)
plt.figure()
plt.show()
'''

for i in range(1,len(x)):
	x[i-1] = float(x[i])-float(x[i-1])

ll = []
mm = []
val1 =  795472.786876 - 4077140971.53

print(val1)

for data in x:
	ll.append(float(data))
#print(statistics.mean(ll))
#print(statistics.stdev(ll))
for data in ll:
	print(data)
#	if data>0 and data < val1:
#		mm.append(data)
#print(len(mm))

#for i in range(len(x)):
#	print(x[i])
import plotly.plotly as py
import plotly.graph_objs as go

import numpy as np
#py.signin("itsafjal", "8bvh80ja93")
py.sign_in("itsafjal", "8bvh80ja93")
y0 = x
y1 = y

m1 = go.Box(
    y=y0
)
m2 = go.Box(
    y=y1
)
data = [m1, m2]
plot_url = py.plot(data, filename='basic-box-plot')
'''
