#encoding: utf-8

age1 = raw_input('请输入第一个人的年龄：')
age2 = raw_input('请输入第二个人的年龄：')

if int(age1) > int(age2):
	print age1
	print '前面大'
if int(age1) < int(age2):
	print age2
	print '后面大'
if int(age1) == int(age2):
	print age1
	print '一样大'
