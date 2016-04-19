#!/usr/bin/env python
# encoding: utf-8
l1 = [2,3,2,12,3,1,3,21,2,2,3,4111,22,3333,444,111,4,5,777,65555,45,33,45]
init_number = None

for i in l1:
    if i > init_number:
        init_number = i


print "第一个最大值是：%s" %(init_number)


init2_number = None
for x in l1:
   if x > init2_number and x != init_number:
       init2_number = x

print "第二个最大值是：%s" %(init2_number)
    
