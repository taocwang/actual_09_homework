#encoding: utf8

age1 = raw_input('�������һ������ֵ��')
age2 = raw_input('������ڶ�������ֵ��')
max_age = 0
if int(age1) > int(age2):
	max_age = age1
elif age1 == age2:
	max_age = age2
else:
	max_age = age2
print '����������' + max_age