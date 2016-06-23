#!/usr/bin/env python
# -*- coding: utf-8 -*-
import time

def fun_wrapper(func):
    def wrapper():
        print '函数%s执行开始' %(func.__name__)
        start=time.time()
        rt=func()
        print '函数%s执行结束，执行时间%s' %(func.__name__,time.time()-start)
        return rt
    return wrapper

@fun_wrapper
def test1():
    time.sleep(5)
    return 5
test1()