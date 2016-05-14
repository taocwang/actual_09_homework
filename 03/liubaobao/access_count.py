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