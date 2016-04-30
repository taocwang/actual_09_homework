#!/usr/bin/env python
#_*_coding:utf-8_*_

#插入排序
'''
描述：首先有一个有序序列，插入一个元素，结果保证依然是一个有序序列
怎么找插入位置：将新插入的元素依次从右到左和序列中的元素比较，
找到第一个比它小或者它已经是第一个元素（元素比它大，交换）
'''
#1
l = [4,1,34,9,26,13,10,7,4]
for i in range(len(l)):
    for j in range(i+1,len(l)):
        if l[i] > l[j]:
            l[i],l[j] = l[j],l[i]
    print(str(l))
print("result: " + str(l))

#2
l = [4,1,9,13,34,26,10,7,4]
for i in range(1, len(l)):
    for j in range(i, 0, -1):
        if l[j - 1] > l[j]:
            l[j-1], l[j] = l[j], l[j-1]
        else:
            break
    print l
#二分查找法
n1 = int(raw_input("guess:"))
L2 = [10,12,18,25,88,92,100,150]
#L2 = [100, 88, 77, 55, 22, 11]
index1 = 0
index2 = len(L2) - 1
while (index1 <= index2):
    mid = (index1 + index2) / 2
    flag = L2[mid]
    if n1 == flag:
        print "number %s is found at index %s!!" %(n1,mid)
        break
    elif n1 < flag:
        index2 = mid -1
    else:
        index1 = mid + 1
else:
    print "number %s is not fount!!!" % n1
    

