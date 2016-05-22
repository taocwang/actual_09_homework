#!/usr/bin/env python
# -*- coding:utf-8 -*-

'''
作业：
一个list[(1,4),(5,1),(2,3)],根据每个元组中的较大值进行排序
期待结果：[(2,3),(1,4),(5,1)]
'''

##方法1：
def is_max(t):
	result = None
	for i in range(len(t)):
		if t[i] > result:
			result = t[i]
	return result


#使用自定义求最大值函数进行冒泡排序
def my_sort(rlist):
	for j in range(len(rlist) - 1):
		for k in range(len(rlist) - 1 - j):
			if is_max(rlist[k]) > is_max(rlist[k + 1]):
				rlist[k], rlist[k + 1] = rlist[k + 1], rlist[k]
	return rlist


#使用系统函数max然后进行冒泡排序
def sys_sort(rlist):
	for j in range(len(rlist) - 1):
		for k in range(len(rlist) - 1 - j):
			if max(rlist[k]) > max(rlist[k + 1]):
				rlist[k], rlist[k + 1] = rlist[k + 1], rlist[k]

	return rlist
	
rlist = [(1, 4), (5, 1), (2, 3), (2, 1), (8, 5), (2, 3), (6, 4), (15, 8), (-10 ,2), (-8, -2)]
print my_sort(rlist)
print sys_sort(rlist)

#列表推导式：(使用自定义函数进行列表推导式操作)
rlist = [(1, 4), (5, 1), (2, 3), (2, 1), (8, 5), (2, 3), (6, 4), (15, 8), (-10 ,2), (-8, -2)]
result_list = sorted(rlist, key=lambda x:is_max(x))
print result_list

'''
非常棒，继续加油
改进点: 已经学习了函数，将排序函数能不能封装成函数
'''
