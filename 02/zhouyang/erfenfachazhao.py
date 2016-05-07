#!/bin/env python
#coding:utf8
'''二分法查找
'''
nu_list=[1, 3, 5, 6, 8, 9]

def erfen(n_list,num):
    low = 0
    high=len(n_list) - 1
    find_times=0
    while low <= high:
        midd = (low + high) / 2
	find_times += 1
	if n_list[midd] > num:
	    high = midd - 1
	elif n_list[midd] < num:
	    low = midd + 1
	else:
	    print n_list[midd]
	    break
    return find_times

times=erfen(nu_list,3)
print "Used %d times to find the number" % times
