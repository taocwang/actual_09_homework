#!/usr/bin/env python
#_*_coding:utf-8_*_

#插入排序法
l = [4,1,9,13,34,26,10,7,4]
for i in range(len(l)):
    for j in range(i+1,len(l)):
        if l[i] > l[j]:
            l[i],l[j] = l[j],l[i]
    print(str(l))
print("result: " + str(l))


#二分查找法
n1 = int(raw_input("guess:"))
#L2 = [10,12,18,25,88,92,100,150]
L2 = [100, 88, 55, 77, 22, 11]
mid = len(L2) / 2
index = mid
if L2[0] < L2[-1]:
    while True:
        if n1 > L2[mid] and len(L2[mid:])>1:
            L2 = L2[mid:]
            mid = len(L2) / 2
            index += mid
        elif n1 < L2[mid] and len(L2[:mid])>1:
            L2 = L2[:mid+1]
            mid = len(L2) / 2
            index -= mid
        elif n1 == L2[mid]:
            print "Your number %s in the list index is %s !!!" %(n1, index)
            break
        else:
            print "Your number %s is not in the list!!" % n1
            break
else:
    while True:
        if n1 > L2[mid] and len(L2[mid:])>1:
            L2 = L2[:mid]
            mid = len(L2) / 2
            index -= mid
            print mid,index
        elif n1 < L2[mid] and len(L2[:mid])>1:
            L2 = L2[mid:]
            mid = len(L2) / 2
            index += mid
            print mid,index
        elif n1 == L2[mid]:
            print "Your number %s in the list index is %s !!!" %(n1, index)
            print mid,index
            break
        else:
            print "Your number %s is not in the list!!" % n1
            break       
    

