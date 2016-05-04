#encoding:utf-8
heigh = [199,168,179,173,175,178]

for j in range(0,len(heigh) - 1):
    for i in range(0,len(heigh) - 1 - j):
        if heigh[i] > heigh[i + 1]:
                heigh[i],heigh[i + 1] = heigh[i + 1 ], heigh[ i ]
        print '将第%s个人排序到最后的结果为:\n%s ' % ((j + 1), heigh)
