#!/usr/bin/env python
# -*- coding: utf-8 -*-
import random

names=['woniu','wd','kk']
# name = raw_input("please input your name:")
# Tag=False
# for i in names:  
#     if name == i:
#         print "the name %s is in the list!" %(name)
#         Tag=True
#         break
#     elif (Tag==False) and (i==names[-1]):
#         print "can't find the name %s" %(name)
# num=dict
# for i in names*2:
#     num.update(num[i]+1)
#     
# print num

# works=[]
# while True:
#     op=raw_input('please input what you want:add,do or exit:')
#     if op.strip() == 'add':
#         while True:
#             work=raw_input('please input your work:')
#             if not work.strip():
#                 print "you not input your work ,please input again:"
#             else:
#                 works.append(work.strip())
#                 break
#     elif op.strip() == 'do':
#         if len(works)==0:
#             print "the worker is down,please input add"
#             continue
#         print works.pop(0)
#     elif op.strip() == 'exit':
#         if len(works)==0:
#             print "the workers is down,will exit."
#             break
#         else:
#             print "the still have work do not work,please worked it."
#             continue
#     else:
#         print"your input is wrang,please input again!"
        
        
# a=['a','b','c','d','e','f']
# for i in range(0,len(a)/2):
#     a[i],a[-1-i]=a[-1-i],a[i]
#     
# print a

#去重
# List=[1,2,3,4,2,12,3,14,3,2,12,3,14,3,21,2,2,3,4111,22,3333,4]
# arr1 = [1,2,3,4,2,12,3,14,3,2,12,3,14,3,21,2,2,3,4111,22,3333,4]
# arr2 = [2,1,3,2,43,234,454,452,234,14,21,14]
# arr3 = lambda arr1,arr2:list(set(arr1) & set(arr2))
# print arr3(arr1,arr2)
# print list(set(arr1) & set(arr2))
# List2 = []
# for i in List:
#     if i in List2:
#         pass
#     else:
#         List2.append(i)
# print List2

#列表排序
 #1冒泡排序
# List = [179, 178, 175, 173, 169, 168, 165]
# for i in range(0,len(List)-1):
#     for j in range(i+1,len(List)):
#         if List[i]>List[j]:
#             List[i],List[j]=List[j],List[i]
#     print List
# print List

 #2冒泡排序的改进（双向排序）
# List = [179, 178, 175, 173, 169, 168, 165]
# for i in range(0,len(List)/2):
#     for j in range(i,len(List)-i-1):
#         if List[i]>List[j]:
#             List[i],List[j]=List[j],List[i]
#         if List[j]>List[-i-1]:
#             List[j],List[-i-1] = List[-i-1],List[j]
#     print List
# print List


#插入排序
#插入排序的方法：当i取某个位置的时候，找i前面的第一个比i大的值的位置j,然后把i的值插入到j的位置，然后把i位置的值给丢弃
# List = []
# for i in range(0,10):
#     List.append(random.randint(0,100))
# #List = [9,8,7,6,5,4,3,2,1]
# for i in range(1,len(List)):
#     j=i
#     while j>0 and List[j-1]>List[i]:
#         j-=1
#     List.insert(j, List.pop(i))
#     print List


#希尔排序
# List = []
# for i in range(0,20):
#     List.append(random.randint(0,100))
# grep = len(List)/2
# while grep > 0:
#     for i in range(grep,len(List)):
#         j=i
#         tmp=List[i]
#         while j>=grep and List[j-grep]>tmp:
#             List[j-grep],List[j]=List[j],List[j-grep]
#             j-=grep
#     grep=grep/2
#     print List
# print List
  
