#!/usr/bin/env python
#coding:utf-8
import multiprocessing
def logc():
    log = 'access.log'
    handle = open(log,'r')
    log_count = {}
    for line in handle:
        key=(line.split(' ')[0],line.split(' ')[6],line.split(' ')[8])
        log_count[key]=log_count.get(key,0) + 1
    log_count = log_count.items()
    for j in range(0,len(log_count)-1):
         for i in range(0,len(log_count)-1):
             if log_count[i][1] > log_count[i+1][1]:
                 temp = log_count[i]
                 log_count[i] = log_count[i+1]
                 log_count[i+1] = temp
    log_count = log_count[-1:-11:-1]
    for a in log_count:
         print '''Ip:%-18sUrl:%-50sStatus:%-8sCount:%s''' %(a[0][0],a[0][1],a[0][2],a[1])

if __name__ == "__main__":
    pool = multiprocessing.Pool(processes=5)
    for i in xrange(10):
        msg = "hello %d" %(i)
        pool.apply_async(logc,)
    pool.close()
    pool.join()


'''
功能ok,复习了不少东西
改进点:
1. line9, 可以考虑split 1次，通过返回值通过index获取需要的值
2. 虽然考虑了使用多进程的方式，但是每个进程中处理都是完成一样的，只是将一件事重复做了10次
    对于该练习多进程方式不会加快处理，可以考虑多进程试用的场景，比如是处理多个日志文件等等，加油
'''
