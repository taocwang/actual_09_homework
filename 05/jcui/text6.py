#encoding:utf-8

import time

''
'''
session      在服务端    一块存储
cookie       在浏览器端  一块存储
认证通过后,将sessions_id 放到服务端的session中
每次请求根据session_id获取session中的认证信息
如果认证信息存在 => 继续访问
如果无认证信息 => 跳转到登陆页面


导入 from flask import session

session ['session_name'] =  session_value

os.urandom(32)  随机生成32位字符串

'''




'''
装饰器

在所有函数之前执行一块代码
在函数之后执行一块代码

多个装饰器存在的bug
from functools import wraper

'''

#记录每个函数的执行时间

def time_wrapper(func):
    def wrapper():
        start = time.time()
        rt = func()
        exec_time = time.time() - start
        print '合计用时:%s' % exec_time
        return rt
    return wrapper

def test1():
    print 'test1'
    return 1

def test2():
    print 'test2'
    return 2

def test3():
    print 'test3'
    return 3

def test4():
    print 'test4'
    return 4

def test5():
    print 'test5'
    return 5

def wrapper(func):
    print '执行之前: %s' % func.__name__
    rt = func()
    print '执行之后: %s' % func.__name__
    return rt


print wrapper(test1)
print wrapper(test2)
print wrapper(test3)
print wrapper(test4)
print wrapper(test5)

@time_wrapper
def test6():
    print 'test6'
    time.sleep(10)
    return 6

print test6()