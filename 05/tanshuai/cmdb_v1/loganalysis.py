#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 1、统计：获取访问信息并统计出现次数
def get_topn(log_files, topn=10):
    rt_dict = {}
    log_files = open(log_files, 'r')
    while True:
        # 读取文件
        line = log_files.readline()
        if not line:
            break
        # 获取ip，url，status信息
        nodes = line.split()
        (ip,url,status) = nodes[0],nodes[6],nodes[8]
        if (ip,url,status) not in rt_dict:
            rt_dict[(ip,url,status)] = 1
        else:
            rt_dict[(ip,url,status)] += 1
    log_files.close()
    # print rt_dict

    # 2、转换成list，方便排序
    rt_list = rt_dict.items()

    # 3、排序出topn访问信息
    for j in range(0, topn):
        for i in range(0, len(rt_list) - 1):
            if rt_list[i][1] > rt_list[i + 1][1]:
                rt_list[i], rt_list[i + 1] = rt_list[i + 1], rt_list[i]
    return rt_list[-1:-(topn + 1):-1]


if __name__ == "__main__":
    log_files = 'access.txt'
    print get_topn(log_files=log_files, topn=20)

