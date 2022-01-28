#!/bin/python3
import sys
with open(sys.argv[1], "r") as ip1, open(sys.argv[2], "r") as ip2:
     file1 = ip1.read().split("\n")[:-1]
     file2 = ip2.read().split("\n")[:-1]
#print(file1)
#print(file2)

ip3 = []
ip4 = []
for i in file1:
    if i in file2:
       ip3.append(i)
#print(ip3)

for i in file2:
    if i not in file1:
       ip4.append(i)
print(ip4)
