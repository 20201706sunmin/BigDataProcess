#!/usr/bin/python3

import sys
import calendar

dayofweek = ['MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT', 'SUN']

datafile = sys.argv[1]
output = sys.argv[2]

rd = ""
data = dict()
list1 = []
list2 = []
v_sum = 0
t_sum = 0	
with open(datafile, "rt") as f:
	for line in f:
		info = line.split(",")
		date = info[1].split("/")
		day = calendar.weekday(int(date[2]), int(date[0]), int(date[1]))
		
		rd = info[0] + "," + dayofweek[day]
		
		if rd not in data:
			v = int(info[2])
			t = int(info[3])
			data[rd] = [v, t]
			
		else:
			v = int(info[2])
			t = int(info[3])
			list1 = data[rd]
			
			v_sum = int(list1[0]) + v
			t_sum = int(list1[1]) + t
			
			data[rd] = [v_sum, t_sum]
	#print(data)


with open(output, "wt") as op:
	for i in data:
		list2 = data[i]
		op.write(i + " " + str(list2[0]) + "," + str(list2[1]) + "\n")
	
