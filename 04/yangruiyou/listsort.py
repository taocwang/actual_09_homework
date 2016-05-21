#!/usr/bin/env python

def sortlist(listsort):
    for j in range(len(listsort) -1 ):
            for i in range(len(listsort)-1):
                if max(listsort[i]) > max(listsort[i+1]):
                    listsort[i],listsort[i+1] = listsort[i+1],listsort[i]
    return listsort

sort_list=[(1,4),(5,1),(2,3)]

print sortlist(sort_list)
