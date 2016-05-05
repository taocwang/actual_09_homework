#!/usr/bin/env python
# -*- coding: UTF-8 -*-

list1 = [8,1,7,5,13,16,20]
print list1

for i in range(1,len(list1)):
	for ii in range(0,i):
		if list1[i] < list1[ii]:
			list1[i],list1[ii] = list1[ii],list1[i]
print list1

