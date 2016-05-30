#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 使用模板生成html文件展示nginx日志top100，从日志文件读取出数据，然后进行排序，之后读取html的模板文件，使用bootstrap以及表格展示排序获取到的数据
def ReadFile(FileName):
    f=open(FileName,'r')
    FileList=[]
    for line in f.readlines():
        FileList.append(line.split())
    f.close()
    return FileList
def FilterNginx(SrcFileName,Num):
    FileList=ReadFile(SrcFileName)
    FileDict={}
    for i in range(0,len(FileList)):
        key=(FileList[i][0],FileList[i][6],FileList[i][8])
        FileDict[key]=FileDict.get(key,0)+1
    FilterList=sorted(FileDict.items(),key=lambda x:x[1],reverse=True)
    return FilterList[:Num]
