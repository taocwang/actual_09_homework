# -*- coding: UTF-8 -*-
# by jcui
# by 2016-04-18

sum = 0
num = 0
n = 0
while num != '' :
    num = raw_input("please input num:")
    if num.isdigit():
        sum = sum + int(num)
        n = n + 1.0

print sum / n


#九九乘法表
for x in range(1,10):
    print
    for y in range(1,x+1):
        print  '%d x %d = %2d' % (x,y,x*y)  ,


#取列表最大的两个值
list = [1,2,3,4,54,5,6,7,8,9,9,45]
m = 0
n = 0
for i in list:
    if i > m:
        m = i
    elif n < i <m:
        n = i
print m,n