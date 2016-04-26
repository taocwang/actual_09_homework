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
L2 = [10,12,18,25,88,92,100,150]
#L2 = [100, 88, 77, 55, 22, 11]
      
    

