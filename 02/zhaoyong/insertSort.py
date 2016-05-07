#encoding: utf-8

list_num = [6,5,4,3,2,1]

for i in range(0,len(list_num) -1):
    for j in range(i,len(list_num)):
        if list_num[i] > list_num[j]:
            list_num[i],list_num[j] = list_num[j],list_num[i]
            print list_num

print '*' *100

list_num = [6,5,4,3,2,1]

for i in range(1,len(list_num)):
    for j in range(i,0,-1):
        if list_num[j-1] > list_num[j]:
            list_num[j-1],list_num[j] = list_num[j],list_num[j-1]
            print list_num