#!/bin/env python
#coding:utf8
'''取出数列中最大的两个数字'''

num = [1,2,3,2,12,3,1,3,21,2,2,3,4111,22,3333,444,111,4,5,777,65555,45,33,45]

max=num[0]
next_max=num[1]

for nu in num:
    if nu > max:
        next_max=max
        max=nu
    elif next_max < nu < max:
        next_max=nu

print "最大的两个数字是%d和%d" % (max,next_max)


'''
功能ok，后续随着课程的积累，尽量避免python中关键字和已使用变量的冲突定义
'''