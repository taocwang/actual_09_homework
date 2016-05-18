#encoding: utf-8

sort_list = [(1,4),(5,1),(2,3)]

for j in range(len(sort_list) - 1):
    for i in range(len(sort_list) - 1):
        if max(sort_list[i]) > max(sort_list[i + 1]): #比较元素
            #交换元素
            temp = sort_list[i]
            sort_list[i] = sort_list[i + 1]
            sort_list[i + 1] = temp

print u'第一次排序'
print sort_list

#使用冒泡排序list
def listsort(rlist):
    for j in range(len(rlist) - 1):
        for i in range(len(rlist) - 1):
            if max(rlist[i]) > max(rlist[i + 1]): #比较元素
                #交换元素
                temp = rlist[i]
                rlist[i] = rlist[i + 1]
                rlist[i + 1] = temp

print u'第二次排序'
sort_list = [(1,4),(5,1),(2,3)]
listsort(sort_list) #传址
print sort_list

#使用冒泡排序list, 不想影响原始的list
def listsort2(rlist):
    temp_list = rlist[:]
    for j in range(len(temp_list) - 1):
        for i in range(len(temp_list) - 1):
            if max(temp_list[i]) > max(temp_list[i + 1]): #比较元素
                #交换元素
                temp = temp_list[i]
                temp_list[i] = temp_list[i + 1]
                temp_list[i + 1] = temp
    return temp_list

print u'第三次排序'
sort_list = [(1,4),(5,1),(2,3)]
print listsort2(sort_list) #传址
print sort_list

# 参数x是一个list或者一个元祖
def get_max_num(x):
    max_value = x[0]
    for i in x:
        if max_value < i:
            max_value = i
    return max_value

#使用冒泡排序list, 不想影响原始的list
def listsort3(rlist):
    temp_list = rlist[:]
    for j in range(len(temp_list) - 1):
        for i in range(len(temp_list) - 1):
            if get_max_num(temp_list[i]) > get_max_num(temp_list[i + 1]): #比较元素
                #交换元素
                temp = temp_list[i]
                temp_list[i] = temp_list[i + 1]
                temp_list[i + 1] = temp
    return temp_list

print u'第四次排序'
sort_list = [(1,4),(5,1),(2,3)]
print listsort3(sort_list) #传址
print sort_list
