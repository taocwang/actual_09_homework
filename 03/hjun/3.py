#!/usr/bin/env python
#-*-coding: UTF-8-*-
path = 'www_access_20140823.log'
path2 = 'www_access_20140823.log.bak'
x = 5242880
rh = open(path,'r')
wh = open(path2,'w')
while True:
	y = rh.read(x)
	if y:
		wh.write(y)
	else:
		break

wh.close()
rh.close()


'''
功能ok，后续写代码的时候注意变量的命名，可以起一个比较见名知意的名字，比如代码的x=>buffer_size
'''
