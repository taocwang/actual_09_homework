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
'''
冒泡排序原理就是从左到右先找第一个值，然后拿这个值右边的值和它进行比较，假如右边的值比它小，那就将右边的这个值和它进行交换，
这样，就能够将整个列表中最小的值放到最左边，第一次排序完成，之后对第二个数也进行相同的操作，最终整个列表变成有序的。
'''
def MaoPaoSort(List):
    for i in range(0,len(List)-1):
        for j in range(i+1,len(List)):
            if List[i]>List[j]:
                List[i],List[j]=List[j],List[i]
    return List
#2冒泡排序的改进（双向排序）   
'''
冒泡排序的改进其实就是在对第一个值寻找最小值的同时也在对最后一个值寻找最大值，双向寻找，这样，一次排序下来，能得到左右两边两个
排好序的值，这样，总的执行排序的次数将减少一半。
'''
def MaoPaoOptimizeSort(List):
    for i in range(0,len(List)/2):
        for j in range(i,len(List)-i-1):
            if List[i]>List[j]:
                List[i],List[j]=List[j],List[i]
            if List[j]>List[-i-1]:
                List[j],List[-i-1] = List[-i-1],List[j]
    return List
#插入排序    
'''
插入排序的原理就是从第二个值开始，假定这个值的左边都是有序的序列，找到左边的有序序列中，该值应该插入的位置，然后将这个值插入到
相应的位置，使得左边的序列依旧有序，然后将这个值丢弃。这样执行下去，到最后将整个序列形成一个有序的序列。
'''
def ChaRuSort(List):
    for i in range(1,len(List)):
        j=i
        while j>0 and List[j-1]>List[i]:
            j-=1
        List.insert(j, List.pop(i))
    return List
#希尔排序    
'''
在序列中，找到一个中间的位置，然后将该序列分成左右两个序列，再将左边序列第一个值与右边序列第一个值进行比较，如果左边大于右边，则
进行交换，持续下去，将左右两个序列比较完成后，左右两个序列又分别取中间位置，分成4个序列，再分别在这四个序列中取出第一个数，进行比
较，使得四个序列的第一个数是按照从小到大排列的，这样依次下去，直到把四个序列的值都对比完成后，再从这四个序列中再取中间数，将四个
序列拆成八个序列，在进行比较，到最后，拆成的序列数量为原来序列长度的一半的时候，原来序列中奇数位置的值都有序了，偶数位置的值也都
有序了，这时候再进行最后一次比较，拆出的序列数量等于原来序列长度，这时候再经过一次排序，整个序列有序了。
'''
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
'''
归并排序是基于对两个有序序列进行排序变成新的有序序列的方式进行排序的，假如有两个有序序列，从第一个值开始一个一个比较，小的就插入
到新的序列中，并使得其位置加一，最后，两个序列中会有某一个序列还剩下最大值，将该最大值插入到新的序列中就完成了排序。归并排序使用
递归方式将一个序列从中间分成左右两个序列，再将左右两个序列从中间分成四个序列。递归下去最后分到每个序列中只有一个元素，将这个元素
返回，到上一级调用两序列排序方式，将两个值排序，返回新的排序好的序列，就这样一层一层递归上来，最后使得序列有序。该方式是使用空间
换取排序时间的算法。
'''
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
'''
快速排序的原理是在序列中找到一个定位点（一般是第一个点）然后将比这个点的值大的值挪到它的右边比这个值小的值挪到它的左边，最后返回
该点的位置通过递归调用该方法，将序列分成左右两个序列，然后再细分下去，到最后每个序列中只有两个元素，这两个元素被排好序后返回倒上
一层，最后返回的将是排序好的序列。
'''
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