# encoding:utf-8

# 根据最大值排序

#方法1
s = [(1,4),(5,1),(2,3)]

lnum = sorted(s,key=lambda j:max(j))
print lnum



#方法2
def ms(sl):
	for i in range(len(sl)):
		for i in range(len(sl) - 1):
			if max(sl[i]) > max(sl[i+1]):
				sl[i],sl[i+1] = sl[i+1],sl[i]

	return sl


sl = s[:]
print ms(sl=sl)

'''
功能ok
扩展思考：
1. 在ms执行完以后, 函数外的sl变了吗？为什么？

'''
