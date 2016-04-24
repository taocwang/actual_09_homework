# -*- coding: UTF-8 -*-
# by jcui
# by 2016-04-20


#输入数字求平均数
sum = 0
num = 0
n = 0
while num != '' :
    num = raw_input("please input num:")
    if num.isdigit():
        sum = sum + int(num)
        n = n + 1.0
    else:
        n = 1
print "输入数字的个数及平均值------------------------------------------------"
print sum / n



#九九乘法表
print "九九乘法表:------------------------------------------------"
for x in range(1,10):
    print
    for y in range(1,x+1):
        print  '%d x %d = %2d' % (x,y,x*y)  ,

print "\n "




#取列表最大的两个值
list = [1,-2,-1,2,3,4,54,5,6,7,8,9,9,45,65535,558,65535]
m = 0
n = 0
for i in list:
    if i > m:
        m = i
    elif n < i :
        n = i
print "求最大的两个数:------------------------------------------------"
print m,n




#列表排序
for i in range(0,len(list)):
    for j in range(i+1,len(list)):
        if list[i] > list[j]:
            list[i],list[j] = list[j],list[i]
print "列表排序:------------------------------------------------"
print list





#求10000块钱存多久可以翻倍

sum = 10000
n = 0
while True:
    sum = sum * (1+0.003)
    if sum >= 20000:
        break
    n = n + 1
print "存钱翻倍:------------------------------------------------"
print "%d年之后钱翻倍" % n




#求每个元素出现的次数
nn = ['asd','afa','asd','arf','afas','asd','afa','arf']
nm = {}
for x in nn:
    if x in nm:
        nm[x] += 1
    else:
        nm[x] = 1
print nm

'''
作业ok，在写代码时注意变量命名与python关键字和内置变量冲突，比如sum、list的使用，随课程介绍经验积累，加油
'''