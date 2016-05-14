#!/usr/bin/env python
# coding=utf-8

from collections import defaultdict
l=[]
k=defaultdict(int)
with open('www_access_20140823.log') as f:
    for line in f:
        k[line.split()[0] + " " + line.split()[6] + " " + line.split()[8]] += 1
l = k.items()
l.sort(key=lambda i: -i[1])
for ll in l[:10]:
    print ll[1], ll[0]

