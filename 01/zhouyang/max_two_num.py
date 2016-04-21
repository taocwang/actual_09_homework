#!/bin/env python
#coding:utf8
num = [1,2,3,2,12,3,1,3,21,2,2,3,4111,22,3333,444,111,4,5,777,65555,45,33,45]

max=num[0]
next_max=num[1]
for nu in A:
    if nu > max:
	    next_max=max
		max=nu
	elif next_max < nu < max:
	    next_max=nu

print "最大的两个数字是%d和%d" % (max.next_max)
