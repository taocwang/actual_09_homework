#encoding:utf-8

names = ['woniu','kk','wd']
raw_name = raw_input("please input names:")
exists = False
for i in names:
    if raw_name == i:
        exists = True
        break


if exists:
    print "%s is in names" % raw_name
else:
    print "%s is not in names" % raw_name
import random

num_list = range(10)
print max(num_list)
print min(num_list)
print len(num_list)
print random.randint(1,len(num_list))
print 2 in num_list

#
num_list2 = num_list
#
num_list3 = num_list[:]

num_list2[-1] = 'haha'
num_list3[-1] = 'kaka'

print num_list
print num_list2
print num_list3

num_list4 = num_list3
num_list3[-2] = 'kaka'
print num_list3
print num_list4


names_list = ['kk','ada','pc','woniu']
print names_list

#add 1
names_list[0] = 'jcui'
print names_list

#add 2
names_list[1:1] = ['lala','huhu']
print names_list

#del 1
names_list[1:1] = ''
print names_list

#del 2
names_list[1:3] = ''
print names_list

#del(根据索引删除)
del names_list[0:2]
print names_list

#list + and *
list1 = ['woniu','kk']
list2 = ['wd','ada']
print (list1 + list2) *2

#index
print list1.index('woniu')

#append(追加到列表的最后)
list1.append('jcui')
print list1

#extend()
list1.extend(list2)
print list1

#count(统计元素出现的次数)
print list1.count('jcui')

#insert(插入元素)
list2.insert(0,'wawa')
print list2

#pop(删除病返回值，默认删除最后一个)
list2.pop(0)
print list2

#remove(根据value删除列表的元素)
list2.remove('wd')
print list2

#reverse(倒序排列)
list2.reverse()
print list2

#sort（从小到大）
list2.sort()
print list2
#sort（从大到小）
list2.sort(reverse=True)
print list2

#max （求列表的最大值）
print max(list2)

#min （求列表的最小值）
print min(list2)

list3 = [1,2,4,5,123,123,123,1,2,3,5]
# nn = int(raw_input('please input a num:'))
nn = 4
m = 0
for i in list3:
    if nn == i:
        m+=1
print '%s is num %s' % (nn,m)
print list3.count(nn)
print list3.index(5,list3.index(5)+1)

try:
    print list3.index(2,2,3)
except ValueError as e:
    print e

list3.insert(-1,3)
print list3

#作业，先进先出

works = []
in_put = []
while True:
    in_put = raw_input("please input add or do:")
    if in_put == 'add':
        in_put_work = raw_input('please input works:')
        works.append(in_put_work)
    elif in_put == 'do':
        if not works:
            print "works is null"
        else:
            print works.pop(0)
    elif in_put == 'exit':
        if works:
            print "works has some works %s" % works
        else:
            print "works is finish"
            break


#排序
heigh = [165, 168, 155, 179, 169, 173, 175, 178, 160]
for i in range(0,len(heigh)):
    for j in range(0,len(heigh)-1):
        if heigh[i] < heigh[j]:
            heigh[i],heigh[j] = heigh[j],heigh[i]
print heigh

#冒泡排序
heighs = [165, 168, 155, 179, 169, 173, 175, 178, 160]
for y in range(0,len(heighs)-1): #循环的次数
    for x in range(0,len(heighs)-1-y):   #每次将最大的数置于最后 -y 代表不需要再和最后的值做比较，上一次已经比较过
        if heighs[x] > heighs[x+1]:
            heighs[x],heighs[x+1] = heighs[x+1],heighs[x]
print heighs

#列表倒序排列（倒序）
list_num = range(0,10)
for i in range(0,len(list_num)/2):
    list_num[i],list_num[-1-i] = list_num[-1-i],list_num[i]
print list_num
# list_num = range(0,10)
# print len(list_num)/2
# for i in range(0,len(list_num)/2):
#     print list_num
#     print i
#     list_num.pop()
#     list_num[i] = list_num.pop()
# print list_num

#列表去重
num_list5 = [1,2,3,4,2,12,3,14,3,2,12,3,14,3,21,2,2,3,4111,22,3333,4]
num_list6 = []
for i in num_list5:
    if i not in num_list6:
        num_list6.append(i)
print num_list6

#列表Set去重
print list(set(num_list5))

#求两个数组共同的值（去重）
arr1 = [1,2,3,4,2,12,3,14,3,2,12,3,14,3,21,2,2,3,4111,22,3333,4]
arr2 = [2,1,3,2,43,234,454,452,234,14,21,14]
arr3 = []
for i in arr2:
    if i in arr1 and i not in arr3:
        arr3.append(i)
print arr3


#元祖 （tuple）

num_num = tuple(range(10))
print num_num

print max(num_num)
print min(num_num)
print num_num.index(3)
print num_num.count(3)