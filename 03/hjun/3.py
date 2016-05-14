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


