#encoding: utf-8

list_num = [(1,4),(5,1),(2,3),(0,9),(0,1)]


for j in range(0,len(list_num) -1):
    for i in range(0,len(list_num) -1 -j):
        if max(list_num[i]) >  max(list_num[i+1]):
            list_num[i],list_num[i+1] = list_num[i+1],list_num[i]
print list_num

print list_num.sort()


