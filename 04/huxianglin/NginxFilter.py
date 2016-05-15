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
def WriteFile(FileName,Details):
    f=open(FileName,'w')
    f.write(Details)
    f.close()
def FilterNginx(SrcFileName,TemFile,DestFileName,Num):
    FileList=ReadFile(SrcFileName)
    FileDict={}
    for i in range(0,len(FileList)):
        key=(FileList[i][0],FileList[i][6],FileList[i][8])
        FileDict[key]=FileDict.get(key,0)+1
    FilterList=sorted(FileDict.items(),key=lambda x:x[1],reverse=True)
    TemFile=open(TemFile,'r')
    PageTem=TemFile.read()
    title='TOP%s访问日志' %Num
    thread='<th>IP</th><th>访问URL</th><th>状态码</th><th>访问次数</th>'
    tbody=''
    for node in range(0,Num):
        tbody+='\n\t\t<tr class="info">\n\t\t\t<th>%s</th>\n\t\t\t<th>%s</th>\n\t\t\t<th>%s</th>\n\t\t\t<th>%s</th>\n\t\t</tr class="info">' %(FilterList[node][0][0],FilterList[node][0][1],FilterList[node][0][2],FilterList[node][1])
    WriteFile(DestFileName, PageTem.format(title=title, thread=thread,tbody=tbody))
if __name__=="__main__":
    FilterNginx('www_access_20140823.log','template.html','lianxi2.html',100)