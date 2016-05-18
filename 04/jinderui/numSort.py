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
ms(sl=sl)
print ms(sl=sl)



