#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 要求：[1,3,5,6,8,9]中找到3
num_list = [1, 3, 5, 6, 8, 9]
find_num = int(raw_input('请输入你要查找的数字：'))
start = 0
end = len(num_list) - 1

while True:
    middle = (start + end) / 2
    if find_num == num_list[middle]:
        print "找到了，索引为：%s" % middle
        break
    elif find_num > num_list[middle]:
        print "在后半段"
        start = middle + 1
    else:
        print "在前半段"
        end = middle - 1
    if start > end:
        print "找不到"
        break
# 没有写出来，查看老师录制的作业视频，跟着老师分析的思路一起写的。
