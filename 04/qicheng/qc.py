#!/usr/bin/env python
#-*-coding: UTF-8-*-

def local_sorted(x):
	for i in x:
		a = x[0]
		if i > a:
			a = i
	return a	
def local_comp(y):
	for iii in range(0,len(y) -1):
		for ii in range(0,len(y) -1):
			if local_sorted(y[ii]) > local_sorted(y[ii + 1]):
				y[ii],y[ii + 1] = y[ii + 1],y[ii]
	return y		

y = [(1,4,5),(5,1,6),(2,3,8)]	
print local_comp(y)	
