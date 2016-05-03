#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 将一个元素插入到一个有序的列表中
num_list = [1, 3, 4, 5, 6, 2]
start = len(num_list) - 1
end = 0
step = -1
cont = 0
for j in range(0, len(num_list)):
    for i in range(start, end + j, step):
        cont += 1
        if num_list[i] < num_list[i - 1]:
            num_list[i - 1], num_list[i] = num_list[i], num_list[i - 1]
print "排序后的列表：%s " % num_list
print "程序一共比较了%s次！" % cont

# 将多个元素插入到一个有序的列表中
num_list = [4, 11, 12, 13, 14, 15, 7, 23, 9, 3, 5, 2, 6]
cont = 0
for j in range(1, len(num_list)):
    for i in range(j, 0, - 1):
        cont += 1
        if num_list[i] < num_list[i - 1]:
            num_list[i - 1], num_list[i] = num_list[i], num_list[i - 1]
        else:
            break
print "排序后的列表：%s " % num_list
print "程序一共比较了%s次！" % cont
print "插入排序算法完成！"