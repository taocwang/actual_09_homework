#!/usr/bin/env python
#-*-coding: UTF-8 -*-

def logscount(nhtml='www_access_20140823.html',path='www_access_20140823.log',cut=10):
	temp = []
	log = {}
	temp2 = []
	rh = open(path,'r')
	for rf in rh:
		x = (rf.split(' ')[0], rf.split(' ')[6], rf.split(' ')[8])
		log[x] = log.get(x,1) + 1
	rh.close()


	temp2 = log.items()

	#temp2 = log.items().sort()
	for ii in range(0,cut):
		for i in range(0,len(temp2) - 1 - ii):
			if temp2[i][1] > temp2[i + 1][1]:
				temp2[i],temp2[i + 1] = temp2[i + 1],temp2[i]	

	return temp2[-1:-cut -1:-1]


if __name__ == '__main__':	
	print logcount()

