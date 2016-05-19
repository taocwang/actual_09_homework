#!/usr/bin/env python
#-*-coding: UTF-8-*-
# '''
一个list[(1,4),(5,1),(2,3)],根据每个元组中的较大值进行排序
#期待结果：[(2,3),(1,4),(5,1)]
 '''

 src_list=[(1,4),(5,1),(2,3)]
 for j in range(len(src_list) + 1):
 	for i in range(len(src_list)):
	    if max(src_list[i]) > max(src_list[i+1]):
		src_list[i],src_list[i+1] = src_list[i+1],src_list[i]
print src_list
