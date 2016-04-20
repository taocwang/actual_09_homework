# -*- coding: utf-8 -*-
# 打印乘法口诀表
print '乘法口诀表：'
for i in range(1, 10):
    for j in range(1, 10):
        if i >= j:
            print '%s x %s = %s ' % (i, j, i*j),
    print ''

'''
功能ok， 可以考虑下去掉if实习相同的功能
'''