#!/usr/bin/env python
#_*_coding:utf-8_*_

li = [11, 999999, 280000, 9222, 1000000, 533433, 24444,4513456]

num = [0, 0]

for i in li:
    if i > num[0]:
        num[1] = num[0]
        num[0] = i 
    elif i > num[1]:
        num[1] = i

print "The large number is %d, The bigger number is %d" %(num[0], num[1])