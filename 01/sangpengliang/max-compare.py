#encoding: utf-8

chars = [1,2,3,2,12,3,1,3,21,2,2,3,4111,22,3333,444,111,4,5,777,65555,45,33,45]
#a = 0
a = chars[0]
for c in chars:
	if a > c:
		a = a
	elif a < c :
		a = c
	elif a == c:
		a = a	
print '最大值为：' + str(a)