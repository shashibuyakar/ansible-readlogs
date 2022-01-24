#!/usr/bin/python
import os
import re
import sys


pattern = "Ultradns quiz application"
ms_list = []

file = open("/home/ec2-user/MadeupLog.log", "r")

for line in file:
    if re.search(pattern, line):
        fields = line.strip().split()
        ms_list.append(int(fields[7]))

file.close()

lastn = ms_list[-20:]

mean = sum(lastn) / float(len(lastn))
variance = sum([((x - mean) ** 2) for x in lastn]) / len(lastn)
res = variance ** 0.5

print("Mean:" + ' ' + str(mean))
print("Standard Deviation:" + ' ' + str(res))





