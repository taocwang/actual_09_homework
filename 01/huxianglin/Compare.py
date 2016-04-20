#!/usr/bin/env python
# enconding:utf-8
List = [1,2,3,2,12,3,1,3,21,2,2,3,4111,22,3333,444,111,4,5,777,65555,45,33,45]
Min,Max = List[0],List[0]
for i in List:
    if i < Min:
        Min = i
    elif i > Max:
        Max = i
print "The max is %s" % (Max)
print "The min is %s" % (Min)