#!/usr/bin/env python
#_*_coding:utf-8_*_

li = [-5, -2, -9, -7, 10]

num = [None, None]

for i in li:
    if i > num[0]:
        num[1] = num[0]
        num[0] = i 
    elif i > num[1]:
        num[1] = i

print "The large number is %d, The bigger number is %d" %(num[0], num[1])

'''
功能ok，可以考虑下该种做法的优缺点，比如list中都有负数呢？
'''