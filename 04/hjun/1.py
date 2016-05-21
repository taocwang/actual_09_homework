#!/usr/bin/env python
#-*-coding: UTF-8-*-
# '''
# 一个list[(1,4),(5,1),(2,3)],根据每个元组中的较大值进行排序
# 期待结果：[(2,3),(1,4),(5,1)]
# '''

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

y = [(1,4,5),(5,1,6),(2,3,8)]
print local_comp(y)


'''
对于示例数list y进行排序没有问题, 但只限定list中的每个元素中最大值在索引为-1位置类型

问题:
1. local_sorted函数逻辑有问题
	可以自己测试下 x = (1, 5, 4)这种情况
	原因：line 10，是不是应该是在第一次将a赋值为x[0]， 而不是每次循环都赋值


扩展思考:
1. 考虑在函数参数传递时对于list类型数据时传址还是传值, 如果local_comp没有返回值, 排序的原始list y是否发生变化

加油
'''
