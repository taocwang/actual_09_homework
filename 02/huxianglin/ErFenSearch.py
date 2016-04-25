#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
二分查找法查找有序列表
'''
import random

def CreateList(Num):
    List=[]
    i=0
    while i < Num:
        List.append(random.randint(1,Num))
        i+=1
    return List
def ErFenserach(List,Num):
    low,high=0,len(List)-1
    while low<=high:
        i=(low+high)/2
        if Num > List[i]:
            low=i+1
        elif Num < List[i]:
            high=i-1
        elif List[i] == Num:
            return i
    return False
if __name__ == "__main__":
    List=CreateList(10)
    List.sort()
    while True:
        Num=raw_input('Please input you want to search number,if you want to exit,please input exit:')
        if Num.strip() == 'exit':
            print 'Bye Bye......'
            break
        Flag=ErFenserach(List, int(Num.strip()))
        if Flag == False:
            print 'Sorry,your input number %s not in the list!' %(Num)
        else:
            print 'Cangraturation,your input number %s in the list,the location is %s' %(Num,Flag)
            print 'The list is :\n%s' %(List)