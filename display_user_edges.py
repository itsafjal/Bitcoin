#! /usr/bin/python
import numpy as np
from ggplot import *

f = open("user_edges.txt", "r")
user_transication = {}
count = 0
x = []
y = []

for line in f:
	if count == 100000:
		break;
	else:
		count = count + 1
		line = line.split(",")
	        x.append(int(line[0]))
		k = line[4]
		pos = k.find("\n")
		y.append(int(float(k[:pos])))
#	user_transication[int(line[0])] = int(float( k[:pos]))

#print(x,y)
#print(x, y)
#for i in range(20):
#	print(str(x[i]) + " " + str(y[i]))


covariance_xy = np.cov(x,y, rowvar=0)
inv_covariance_xy = np.linalg.inv(covariance_xy)
xy_mean = np.mean(x),np.mean(y)
x_diff = np.array([x_i - xy_mean[0] for x_i in x])
y_diff = np.array([y_i - xy_mean[1] for y_i in y])
diff_xy = np.transpose([x_diff, y_diff])
    
md = []
for i in range(len(diff_xy)):
	md.append(np.sqrt(np.dot(np.dot(np.transpose(diff_xy[i]),inv_covariance_xy),diff_xy[i])))
#print(md)

#print(MahalanobisDist(x,y))


MD = md
threshold = np.mean(MD) * 1.5 # adjust 1.5 accordingly 
nx, ny, outliers = [], [], []
for i in range(len(MD)):
	if MD[i] <= threshold:
		nx.append(x[i])
		ny.append(y[i])
	else:
		outliers.append(i) # position of removed pair
print((np.array(nx), np.array(ny), np.array(outliers), len(np.array(outliers))))

#f = 
#print(MD_removeOutliers(x,y))




import pandas as pd

DF_diff_xy = pd.DataFrame(diff_xy)
DF_diff_xy.rename(columns = lambda x: str(x), inplace=True)
DF_diff_xy.rename(columns={"0": "X"}, inplace=True) # rename a dfcolumn   
DF_diff_xy.rename(columns={"1": "Y"}, inplace=True) # rename a dfcolumn 


print(DF_diff_xy)

g = ggplot(DF_diff_xy, aes(x = 'X', y = 'Y')) + \
geom_point(alpha=1, size=100, color='dodgerblue') + \
geom_point(data = DF_diff_xy[(DF_diff_xy.Y >=4.23) & (DF_diff_xy.X >= -24.01)], alpha=1, size=100, color='red')


print(g)

print("working")

