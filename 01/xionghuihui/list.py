#encoding:utf-8
a = [1,2,3,2,12,3,1,3,21,2,2,3,4111,22,3333,444,111,4,5,777,65555,45,33,45]
b = a[0]
c = a[0]
for i in a:
    if b < i:
       b = i
for i in a:
    if i != b and c < i:
       c = i
print b,c
