#!/usr/bin/env python
# -*- coding: utf-8 -*-
def ReadFile():
    files_dict = {}
    files = open('www_access_20140823.log', 'rb')
    for line in files:
        src_list = line.split()
        IP, URL, Status = src_list[0], src_list[6], src_list[8]
        files_dict[(IP, URL, Status)] = files_dict.get((IP, URL, Status), 0) + 1
    files.close()
    return files_dict

def getVal(x):
    return x[1]

num = sorted(ReadFile().items(), key=getVal, reverse=True)[:10]
# print num
# for i in sorted(files_dict.items(), key=getVal, reverse=True)[:10]:
#     num += i
#     print num
for j in range(0, 10):
    print '访问次数:%s\t访问IP:%-15s\t访问URL:%-50s\t访问状态:%s' % (num[j][1],num[j][0][0],num[j][0][1],num[j][0][2])
