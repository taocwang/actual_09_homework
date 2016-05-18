# encoding:utf-8

# 根据最大值排序

sl = [(1,4),(5,1),(2,3)]


#拿到所有的最大值，放到列表里面
def tt(sl):
	maxnum = []
	for i in range(len(sl)):
		if sl[i][0] > sl[i][1]:
		    maxnum.append(sl[i][0])
		else:
			maxnum.append(sl[i][1])
	return maxnum

maxnum = tt(sl=sl)

#循环比较最大值，如果值maxnum[x]大于maxnum[x+1] 就把最大值和对应的元组都进行调换
def maxList(sl):
	for x in range(len(sl)):
		for x in range(len(maxnum) - 1):
			if maxnum[x] > maxnum[x+1]:
				maxnum[x],maxnum[x+1]=maxnum[x+1],maxnum[x]
				sl[x],sl[x+1] = sl[x+1],sl[x]
	return sl
print maxList(sl)


