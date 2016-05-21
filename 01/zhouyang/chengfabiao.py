#!/bin/env python
#coding:utf8
'''99乘法表'''

for i in range(1,10):
    for j in range(1,i+1):
        print "%d*%d=%2d" % (i,j,i*j),  #%2表示右对齐两位
    print

'''
功能ok
'''
