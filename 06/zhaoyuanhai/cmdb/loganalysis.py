#!/usr/bin/env python
#-*- coding:utf-8 -*-

from functools import wraps
import time
import dbutils

def time_wrapper(func):  #传入函数
	@wraps(func)
	def wrapper(*args, **kwargs): #计算函数计时
		print '开始计时: %s'%func.__name__
		start_time = time.time()  #计时开始
		rt = func(*args, **kwargs)  #执行函数
		exec_time = time.time() - start_time  #计算时间 
		print '结束计时: %s'%func.__name__
		return exec_time  #返回执行时间
	return wrapper 

@time_wrapper
def log2Db(file):
	_rt_list = []
	f = open(file, 'rb')
	for i in f:
		ilist = i.split()
		_rt_list.append((ilist[0], ilist[6], ilist[8]))
	sql = 'insert into accesslog values(%s, %s, %s)'
	dbutils.upLogToDb(sql, _rt_list)

def logTop(number):
	_rt = []
	count = 1
	#_sql = 'select ip, url, status, count(*) as cnt from accesslog group by ip, url, status  order by cnt desc limit %s'
	_sql = 'select ip, url, status, count(*) as cnt from accesslog group by ip ,url, status  order by cnt desc limit %s'
	args=(int(number),)
	_count, _rt_list = dbutils.excute_mysql(_sql, args)
	cols = ('number', 'ip', 'url', 'status', 'count')
	for i in _rt_list:
		_rt.append(dict(zip(cols,(count,i[0], i[1], i[2], i[3]))))
		count += 1
	#print _rt
	return _rt
	#print _rt_list



if __name__ == '__main__':
	#log2Db('/Users/yhzhao/Downloads/www_access_20140823.log')
	logTop(10)