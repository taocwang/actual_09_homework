#coding:utf-8

#First method(my method)
#定义列表
list_a = [(1,3),(4,7),(2,5),(6,7),(1,1),(2,2)]
#进行冒泡排序循环列表长度的n-1次
for i in range(0,len(list_a)-1):
    for j in range(0,len(list_a)-1):
        #进行列表里面的 每个元素元组里面的元素进行比较。如果第一个元素大就拿第一个元素进行比较然后j和j+1元素进行交换
        if list_a[j][0] > list_a[j][1]:
            if list_a[j][0] > list_a[j+1][0]:
                list_a[j],list_a[j+1] = list_a[j+1],list_a[j]
        #否则拿元组里面的第二个元素进行比较，然后进行列表的j和j+1进行交换
        else:
            if list_a[j][1] > list_a[j+1][1]:
                list_a[j],list_a[j+1] = list_a[j+1],list_a[j]
print '----------------one------------------------'
print list_a


#second method(kk techear's method)
#这个方法是根据max内置函数来进行冒泡排序
list_b = [(1,3),(4,7),(2,5),(6,7),(1,1),(2,2)]

for i in range(len(list_b)-1):
    for j in range(len(list_b)-1):
        if max(list_b[j]) > max(list_b[j+1]):
            list_b[j],list_b[j+1] = list_b[j+1],list_b[j]
print '--------two-----------'
print list_b
#third method(kk techear's function methond)
#这个方法是进行函数传参使程序更有复用性
list_c = [(1,3),(4,7),(2,5),(6,7),(1,1),(2,2)]
def list_sort(list_c):
    temp_list_c = list_c[:]
    for i in range(len(temp_list_c)-1):
        for j in range(len(temp_list_c)-1):
            if max(temp_list_c[j]) > max(temp_list_c[j+1]):
                 temp_list_c[j],temp_list_c[j+1] =  temp_list_c[j+1],temp_list_c[j]
    return temp_list_c
print '----------three-----------'
print list_sort(list_c)


#fourth method(kk techear's max function method)
#这个方法自己定义比较函数：
a=(1,7,5,9,3,4,5)
def getnum_max(a):
    mem_value=a[0]
    for i in a:
        if i>mem_value:
            mem_value = i
    return mem_value

list_c = [(1,3),(4,7),(2,5),(6,7),(1,1),(2,2)]
def list_sort1(list_c):
    temp_list_c = list_c[:]
    for i in range(len(temp_list_c)-1):
        for j in range(len(temp_list_c)-1):
            if getnum_max(temp_list_c[j]) >getnum_max(temp_list_c[j+1]):
                 temp_list_c[j],temp_list_c[j+1] =  temp_list_c[j+1],temp_list_c[j]
    return temp_list_c
print '----------four---------------'
print list_sort1(list_c)

'''
功能ok，非常棒，加油
'''
