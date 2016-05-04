#encoding: utf-8

while True:
	ss = raw_input('please input 年数：')
	if ss == 'quit':
		break
	ss = int(ss)	
	if ss % 100 == 0 and ss % 400 == 0:
		print '%s 是闰年' % ss
	elif ss %100 !=0 and ss %4 == 0:
		print '%s 是闰年' % ss
	else:
		print '%s 不是闰年' % ss
