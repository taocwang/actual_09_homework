#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 使用模板生成html文件展示nginx日志top100，从日志文件读取出数据，然后进行排序，之后读取html的模板文件，使用bootstrap以及表格展示排序获取到的数据
import dbutil
import time
import dbutil

from functools import wraps
def exe_time(func):
    @wraps(func)
    def wrapper(*args):
        start = time.time()
        rt=func(*args)
        print u'使用时间:'+str(time.time()-start)
        return rt
    return wrapper

def ReadFile(FileName):
    f=open(FileName,'r')
    FileList=[]
    for line in f.readlines():
        FileList.append(line.split())
    f.close()
    return FileList
@exe_time
def FilterNginx(SrcFileName):
    FileList=ReadFile(SrcFileName)
    FileDict={}
    for i in range(0,len(FileList)):
        key=(FileList[i][0],FileList[i][6],FileList[i][8])
        FileDict[key]=FileDict.get(key,0)+1
    FilterList=sorted(FileDict.items(),key=lambda x:x[1],reverse=True)
    sql='insert into accesslog(count,ip,url,code) values(%s,%s,%s,%s)'
    count=dbutil.execute_aggregation_sql(sql,FilterList)
    print count
'''
'select * from accesslog order by count desc limit %s使用order by对查询出来的数据进行排序（默认是从小到大排序）
使用desc可将排序结果反转，limit输出排序后的结果的n行，这里面可有两个参数，开始行和结束行，这里只使用了一个参数默认是
从1开始'
'''
@exe_time
def sort_nginx(topn):
    sql='select * from accesslog order by count desc limit %s'
    args=(topn,)
    _count,_rt_list=dbutil.execute_fetch_sql(sql,args)
    rt_list=[]
    if _count:
        for i in range(0,len(_rt_list)):
            rt_list.append(((_rt_list[i][2],_rt_list[i][3],_rt_list[i][4]),_rt_list[i][1]))
        return rt_list
    else:
        return False
if __name__=="__main__":
    FilterNginx('www_access_20140823.log')