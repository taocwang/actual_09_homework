#!/usr/bin/env python
# -*- coding: utf-8 -*-
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
    sql='truncate table accesslog'
    dbutil.execute_commit_sql(sql)
    sql='insert into accesslog(count,ip,url,code) values(%s,%s,%s,%s)'
    count=dbutil.execute_aggregation_sql(sql,FilterList)
    if count:
        return True
    else:
        return False
