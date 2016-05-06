#encoding: utf-8

total = 0
value = 0
i = 0 
#i = i + 1
while value != 'pc':
	value = raw_input('input a num:')
	if value != 'pc':
		i = i + 1
		total += int(value)
if i == 0:
	print 'total:%s,avg:0' % total
else:
	print 'total:%s, avg:%s' % (total ,total * 1.0 / i)
