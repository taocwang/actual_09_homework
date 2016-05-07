#!/bin/env python

list1 = [1,3,5,6,8,9]

def bsearch(vlist,value):
    low,high = 0,len(vlist) - 1
    print len(vlist)
    while low <= high:
        mid = (low + high)/2
        if vlist[mid] < value:
            low = mid + 1
        elif vlaue < vlist[mid]:
            high = mid - 1
        else:
            return mid
    return -1

print bsearch(list1,3)
