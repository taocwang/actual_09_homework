#!/usr/bin/env python
# coding=utf-8



l=[(9,-2),(8,5),(3,4),(22,2),(0,8),(2,7),(0,1)]
print "排序前：%s" %l

#使用sort 或sorted+max 直接排序
#l.sort(key=lambda x:max(x))
l=sorted(l,key=lambda x:max(x))
print "方法一排序后:%s" %l

#使用排序法
x=0
while x>(len(l)-1):
    for i in l:
        #if i[x][0] > i[x+1][0] or i[x][1] > i[x+1][1]:
        if max(i)>max(i+1):
            i[x],i[x+1] = i[x+1],i[x]
    x-=1
print "方法二排序后:%s" %l


