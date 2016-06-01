#!/usr/bin/env python
#-*- coding:utf-8 -*-

import MySQLdb as db
import gconfig

def excute_mysql(sql, args=(), fetch=True):
	_conn = None
	_cur = None
	_rt_list = []
	_count = 0
	try:
		print sql, args
		_conn = db.connect(host=gconfig.MYSQL_HOST, port=gconfig.MYSQL_PORT, user=gconfig.MYSQL_USER,\
							passwd=gconfig.MYSQL_PASSWD, db=gconfig.MYSQL_DB, charset=gconfig.CHARSET)
		_cur = _conn.cursor()
		_count = _cur.execute(sql, args)
		if fetch:
			_rt_list = _cur.fetchall()
		else:
			_conn.commit()
	except Exception, e:
		print e

	finally:
		if _cur:
			_cur.close()
		if _conn:
			_conn.close()
	return _count, _rt_list


def upLogToDb(sql, log_list):
	_conn = None
	_cur = None
	try:
		_conn = db.connect(host=gconfig.MYSQL_HOST, port=gconfig.MYSQL_PORT, user=gconfig.MYSQL_USER,\
							passwd=gconfig.MYSQL_PASSWD, db=gconfig.MYSQL_DB, charset=gconfig.CHARSET)
		_cur = _conn.cursor()
		for i in log_list:
			args = (i[0], i[1], i[2])
			_count = _cur.execute(sql, args)
		_conn.commit()
	except Exception, e:
		print e

	finally:
		if _cur:
			_cur.close()
		if _conn:
			_conn.close()