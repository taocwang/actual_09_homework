#!/usr/bin/env python
# -*- coding: utf-8 -*-
import random
import time

#列表生成函数
def CreateList(Num):
    List=[]
    i=0
    while i < Num:
        List.append(random.randint(1,Num))
        i+=1
    return List
#文件追加
def AddFile(Information,FileName):
    f=open(FileName,'a')
    f.write(str(Information)+'\n')
    f.close
#清空文件
def ClearFile(FileName):
    f=open(FileName,'w')
    f.close()
#时间计算
def CalaulateteTime(Num,FileName):
    ClearFile(FileName)
    #系统内置排序
    List=CreateList(Num)
    TimeStart=time.time()
    List.sort()
    TimeStop=time.time()
    AddFile('系统内置排序：\n时间：'+str(TimeStop-TimeStart)+'\n'+str(List), str(FileName))
    #冒泡排序
    List=CreateList(Num)
    TimeStart=time.time()
    MaoPaoSort(List)
    TimeStop=time.time()
    AddFile('冒泡排序：\n时间：'+str(TimeStop-TimeStart)+'\n'+str(List), str(FileName))
    #冒泡排序改进
    List=CreateList(Num)
    TimeStart=time.time()
    MaoPaoOptimizeSort(List)
    TimeStop=time.time()
    AddFile('冒泡排序改进，双向排序：\n时间：'+str(TimeStop-TimeStart)+'\n'+str(List), str(FileName))
    #插入排序
    List=CreateList(Num)
    TimeStart=time.time()
    ChaRuSort(List)
    TimeStop=time.time()
    AddFile('插入排序：\n时间：'+str(TimeStop-TimeStart)+'\n'+str(List), str(FileName))
    #希尔排序
    List=CreateList(Num)
    TimeStart=time.time()
    XiErSort(List)
    TimeStop=time.time()
    AddFile('希尔排序：\n时间：'+str(TimeStop-TimeStart)+'\n'+str(List), str(FileName))
    #归并排序
    List=CreateList(Num)
    TimeStart=time.time()
    GuiBing=GuiBingSort()
    List=GuiBing.GuiBingSort(List)
    TimeStop=time.time()
    AddFile('归并排序：\n时间：'+str(TimeStop-TimeStart)+'\n'+str(List), str(FileName))
    #快速排序
    List=CreateList(Num)
    TimeStart=time.time()
    KuaiSuSort(List, 0, len(List)-1)
    TimeStop=time.time()
    AddFile('快速排序：\n时间：'+str(TimeStop-TimeStart)+'\n'+str(List), str(FileName))
#列表排序
#1冒泡排序
def MaoPaoSort(List):
    for i in range(0,len(List)-1):
        for j in range(i+1,len(List)):
            if List[i]>List[j]:
                List[i],List[j]=List[j],List[i]
    return List
#2冒泡排序的改进（双向排序）   
def MaoPaoOptimizeSort(List):
    for i in range(0,len(List)/2):
        for j in range(i,len(List)-i-1):
            if List[i]>List[j]:
                List[i],List[j]=List[j],List[i]
            if List[j]>List[-i-1]:
                List[j],List[-i-1] = List[-i-1],List[j]
    return List
#插入排序    
def ChaRuSort(List):
    for i in range(1,len(List)):
        j=i
        while j>0 and List[j-1]>List[i]:
            j-=1
        List.insert(j, List.pop(i))
    return List
#希尔排序    
def XiErSort(List):
    grep = len(List)/2
    while grep > 0:
        for i in range(grep,len(List)):
            j=i
            while j>=grep and List[j-grep]>List[i]:
                List[j-grep],List[j]=List[j],List[j-grep]
                j-=grep
        grep=grep/2
    return List
#归并排序    
class GuiBingSort(object):
    def MergeTwoList(self,List1,List2):
        i,j,tmp=0,0,[]
        while i<len(List1) and j<len(List2):
            if List1[i]<=List2[j]:
                tmp.append(List1[i])
                i+=1
            else:
                tmp.append(List2[j])
                j+=1
        tmp.extend(List1[i:])
        tmp.extend(List2[j:])
        return tmp
    def GuiBingSort(self,List):
        if len(List)<=1:
            return List
        List1=self.GuiBingSort(List[:len(List)/2])
        List2=self.GuiBingSort(List[len(List)/2:])
        return self.MergeTwoList(List1, List2)
#快速排序
def Partition(List, low, high):  
    tmp = List[low]  
    while low < high:  
        while low < high and List[high] >= tmp:  
            high = high - 1  
        List[low] = List[high]   
        while low < high and List[low] <= tmp:  
            low = low + 1    
        List[high] = List[low]   
    List[low] = tmp  
    return low  
def KuaiSuSort(List,low,high): 
    if low < high:  
        pivotpos = Partition(List, low, high)  
        KuaiSuSort(List, low, pivotpos - 1)  
        KuaiSuSort(List, pivotpos + 1, high)
        
if __name__ == "__main__":
    CalaulateteTime(10000, 'test.txt')
    print 'calculate is successful,the file is test.txt'