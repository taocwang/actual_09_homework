#!/usr/bin/env python
#encoding:utf-8

list_09=[1,2,3,2,12,3,1,3,21,2,2,3,4111,22,3333,444,111,4,5,777,65555,45,33,45]
for i in range(0,len(list_09)):
    for j in range(i+1,len(list_09)):
        a=list_09[i]
        b=list_09[j]
        if a<b:
            list_09[i]=b
            list_09[j]=a
print list_09[0]
print list_09[1]

'*' * 70

print '*' * 70
for i in range(1, 10) :
    for j in range(1, i+1) :
        print j, 'x', i, '=', j*i, '\t',
    print '\n'
