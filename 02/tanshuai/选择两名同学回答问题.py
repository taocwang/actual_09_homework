#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
思路：
1、获取列表索引值
2、通过random.randint(0,_index)，得出需要弹出的元素
3、list.pop弹出元素：第一个同学的名字出来

4、通过random.randint(0,_cont)，得出需要弹出的元素
5、list.pop弹出元素：第二个同学的名字出来

6、打印两个同学的名字：
'''
import random
num_list = ['靳德瑞', '祁成', '鲍鹏飞', '佘朝辉', '常华伟', '崔佳', '赵云海', '谭帥','李续', '郭云飞', '周福成', '桑鹏亮','赵勇']

_index = len(num_list)
print "第一个回答问题的同学是：%s" % num_list.pop(random.randint(0, _index) - 1)
print "第二个回答问题的同学是：%s" % num_list.pop(random.randint(0, _index) - 2)

# KK老师，我知道这个程序比较low逼，后期等学完文件操作，我再优化优化哈！
# 目前知道的有一个问题是：1、pop弹出的值，如果是负数，程序就会报错；
#                         2、被处理过后的列表不能持久化，等后续学文件操作后，将处理的结果直接写入文件里，应该能解决；
#                         3、其他的问题，还望老师给予指点！