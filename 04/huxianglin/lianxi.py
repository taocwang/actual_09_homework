#!/usr/bin/env python
# -*- coding: utf-8 -*-
import time
# def ReadFile(FileName):
#     f=open(FileName,'r')
#     FileList=[]
#     for line in f.readlines():
#         FileList.append(line.split())
#     f.close()
#     return FileList
# def WriteFile(FileName,List):
#     f=open(FileName,'w')
#     for i in List:
#         f.write(str(i)+'\n')
#     f.close()
# def FilterNginx(SrcFileName,DestFileName):
#     FileList=ReadFile(SrcFileName)
#     FileDict={}
#     for i in range(0,len(FileList)):
#         key=(FileList[i][0],FileList[i][6],FileList[i][8])
#         FileDict[key]=FileDict.get(key,0)+1
#     FilterList=sorted(FileDict.items(),key=lambda x:x[1],reverse=True)
#     WriteFile(DestFileName, FilterList[:10])
# if __name__=="__main__":
#     FilterNginx('www_access_20140823.log','test.txt')

# List=[]
# sum=0.0
# time1=time.time()
# for i in xrange(100001):
#     sum+=time.time()-time1
#     time1=time.time()
#     List.append(i)
#     List.reverse()
# print sum
# 
# List=[]
# sum=0.0
# time1=time.time()
# for i in xrange(100001):
#     sum+=time.time()-time1
#     time1=time.time()
#     List.insert(0, i)
# print sum

# f=open('test.txt','rU') #跨平台自动处理换行符
# print f.read()
# f.close

# 打印文件
# f=open('test.txt','r')
# print f.read()
# f.close()

# 去除换行符
# FileLines=[]
# f=open('test.txt','r')
# for i in f.readlines():
#     FileLines.append(i.strip('\n'))
# f.close()
# f=open('test.txt','w')
# for i in FileLines:
#     f.write(i)
# f.close()

# 替换reboot为hello
# FileLines=[]
# f=open('test.txt','r')
# for i in f.readlines():
#     FileLines.append(i.replace('reboot','hello'))
# f.close()
# f=open('test.txt','w')
# for i in FileLines:
#     f.write(i)
# f.close()

#替换第二行内容为wd
# FileLines=[]
# f=open('test.txt','r')
# FileList=f.readlines()
# for i in range(0,len(FileList)):
#     if i == 1:
#         FileList[i]='wd\n'
#     FileLines.append(FileList[i])
# f.close()
# f=open('test2.txt','w')
# for i in FileLines:
#     f.write(i)
# f.close()

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#异常处理
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# copy_list=[('test1.txt','test2.txt'),('test3.txt','test4.txt')]
# for src,dest in copy_list:
#     sf,df=None,None
#     try:
#         sf=open(src,'r')
#         df=open(dest,'w')
#         size=5
#         while True:
#             cxt=sf.read(size)
#             if not cxt:
#                 break
#             df.write(cxt)
#     except Exception ,e:
#         print 'copy文件失败：%s' %src,e
#     finally:
#         if sf:
#             print '%s关闭' % src
#             sf.close()
#         if df:
#             print '%s关闭' % dest
#             df.close()

# 使用模板生成html文件展示nginx日志top100
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
    FilterNginx('www_access_20140823.log','template.html','lianxi2.html',60)

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#函数
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# def test():
#     for i in range(0,10):
#         print i
# test()

List=[(1,4),(5,1),(2,3)]
print sorted(List, key=lambda x:max(x))
def MaxNum(Tuple):
    MaxNumber=0
    for i in range(0,len(Tuple)-1):
        if Tuple[i]<Tuple[i+1]:
            MaxNumber=i+1
    return Tuple[MaxNumber]
print sorted(List,key=lambda x:MaxNum(x))