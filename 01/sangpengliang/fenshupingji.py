#encoding: utf-8

fenshu = raw_input('请输入一个数字:')
fenshu = int(fenshu)
if fenshu < 60 and fenshu >= 0:
	print '不及格'
elif fenshu >= 60 and fenshu <70:
	print '一般'
elif fenshu >=70 and fenshu < 80:
	print '良好'
elif fenshu >=80 and fenshu < 90:
	print '优良'
elif fenshu >=90 and fenshu <= 100:
	print '优秀'
else:
	 print '你输入的有误'