#!/usr/bin/python
import os
import re
import sys
import numpy as np


pattern = "Ultradns quiz application"
ms_list = []

file = open("/Users/shashidhar.buyakar/Downloads/MadeupLog.log", "r")
for line in file:
    if re.search(pattern, line):
        fields = line.strip().split()
        ms_list.append(int(fields[7]))

file.close()

lastn = ms_list[-20:]

print("Mean: % s" %(np.average(lastn)))

print("Standard Deviation: % s" %(np.std(lastn)))





