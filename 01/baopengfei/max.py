#encoding: utf-8

num_list = [1,2,3,2,12,3,1,3,21,2,2,3,4111,22,3333,444,111,4,5,777,65555,45,33,45]


#求第一个最大的值
max_num = None

for i in num_list:
    if max_num is None:
        max_num = i
    elif max_num < i:
            max_num = i

print 'max num is:%s' % max_num

#求第二个最大的值

second_num = None

for i in num_list:
    if second_num is None:
        second_num = i
    elif max_num != i and second_num < i:
            second_num = i

print 'second num is:%s' % second_num
