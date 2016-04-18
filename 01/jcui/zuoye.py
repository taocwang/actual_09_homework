# -*- coding: UTF-8 -*-

# sum = 0
# num = 0
# n = 0
# while num != '' :
#     num = raw_input("please input num:")
#     if num.isdigit():
#         sum = sum + int(num)
#         n = n + 1.0
#
# print sum / n


#九九乘法表
for x in range(1,10):
    print
    for y in range(1,x+1):
        print  '%d x %d = %2d' % (x,y,x*y)  ,