#!/usr/bin/env python
#-*-coding: UTF-8 -*-
temp = []
log = {}
temp2 = []
path='www_access_20140823.log'
rh = open(path,'r')
for rf in rh:
	x = (rf.split(' ')[0], rf.split(' ')[6], rf.split(' ')[8])
	if x in log:
		log[x] += 1
	else:
		log[x] = 1
rh.close()

for y,z in log.items():
	temp2.append((y,int(z)))

for ii in range(0,11):
	for i in range(0,len(temp2) - 1 - ii):
		if temp2[i][1] > temp2[i + 1][1]:
			temp2[i],temp2[i + 1] = temp2[i + 1],temp2[i]
for i in temp2[:-11:-1]:
	print '访问IP为:%-20s' %i[0][0] + '访问URL为:%-50s' % i[0][1] + '访问状态为:%-9s' % i[0][2] + '访问次数为:%s' % i[1]


'''
ok，功能实现ok
可以考虑这几个地方的优化
1. line9: 可以考虑split一次
2. line10~13: 功能ok，可以考虑setdefault的方式或者，get(key, [value])的方式（多考虑几种实现方式，熟练后可以使用最简单的方式）
3. line16~line17: 这个结果temp2和log.items()返回的结果是一样的
'''
