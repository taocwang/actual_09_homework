#!/usr/bin/env python
#-*-coding: UTF-8-*-

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
