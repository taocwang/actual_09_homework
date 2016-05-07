#!/usr/bin/env python
# coding=utf-8



#l=[25,12,45,56,56,56,4,69]
#l=[1,3,22,44,9,7,34,78,1,22]
l=[6,5,4,3,2,1,7]
print "交换前列表为：%s\n" %l
x=len(l)
cnt=0

while x>0:
    for i in range(0,len(l)-1):
        if l[i] > l[i+1]:
            l[i],l[i+1] = l[i+1],l[i]
            print "swap %s[%s]<->%s[%s]" %(i,l[i+1],i+1,l[i])
            print "本次交换后的顺序为：%s" %l
            cnt+=1
            #print "排序%s个数排序到最后:\n %s" %(i+1,l)
    
    print "经过%s次排序后的顺序结果为：%s" %(cnt,l)
    print ""
    x-=1
print l
print "本次排序总共交换次数为：%s" %cnt
