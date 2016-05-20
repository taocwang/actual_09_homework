# encoding:utf-8

# 根据最大值排序


## 获取列表中每个元组的最大值
def tt(sl):
	maxnum = sl[0]
	for k in sl:
		if k > maxnum:
			maxnum = k
	return maxnum

# 通过tt函数获取元组中的最大值进行比较，然后把元组对调
def SortList(sl):
	for i in range(len(sl)):
		for i in range(len(sl) -1):
			if tt(sl[i]) > tt(sl[i+1]):
				sl[i],sl[i+1] = sl[i+1],sl[i]

	return sl

sl = [(1,4),(5,1),(2,3)]
print SortList(sl=sl)


'''
def tt(sl):
	maxnum = sl[0]
	for k in sl:
		if k > maxnum:
			maxnum = k
	return maxnum

sl = [(1,4),(5,1),(2,3)]
a = sorted(sl,key=lambda x:tt(x))
print a
'''