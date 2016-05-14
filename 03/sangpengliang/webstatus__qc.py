#!/usr/bin/env python
#_*_coding:utf-8_*_
logpath = 'D:\/python\/nginx_log\/access.log'

web_status = {}
f = open( logpath,  'r')
for i in f:
    flist = i.split()
    web_status[(flist[0], flist[6], flist[8])] = web_status.get((flist[0], flist[6], flist[8]),0) + 1

Ngx_list = web_status.items()

Ngx_dic = sorted(Ngx_list, key=lambda x:x[1], reverse = True)

for i in range(1,11):
    print "排名%s: 访问IP：%s, 访问文件：%s，访问状态：%s，访问次数：%s;" %(i, Ngx_dic[i][0][0], Ngx_dic[i][0][1], Ngx_dic[i][0][2], Ngx_dic[i][1])
