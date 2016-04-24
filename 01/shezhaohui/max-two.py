#ecoding: utf-8
num = [1,2,3,2,12,3,1,3,21,2,2,3,4111,22,3333,444,111,4,5,777,65555,45,33,45]
zd = num[0]
dr = num[0]
for n in num:
    if n > zd:
        zd = n
for n in num:
    if n != zd and dr < n:
        dr = n
print '最大的数字是： %s,第二大的数字是： %s' % (zd, dr)
