#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
通过三个关键字IP，URL和访问状态来对nginx日志进行排序，找出访问次数最高的十个访问记录输出出来
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
'''
def ReadFile(FileName):
    Lines=[]
    f=open(FileName,'r')
    for line in f.readlines():
        Lines.append(line.rstrip('\n'))
    f.close()
    return Lines
def FilterNginx(Lines):
    FilterDict={}
    for i in range(0,len(Lines)):
        LineList=Lines[i].split()
        IP,Url,Status=LineList[0],LineList[6].rstrip('"'),LineList[8]
        Key=(IP,Url,Status)
        FilterDict[Key]=FilterDict.get(Key,0)+1
    FilterList=sorted(FilterDict.items(),key=lambda x:x[1],reverse=True)
    for i in range(0,10):
        print '访问次数:%s\t访问IP:%-15s\t访问URL:%-50s\t访问状态:%s' %(FilterList[i][1],FilterList[i][0][0],FilterList[i][0][1],FilterList[i][0][2])
        
if __name__ == "__main__":
    Lines=ReadFile('www_access_20140823.log')
    FilterNginx(Lines)