#ecoding: utf-8
print '九九乘法表：'
for i in range(1, 10):
    for j in range(1, i+1):
        print '%s x %s = %s' %(j, i, j*i),
    print '\n'
