#!/usr/bin/env python
# coding=utf-8

l=[(9,-2),(8,5),(3,4),(22,2),(0,8),(2,7),(0,1)]
print "排序前：%s" %l

#使用sort 或sorted+max 直接排序
#l.sort(key=lambda x:max(x))
l=sorted(l,key=lambda x:max(x))
print "方法一排序后:%s" %l

#使用排序法
x=len(l)
while x>0:
    for i in range(0,x-1):
        if max(l[i])>max(l[i+1]):
            l[i],l[i+1] = l[i+1],l[i]
            #print l
    x-=1
print "方法二排序后:%s" %l

'''
功能ok，继续加油
'''
