#/usr/bin/env python
#encondig: UTF-8

for x in range(1,10):
	for y in range(1,x+1):
		z = y * x
		if len(str(z)) == 1:
			print '%s * %s = %s  ' %(y,x,y*x),
		else:
			print '%s * %s = %s ' %(y,x,y*x),
	print '\n'

'''
功能ok，考虑到输出格式的美观，后续介绍字符串课程时可以注意下字符串在格式化方面的一些方法
'''