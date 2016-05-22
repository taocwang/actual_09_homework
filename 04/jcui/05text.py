#encoding:utf-8
#by jcui
#by 2016-05-22

''
'''
列表推倒式

作用: 用于生成一个新的列表

由[] 组成

lambda 匿名函数,是一个函数,调用注意加()

add = lambda x,y: x+y

list.sort函数  只针对列表

sorted函数

'''
#老方法
def filter(x):
    return x % 2 == 0

def translate(x):
    return x * x

print [translate(x) for x in range(10) if filter(x)]

#新方法
print [x * x for x in range(0,10) if x % 2 == 0]


print [(x,x*2,x*x) for x in range(0,10) ]
print [(x,x*2,x*x) for x in range(0,10) if x % 2 == 0]

#lambda
add = lambda x,y : x+y

print add(4,5)
a = add
print a(4,5)

#list.sort()函数
def cmp(x,y):
    if x>y:
        return True
    else:
        return False

def list_sort(lists,key,cmp):
    for n in range(len(lists)-1):
        for i in range(len(lists)-1):
            if cmp(key(lists[i]),key(lists[i+1])):
                lists[i], lists[i + 1] = lists[i + 1], lists[i]
    return lists


num_list3 = [(11, 4), (5, 1), (2, 3), (10, 2), (6, 3), (23, 4, 43, 4), (34, 45), (1, 1, 1, 1, 1)]
print '按最大值排序: %s' % list_sort(num_list3, key=lambda x: max(x), cmp=cmp)
num_list3 = [{'a': 1}, {'e': 9}, {'c': 0}, {'d': 3}]
print '按最大值排序: %s' % list_sort(num_list3, key=lambda x: x.values(), cmp=cmp)


#sorted函数
work_list = [(1,4),(5,3),(2,3)]

new_list = sorted(work_list,key=lambda x:max(x))    #按最大值比较
print new_list

new_list = sorted(work_list,key=lambda y:min(y))    #按最小值比较
print new_list

'''
模块/包

#模块
import 文件名

调用方法: 文件名.函数名()

from 文件名 import 函数名
from 文件名 import *     #导入所有的包中的所有模块

调用方法: 函数名()

#包
一堆模块组成的文件夹
同级目录必须包含 __init__.py 文件

import完成,在调用的时候优先执行__init_.py的内容

from 文件夹 import 文件名1,文件名2

避免使用与系统默认的包一样的名字
'''
print '模块'
import sortlist
mylist = [1,9,54,6,2,10]
print sortlist.list_sort(mylist)

mylist2 =  [(11, 4), (5, 1), (2, 3), (10, 2), (6, 3), (23, 4, 43, 4), (34, 45), (1, 1, 1, 1, 1)]
print sortlist.list_sort(mylist2,key=lambda x:max(x))

from sortlist import list_sort
mylist3 =  [(11, 4), (5, 1), (2, 3), (10, 2), (6, 3), (23, 4, 43, 4), (34, 45), (1, 1, 1, 1, 1)]
print list_sort(mylist3,key = lambda x: min(x))

'''
flask

debug
1,  修改自动reload
2,  错误页面会提示,否则报只是报http错误

MVC:
M: module
V: view
C: control


json
import json

json.loads()   将字符串转换为列表
json.dumps()   将列表转换为字符串
'''

import json

a = [{'username':'jcui','password':'123456'},{'username':'admin','password':'654321'}]

b = json.dumps(a)
print b
print type(b)

c = json.loads(b)
print c
print type(c)

def test():
    a = 1
    b = 2
    return a,b

print test()