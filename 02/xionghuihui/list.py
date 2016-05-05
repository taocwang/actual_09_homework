#encoding:utf-8
#插入排序
num = [1,2,4,7,3,8,5]
for i in range(len(num) - 1):
    for j in range(i + 1,len(num)):
        if num[i] > num[j]:
            a = num[i]
            num[i] = num[j]
            num[j] = a
            print num
#print num
