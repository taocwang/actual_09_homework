#!/usr/bin/env python
#-*- coding: UTF-8 -*-

num = [1,2,3,2,12,3,1,3,21,2,2,3,4111,22,3333,444,111,4,5,777,65555,45,33,45]
max=num[0]
max2=num[0]

for i in num:
	if i > max:
		max2=max
		max = i
		
print '列表中第一大数字为:%s,第二大数字为:%s' % (max,max2)
