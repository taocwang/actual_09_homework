#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
作业：
[(1, 4), (3, 7), (2, 6), (3, 1), (5, 2), (9, 1)]
将上面list元素里，每个元组中的最大值进行排序，从小到大排序；
思路：
1、获取list的长度
2、将元组里最大值进行比较，并排序
3、打印出结果
'''
# 实战：
# 方法1：使用最传统的冒泡排序方法
num_list = [(1, 4), (3, 7), (2, 6), (3, 1), (5, 2), (9, 1)]
def SortList(num_list):
    for i in range(0, len(num_list)):
        for num in range(0, len(num_list) - 1 - i):
            if max(num_list[num]) > max(num_list[num + 1]):
                 num_list[num], num_list[num + 1] = num_list[num + 1], num_list[num]
    return num_list
print '方法1，传统的冒泡排序法实现：%s' % SortList(num_list)

# 方法2：使用sorted方法
arr = [(1, 4), (3, 7), (2, 6), (3, 1), (5, 2), (9, 1)]

# 使用hello函数设定比较的元素；在hello函数里可以随意更改需要比较的函数
def hello(x):   # 这里的x就是arr列表里的一个元组
    # return x[1]
    return max(x)   # 获取元组内最大元素

# 用冒泡模拟sorted函数
def sorted1(arr, key, reverse=False):  # reverse默认是True，True意即倒序排序，False意即顺序排序
    for i in range(0, len(arr)):
        for j in range(0, len(arr)-1-i):
            if key(arr[j]) > key(arr[j+1]):  # 这里的key是调用了hello函数
                arr[j], arr[j+1] = arr[j+1], arr[j]
    if reverse == True:
        arr = arr[::-1]
    return arr

# 使用python自带函数sorted方法：
print '方法2，用排序函数sorted实现：%s ' % sorted(arr, key=hello)  


