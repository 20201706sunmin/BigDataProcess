#!/usr/bin/python3

import sys
import calendar

dayofweek = ['MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT', 'SUN']

datafile = sys.argv[1]
output = sys.argv[2]

s = ""
with open(datafile, "rt") as f:
	for line in f:
		info = line.split(",")
		date = info[1].split("/")
		
		day = calendar.weekday(int(date[2]), int(date[0]), int(date[1]))
		s += info[0] + "," + dayofweek[day] + " " + str(info[2]) + "," + str(info[3])
	#print(s)
	
with open(output, "wt") as op:
	op.write(s)

	
	
