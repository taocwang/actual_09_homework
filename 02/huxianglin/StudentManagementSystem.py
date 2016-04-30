#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

class AddStudent(object):
    def AddStudent(self,FileName):
        print '''使用帮助：
        添加学员学号必须唯一，且为数字，可以一次性输入该多次课程成绩，多次课程成绩之间使用英文逗号（,）分隔！
        退出添加学生请输入exit
        '''
        GetData=IOJsonFile()
        Data=GetData.ReadJson(FileName)
        while True:
            ID={}
            print '当前系统中学号与姓名如下，新加入学员学号需要保持唯一性：'
            for i in Data.keys():
                print i,Data[i]['name']+' ',
            print ''
            Id=raw_input('请输入学号：').strip()
            if Id=='exit':
                break
            else:
                if int(Id) in [int(i) for i in Data.keys()]:
                    print '抱歉，输入学员学号和系统中的学号重复，请重新输入！'
                    continue
            Name=raw_input('请输入姓名：')
            if Name.strip()=='exit':
                break
            else:
                ID['name']=Name.strip()
            Sex=raw_input('请输入性别：')
            if Sex.strip()=='exit':
                break
            else:
                ID['sex']=Sex.strip()
            Age=raw_input('请输入年龄：').strip()
            if Age=='exit':
                break
            else:
                ID['age']=int(Age)
            Results=raw_input('请输入该学员每次课程成绩，每次课程成绩之间用,分隔（英文的逗号）:').strip()
            if Results=='exit':
                break
            else:
                ResultsList=[int(i) for i in Results.split(',')]
                print ResultsList
            for i in range(1,len(ResultsList)+1):
                if len(ResultsList)== 0:
                    break
                ID['result'+str(i)]=ResultsList[i-1]
            Data[int(Id)]=ID
        SaveData=IOJsonFile()
        Flag=SaveData.WriteJson(Data,FileName)
        if Flag:
            print '保存成功'
class DelStudent(object):
    def DelStudent(self,FileName):
        GetDate=IOJsonFile()
        Data=GetDate.ReadJson(FileName)
        print '退出删除学生请输入exit'
        while True:            
            print '当前系统中学号与姓名对应如下：'
            for i in Data.keys():
                print i,Data[i]['name']+' ',
            print ''
            ID=raw_input('请输入想删除学生的 学号：').strip()
            if ID=='exit':
                break
            else:
                if int(ID) in [int(i) for i in Data.keys()]:
                    del Data[ID]
                else:
                    print '抱歉，输入的学生ID不在系统中！'
                    continue
        SaveData=IOJsonFile()
        Flag=SaveData.WriteJson(Data,FileName)
        if Flag:
            print '保存成功'          
class ChangeStudent(object):
    def ChangeStudent(self,FileName):
        GetDate=IOJsonFile()
        Data=GetDate.ReadJson(FileName)
        print '退出修改学生信息请输入exit'
        while True:            
            print '当前系统中学号与姓名对应如下：'
            for i in Data.keys():
                print i,Data[i]['name']+' ',
            print ''
            ID=raw_input('请输入想修改学生的 学号：').strip()
            if ID=='exit':
                break
            else:
                if int(ID) not in [int(i) for i in Data.keys()]:
                    print '抱歉，输入学员学号和不在系统中，请重新输入！'
                    continue
            Name=raw_input('请输入姓名：').strip()
            if Name.strip()=='exit':
                break
            else:
                Data[ID]['name']=Name
            Sex=raw_input('请输入性别：').strip()
            if Sex=='exit':
                break
            else:
                Data[ID]['sex']=Sex
            Age=raw_input('请输入年龄：').strip()
            if Age=='exit':
                break
            else:
                Data[ID]['age']=int(Age)
            Results=raw_input('请输入该学员每次课程成绩，每次课程成绩之间用,分隔（英文的逗号）：').strip()
            if Results=='exit':
                break
            else:
                ResultsList=[int(i) for i in Results.strip().split(',')]
            for i in range(1,len(ResultsList)+1):
                Data[ID]['result'+str(i)]=ResultsList[i-1]            
        SaveData=IOJsonFile()
        Flag=SaveData.WriteJson(Data,FileName)
        if Flag:
            print '保存成功'
class SearchStudent(object):
    def SearchStudent(self,FileName):
        GetDate=IOJsonFile()
        Data=GetDate.ReadJson(FileName)
        print '退出查找学生信息请输入exit'
        while True:
            print '当前系统中学号与姓名对应如下：'
            for i in Data.keys():
                print i,Data[i]['name']+' ',
            print ''
            ID=raw_input('请输入想查找学生的 学号：').strip()
            if ID=='exit':
                break
            else:
                if int(ID) not in [int(i) for i in Data.keys()]:
                    print '抱歉，输入学员学号和不在系统中，请重新输入！'
                    continue
            print '学号：%s 姓名：%s 性别：%s 年龄：%s ' %(ID,Data[ID]['name'],Data[ID]['sex'],Data[ID]['age'])
            ResultList=[]
            for i in Data[ID].keys():
                if 'result' in i:
                    ResultList.append(int(i.split('result')[1]))
            ResultList.sort()
            for i in ResultList:
                print '第%s次课的成绩：%s' %(i,Data[ID]['result'+str(i)])
class SortStudent(object):
    def SortStudent(self,FileName):
        GetDate=IOJsonFile()
        Data=GetDate.ReadJson(FileName)
        print '退出学生信息排序请输入exit'
        while True:
            Operation=raw_input('请输入排序方式，ID基于学号排序，AGE基于年龄排序，Result基于课程成绩排序：').strip()
            if Operation=='exit':
                break
            elif Operation=='ID':
                IDList=[int(i) for i in Data.keys()]
                IDList.sort()
                print '基于学号排序结果如下：'
                for i in IDList:
                    print '学号：%s 姓名：%s 性别：%s 年龄：%s ' %(i,Data[str(i)]['name'],Data[str(i)]['sex'],Data[str(i)]['age']),
                    ResultList=[]
                    for j in Data[str(i)].keys():
                        if 'result' in j:
                            ResultList.append(int(j.split('result')[1]))
                            ResultList.sort()
                    for Result in ResultList:
                        print '第%s次课的成绩：%s ' %(Result,Data[str(i)]['result'+str(Result)]),
                    print ''
            elif Operation=='AGE':
                DataSorted=sorted(Data.iteritems(),key=lambda x:x[1]['age'])
                for i in DataSorted:
                    print '学号：%s 姓名：%s 性别：%s 年龄：%s ' %(i[0],i[1]['name'],i[1]['sex'],i[1]['age']),
                    ResultList=[]
                    for j in i[1].keys():
                        if 'result' in j:
                            ResultList.append(int(j.split('result')[1]))
                            ResultList.sort()
                    for Result in ResultList:
                        print '第%s次课的成绩：%s ' %(Result,i[1]['result'+str(Result)]),
                    print ''
            elif Operation=='Result':
                ResultNum=raw_input('请输入按第几次课成绩排序：').strip()
                if ResultNum=='exit':
                    break
                Flag=False
                for i in Data.values():
                    if 'result'+ResultNum in i.keys():
                        Flag=True
                if Flag:
                    DataSorted=sorted(Data.iteritems(),key=lambda x:x[1]['result'+ResultNum],reverse=True)
                    for i in DataSorted:
                        print '学号：%s 姓名：%s 性别：%s 年龄：%s ' %(i[0],i[1]['name'],i[1]['sex'],i[1]['age']),
                        ResultList=[]
                        for j in i[1].keys():
                            if 'result' in j:
                                ResultList.append(int(j.split('result')[1]))
                                ResultList.sort()
                        for Result in ResultList:
                            print '第%s次课的成绩：%s ' %(Result,i[1]['result'+str(Result)]),
                        print ''
                else:
                    print '抱歉，第%s节课成绩还未出来。。。' %(ResultNum)
                    continue                
class IOJsonFile(object):
    def ReadJson(self,FileName):
        Data=json.load(open(FileName, 'r'),encoding='utf-8')#Utf-8编码,encoding='utf-8'
        return Data
    def WriteJson(self,Data,FileName):
        json.dump(Data,open(FileName, 'w'),ensure_ascii=False)#ensure_ascii=False是为了解决文件中文乱码问题。json.dumps在默认情况下，对于非ascii字符生成的是相对应的字符编码，而非原始字符。
        return True

if __name__ == "__main__":
#     Data={1:{'name':'胡湘林','sex':'男','age':24}}
#     test=IOJsonFile()

#     test.WriteJson(Data, 'test.json')
#     Data1=test.ReadJson('test.json')
#     print type(Data1['01']['age'])
    FileName='test.json'
    AddStudent=AddStudent()
    DelStudent=DelStudent()
    ChangeStudent=ChangeStudent()
    SearchStudent=SearchStudent()
    SortStudent=SortStudent()
    print '*'*40
    print '*'+' '*38+'*'
    print '*'+' '*7+'欢迎来到学生信息管理系统'+' '*23+'*'
    print '*'+' '*38+'*'
    print '*'*40
    print '''使用帮助：
        增加学生信息，请使用add；
        删除学生信息，请使用del；
        修改学生信息，请使用change；
        查询学生信息，请使用search；
        给学生排序，请使用sort；
        退出系统，请使用exit''' 
    while True:
        Oper=raw_input('请输入想要执行的操作：').strip()
        if Oper=='exit':
            print 'Bye Bye......'
            break
        if Oper=='add':
            AddStudent.AddStudent(FileName)
        elif Oper=='del':
            DelStudent.DelStudent(FileName)
        elif Oper=='change':
            ChangeStudent.ChangeStudent(FileName)
        elif Oper=='search':
            SearchStudent.SearchStudent(FileName)
        elif Oper=='sort':
            SortStudent.SortStudent(FileName)
        else:
            print '您没有按照要求输入，请重新输入！'
            continue