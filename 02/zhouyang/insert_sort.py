#!/bin/env python
#coding:utf8
'''插入排序'''
nu_list=[1,2,3,6,23,234,2222]
print nu_list
insert_nu=input("insert your number: ")
for i in nu_list:
    if i > insert_nu:
        nu_list.insert(nu_list.index(i),insert_nu)
	    break

print nu_list
