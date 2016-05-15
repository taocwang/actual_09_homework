#!/usr/bin/env python
#_*_coding:utf-8_*_

fpath = '/Users/yhzhao/Downloads/www_access_20140823.log'

Ngx_cnt = {}

f = open(fpath, 'r')
for i in f:
    flist = i.split()
    #print flist
    Ngx_cnt[(flist[0], flist[6], flist[8])] = Ngx_cnt.get((flist[0], flist[6], flist[8]),0) + 1
    #print "访问IP：%s，访问文件：%s, 返回状态: %s" %(flist[0], flist[6], flist[8])

Ngx_list = Ngx_cnt.items()

#全部排序后取访问次数最高的10个
# for i in range(len(Ngx_list) - 1):
#     for j in range(len(Ngx_list) - 1 - i):
#         if Ngx_list[j][1] > Ngx_list[j + 1][1]:
#             Ngx_list[j], Ngx_list[j+1] = Ngx_list[j+1], Ngx_list[j]

#最排访问次数最高的10个，然后返回后10个
# for i in range(11):
#     for j in range(len(Ngx_list) - 1 - i):
#         if Ngx_list[j][1] > Ngx_list[j + 1][1]:
#             Ngx_list[j], Ngx_list[j+1] = Ngx_list[j+1], Ngx_list[j]

# Ngx_top10 = Ngx_list[-1:-11:-1]
# j = 1
# for i in Ngx_top10:
#     print "排名%s: 访问IP：%s, 访问文件：%s，访问状态：%s，访问次数：%s;" %(j, i[0][0], i[0][1], i[0][2], i[1])
#     j += 1

#python 字典排序
Ngx_dic = sorted(Ngx_list, key=lambda x:x[1], reverse = True)
 
for i in range(1,11):
    print "排名%s: 访问IP：%s, 访问文件：%s，访问状态：%s，访问次数：%s;" %(i, Ngx_dic[i][0][0], Ngx_dic[i][0][1], Ngx_dic[i][0][2], Ngx_dic[i][1])



'''
功能ok，加油
'''
