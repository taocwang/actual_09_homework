#encoding: utf8

age1 = raw_input('请输入第一个年龄值：')
age2 = raw_input('请输入第二个年龄值：')
max_age = 0
if int(age1) > int(age2):
	max_age = age1
elif age1 == age2:
	max_age = age2
else:
	max_age = age2
print '最大的年龄是' + max_age