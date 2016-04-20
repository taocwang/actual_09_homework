#!/usr/bin/env python
# -*- coding: utf-8 -*-
import random

<<<<<<< HEAD
# #乘法口诀表
# for i in range(1,10):
#     for j in range(1,i+1):
#         print "%s * %s = %s\t" % (j,i,i*j),
#     print
    
class a(object):
    def __init__(self,Number,Name):
        self.Number = Number
        self.Name = Name
        print self.Number,self.Name
    def ChangeName(self,NewName):
        self.Name = NewName
        print "The new name is %s" %(self.Name)
        
class b(a):
    def __init__(self,Number,Name,Address,Sex):
        self.Address = Address
        self.Sex = Sex
        a.__init__(self, Number, Name)
        print self.Address,self.Sex
    def ChangeAddress(self,NewAddress):
        self.Address = NewAddress
        print "The new address is %s" %(self.Address)
        
person1 = b("12345","huxianglin","ShangHai","man")
person1.ChangeName("xianglinhu")
person1.ChangeAddress("ShenZhen")

#判断是不是闰年
# Year=int(raw_input("Please input the year:"))
# if (Year % 100 == 0) and (Year % 400 == 0):
#     print "The %s year is True!" %(Year)
# elif (Year % 100 != 0) and (Year % 4 == 0):
#     print "The %s year is True!" %(Year)
# else:
#     print "The %s year is False!" %(Year)

#插入排序
#插入排序的方法：当i取某个位置的时候，找i前面的第一个比i大的值的位置j,然后把i的值插入到j的位置，然后把i位置的值给丢弃
List = []
for i in range(0,10):
    List.append(random.randint(0,100))
#List = [9,8,7,6,5,4,3,2,1]
for i in range(1,len(List)):
    j=i
    while j>0 and List[j-1]>List[i]:
        j-=1
    List.insert(j, List.pop(i))
    print List

#
=======
#乘法口诀表
for i in range(1,10):
    for j in range(1,i+1):
        print "%s * %s = %s\t" % (j,i,i*j),
    print

'''
功能ok
'''
>>>>>>> 908d393238f3009c0ecd539f73ccb3c96a5e2516
