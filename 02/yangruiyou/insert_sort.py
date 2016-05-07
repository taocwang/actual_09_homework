#!/bin/env python

def insert_sort(vlist):
    list_len = len(vlist)
    for i in range(1,list_len):
        key = vlist[i]
        for j in range(1,i+1)[::-1]:
            vlist[j] = vlist[j-1]
            vlist[j-1]=key
    return vlist

list1 = [59,12,20,16,33]
print insert_sort(list1)


