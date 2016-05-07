#!/bin/env python
#coding:utf8
'''插入法排序
这是网上的做法，我仍然不懂它跟冒泡法的区别
'''
A=[2,3,12,32,112,322,112,23,2,12,2]
def insert_s(array):
	for i in range(1,len(array)):
	    key = array[i]:
	    j=i-1
	    while j >=0 and key <array[j]:
	        array[j+1]=array[j]
		j-=1
	    array[j+1]=key

num_list=[2,3,2,12,3,212,3,21]
insert_s(num_list)
print num_list
