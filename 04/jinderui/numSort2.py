# encoding:utf-8

# 根据最大值排序

#拿到所有的最大值，放到列表里面
def tt(sl):
	maxnuml = []
	for k,v in sl:
		if k > v:
			maxnuml.append(k)
		else:
			maxnuml.append(v)

	return maxnuml

sl = [(1,4),(5,1),(2,3)]

#循环比较最大值，如果值maxnum[x]大于maxnum[x+1] 就把最大值和对应的元组都进行调换
maxnum = tt(sl=sl)
def maxList(sl):
	for x in range(len(sl)):
		for x in range(len(maxnum) - 1):
			if maxnum[x] > maxnum[x+1]:
				maxnum[x],maxnum[x+1]=maxnum[x+1],maxnum[x]
				sl[x],sl[x+1] = sl[x+1],sl[x]
	return sl
print maxList(sl)

'''
功能ok， 加油
'''
