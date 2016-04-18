# -*- coding: utf-8 -*-
'''
# 作业要求：
一个序列[1,2,3,2,12,3,1,3,21,2,2,3,4111,22,3333,444,111,4,5,777,65555,45,33,45]
求这个list的最大的两个值
'''

'''
解答方法一：（参考同学作业）

num_list = [1, 2, 3, 2, 12, 3, 1, 3, 21, 2, 2, 3, 4111, 22, 3333, 444, 111, 4, 5, 777, 65555, 45, 33, 45]
# 定义两个变量，用于存储第一，第二最大值；
max_num1 = None
max_num2 = None
# 使用for循环，拿出列表里的数据；
for i in num_list:
    # 判断i大于预定义变量max_num1的话，则max_num1 等于 i；
    if i > max_num1:
        # 每一次循环，都会将最大的值存放到 max_num1 变量中；
        max_num1 = i
# 打印max_num1的值
print "第一个最大值为：%s"% max_num1
# 使用for循环，拿出列表数据；
for j in num_list:
    # 判断 j 如果大于 max_num2 和 j 不等于max_num1，则是我们想要的第二个最大值；
    if j > max_num2 and j != max_num1:
        # 将if判断后的结果加到max_num2变量中；
        max_num2 = j
# 打印第二个最大的值
print "第二个最大值为：%s"% max_num2
'''

'''
解答方法二：（参考知乎网：https://www.zhihu.com/question/33559625）
'''
num_list = [1, 2, 3, 2, 12, 3, 1, 3, 21, 2, 2, 3, 4111, 22, 3333, 444, 111, 4, 5, 777, 65555, 45, 33, 45]
num_list.sort()
print "第一个最大值为：%s" % num_list[-1]
print "第二个最大值为：%s" % num_list[-2]

# 此方法有一个缺陷，如果list里有两个65555，则num_list[-2 ]取到的结果还是65555，除非你知道自己要取倒数第几位数字。

