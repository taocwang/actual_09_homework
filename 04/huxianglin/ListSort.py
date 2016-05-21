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


'''
功能 ok
排序方法每次保证第i(0->n-1)为最小的元素

改进:
1. 函数MaxNum，如果Tuple是两个元素的list/tuple是ok的，但是如果是多个呢比如(4, 1, 2)
    原因: line 12，是不是应该每次和最大的值相比

加油
'''
