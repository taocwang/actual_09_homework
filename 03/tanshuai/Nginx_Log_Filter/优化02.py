#!/usr/bin/env python
# -*- coding: utf-8 -*-
import time
s = time.time()
'''
思路：
1、打开文件，获取并统计ip，url，status出现的次数；
2、排序成list，统计出访问的top10；
3、打印top10
'''

# 1、统计：获取访问信息并统计出现次数
def insethtml(log_files, htmlhandler, topn=10):
    rt_dict = {}
    log_files = open(log_files,'r')
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
    # print rt_list

    print 'start after:', time.time() - s
    # 3、排序出top10访问信息
    dest_file = open('top10.txt', 'w')
    for j in range(0, 10):
        for i in range(0, len(rt_list) - 1):
            if rt_list[i][1] > rt_list[i + 1][1]:
                rt_list[i], rt_list[i + 1] = rt_list[i + 1], rt_list[i]
        top10 = rt_list[-1:-11:-1]
        # print '访问次数:%s\t访问IP:%-15s\t访问URL:%-50s\t访问状态:%s' % (top10[j][1],top10[j][0][0],top10[j][0][1],top10[j][0][2])
        dest_file.write('访问次数:%s\t访问IP:%-15s\t访问URL:%-50s\t访问状态:%s\n' % (top10[j][1],top10[j][0][0],top10[j][0][1],top10[j][0][2]))
    dest_file.close()
    print 'ok:', time.time() - s


    page_tpl = '''<!DOCTYPE html>
    <html>
        <head>
            <meta charset="utf-8"/>
            <title>{title}</title>
        </head>
        <body>
            <table border = "1">
                <thead>
                    {thead}
                </thead>
                <tbody>
                    {tbody}
                </tbody>
            </table>
        </body>
    </html>
    '''
    title = 'TOP %s 访问日志' % topn
    thead = '<th>index</th><th>访问次数</th><th>访问IP</th><th>访问URL</th><th>访问状态</th>'
    tbody = ''
    for j in range(0, topn):
        top10 = rt_list[-1:-(topn + 1):-1]
        tbody += '\t\t\t\t<tr>\n\t\t\t\t\t<td>%s</td><td>%s</td><td>%s</td><td>%s</td><td>%s</td>\n\t\t\t\t</tr>\n' % (j,top10[j][1],top10[j][0][0],top10[j][0][1],top10[j][0][2])

    htmlhandler = open(htmlhandler, 'w')
    htmlhandler.write(page_tpl.format(title=title, thead=thead, tbody=tbody))
    htmlhandler.close()


log_files = 'www_access_20140823.log'
htmlhandler = 'top10.html'

insethtml(topn=5, htmlhandler='top5.html',log_files=log_files)
insethtml(htmlhandler='top10.html', log_files=log_files)
insethtml(log_files=log_files,topn=15, htmlhandler='top15.html')
# insethtml(log_files, 'top20.html', 20)
# insethtml(log_files, 'top30.html', 30)


