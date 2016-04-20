#!/usr/bin/env python
# -*- coding: utf-8 -*-

#乘法口诀表
for i in range(1,10):
    for j in range(1,i+1):
        print "%s * %s = %s\t" % (j,i,i*j),
    print