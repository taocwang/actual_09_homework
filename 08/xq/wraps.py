#!/usr/bin/env python
# coding=utf-8

import time

def time_wrapper(func):
    def warpper():
        print "计时开始：%s" %func.__name__
        start = time.time()
        rt = func()
        print "计时结束：%s---%s" %(func.__name__,time.time()-start)
        return rt
    return warpper


def log_wrapper(func):
    def warpper():
        print  "log装饰器开始：%s" %(func.__name__)
        rt = func()
        print "log装饰器结束：%s" %(func.__name__)
        return rt
    return warpper

@time_wrapper
@log_wrapper
def test():
    print 'test'


test()
