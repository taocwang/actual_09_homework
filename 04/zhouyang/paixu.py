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


'''
功能ok，非常棒，继续加油
改进点:
1. python中的注释有两种
    #开头，注释一行
    或者使用三个\'/三个\"注释多行
    切记不要在三个\'之前加#，会破环注释结构
'''
