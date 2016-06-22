#! /usr/bin/python


f = open("user_edges.txt", "r")

cnt = 0
#print("\n")
#print(("\n")
print("Tran_key" + " " + "key_from" + " " + "key_to" + " " + "data" + " " + "balance")
for line in f:
	if cnt==15:
		break
	else:
		print(line)
		cnt = cnt + 1
