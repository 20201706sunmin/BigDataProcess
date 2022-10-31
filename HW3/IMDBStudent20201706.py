#!/usr/bin/python3

import sys

datafile = sys.argv[1]
output = sys.argv[2]
info = []
all_g = []
genre = []
dicGen = dict()
with open(datafile, "rt") as f:
	for line in f:
		info = line.split("::")
		genre = []
		if('|' in info[2]):
			genre = info[2].split("|")
			info_len = len(genre)
			genre[info_len-1] = genre[info_len-1].strip("\n")
			
		else:
			info[2] = info[2].strip("\n")
			genre.append(info[2])
					
		for i in genre:
			all_g.append(i)	
			
	for element in all_g:
		if element not in dicGen:
			dicGen[element] = 1
		else:
			dicGen[element] += 1
	#print(dicGen)
with open(output, "wt") as op:
	for i in dicGen:
		op.write(i + " " + str(dicGen[i]) + "\n")

