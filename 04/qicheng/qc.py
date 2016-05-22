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

<<<<<<< HEAD

=======
def local_sorted(x):
	for i in x:
		a = x[0]
		if i > a:
			a = i
	return a
def local_comp(y):
	for iii in range(0,len(y) -1):
		for ii in range(0,len(y) -1):
			if local_sorted(y[ii]) > local_sorted(y[ii + 1]):
				y[ii],y[ii + 1] = y[ii + 1],y[ii]
	return y

y = [(2,4,9),(5,1,3),(2,3,4)]
print local_comp(y)

'''
加油，功能逻辑有点问题，可以多思考下
1. local_sorted函数是干嘛的？如果参数传递为(5, 1, 3)， 返回的结果是不是你想要的
'''
>>>>>>> 671ca84665f10647e379b92ef67f7b0894bcd079
