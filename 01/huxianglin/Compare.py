#!/usr/bin/env python
# -*- coding: utf-8 -*-

#列表取最大值以及最小值
List = [1,2,3,2,12,3,1,3,21,2,2,3,4111,22,3333,444,111,4,5,777,65555,45,33,45]
Min,Max = List[0],List[0]
for i in List:
    if i < Min:
        Min = i
    elif i > Max:
        Max = i
print "The max is %s" % (Max)
print "The min is %s" % (Min)

#列表去重
List2 = []
for i in List:
    if i in List2:
        pass
    else:
        List2.append(i)
print List2

#列表排序
 #1冒泡排序
for i in range(0,len(List)-1):
    for j in range(i+1,len(List)):
        if List[i]>List[j]:
            List[i],List[j]=List[j],List[i]
print List
  
 #2冒泡排序的改进（双向排序）
for i in range(0,len(List)/2):
    for j in range(i,len(List)-i-1):
        if List[i]>List[j]:
            List[i],List[j]=List[j],List[i]
        if List[j]>List[len(List)-i-1]:
            List[j],List[len(List)-i-1] = List[len(List)-i-1],List[j]
print List