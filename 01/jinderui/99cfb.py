#!/usr/bin/env python

# encoding: utf-8

for i in range(1,10):
    for j in range(1,10):
        if j <=i:
            print "%s * %s =  %s " %(j,i,j*i),
	print ""