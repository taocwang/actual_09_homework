#!/usr/bin/env python
# -*- coding: utf-8 -*-
#根据list中的每个元祖取到最大值并依据最大值排序
#使用sorted,lambda以及max函数直接对列表进行排序
List=[(1,4),(5,1),(2,3),(7,5),(3,2),(1,9),(6,2),(3,5)]
print sorted(List, key=lambda x:max(x))
#使用MaxNum替代max函数的功能，以及lambda和sorted对列表进行排序

def MaxNum(Tuple):
    MaxNumber=0
    for i in range(0,len(Tuple)-1):
        if Tuple[i]<Tuple[i+1]:
            MaxNumber=i+1
    return Tuple[MaxNumber]
List=[(1,4),(5,1),(2,3),(7,5),(3,2),(1,9),(6,2),(3,5)]
print sorted(List,key=lambda x:MaxNum(x))
#使用冒泡方式对列表进行排序
List=[(1,4),(5,1),(2,3),(7,5),(3,2),(1,9),(6,2),(3,5)]
for i in range(0,len(List)-1):
    for j in range(i+1,len(List)):
        if MaxNum(List[i])>MaxNum(List[j]):
            List[i],List[j]=List[j],List[i]
print List