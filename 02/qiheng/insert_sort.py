#!/bin/env python
#encoding: utf-8

num_list = [11,22,33,44,443,34,11,22,33]
print '原始'
print num_list
for i in range(1, len(num_list)):
    for x in range(i, 0, -1):
        if num_list[x] < num_list[x -1]:
                num_list[x], num_list[x - 1] = num_list[x - 1], num_list[x]
        else:
                break
    print '排序索引为%s的元素后' % i
    print num_list
