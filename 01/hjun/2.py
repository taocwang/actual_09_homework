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
