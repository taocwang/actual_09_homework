#!/usr/bin/env python
# -*- coding: utf-8 -*-
import time
s = time.time()
# 1、从log里获取出需要的信息访问次数，访问URL，访问状态
# 2、写入文件
# 3、读取文件，拿出去重后的top10访问信息，

# 1.获取文件里的所有日志，放入list里面，方便后面处理
New_logs = []
files = open('www_access_20140823.log', 'rb')
for line in files.readlines():
    New_logs.append(line.rstrip('\n'))       # rstrip 删除读取行后面的换行符号
files.close()
# print New_logs

# 2.将上面得出的结果，转化为dict类型，并统计出IP的访问次数。
files_dict = {}
for i in range(0, len(New_logs)):            # 遍历上面获取到的日志数据，取索引值
    src_list = New_logs[i].split()            # 将数据以list数据类型存入list中
    IP, URL, Status = src_list[0], src_list[6], src_list[8] # 获取所需要的数据：IP URL Status
    key = (IP, URL, Status)                   # 以tuple数据类型加入key中
    files_dict[key] = files_dict.get(key, 0) + 1 # 统计IP出现次数：第一次出现默认设置0，出现一次就+1
# print files_dict

# 3.将上面得出的结果，转化为list类型，list里用tuple类型将访问信息及访问次数包含起来。
rt_list = []
for key, value in files_dict.items():
    rt_list.append((key, value))
# print rt_list

print 'start after:', time.time() - s
# 4. 获取top10访问信息
for j in range(0, 10):                          # 因为我们知道需要top10的信息，所以只需要循环10次即可。
    for i in range(0, len(rt_list) - 1 - j):    # 使用for循环出列表里所有的元素
        if rt_list[i][1] > rt_list[i + 1][1]:   # 取列表的0元素与1元素进行比较
            rt_list[i], rt_list[i + 1] = rt_list[i + 1], rt_list[i]  # 将最大的交换到列表最后面
    # print '访问次数:%s\t访问IP:%-15s\t访问URL:%-50s\t访问状态:%s' % (lt_list[j][1],lt_list[j][0][0],lt_list[j][0][1],lt_list[j][0][2])

lt_list = rt_list[-1:-11:-1]         # 获取top10访问
for j in range(0, 10):
    print '访问次数:%s\t访问IP:%-15s\t访问URL:%-50s\t访问状态:%s' % (lt_list[j][1],lt_list[j][0][0],lt_list[j][0][1],lt_list[j][0][2])

print 'ok:', time.time() - s

'''
说明：
    此作业参考了胡湘林同学的作业思路编写而成。因为自己写确实没有思路，很多知识点在课堂上都学过，但就是整合不到一起！还需要多多练习，多多看别人写的代码。
'''


'''
ok，没问题，自己多练一些，但是要想每一步为什么那么坐，如何优化
改进点
1. line21, 22有什么改进的地方吗？能不能合成一句 key = (list[x], list[y], list[z])呢
2. line28, 29, 结果rt_list和files_dict.items()的结果有什么区别呢? 自己可以尝试下
'''
