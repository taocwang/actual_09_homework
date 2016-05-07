#!/usr/bin/env python
# coding=utf-8

def search2(a,m):
    low = 0
    high = len(a) - 1
    while(low <= high):
        mid = (low + high)/2
        midval = a[mid]

        if midval < m:
            low = mid + 1
        elif midval > m:
            high = mid - 1
        else:
            print mid
            return mid
    print -1
    return -1

if __name__ == "__main__":
    a = [1,2,3,4,5,5,6,7]
    m = 5
    search2(a,m)
