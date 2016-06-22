#! /usr/bin/python 

f = open("user_edges.txt", "r")

count = 0
for line in f:
	count = count + 1


print("Number of entry in this file" + "= " + str(count)) 
