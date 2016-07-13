#!/usr/bin/env python
#-*- coding:utf-8 -*-


import json, gconfig
from flask import request
from dbutils import excute_mysql

def get_user():
	_cols = ('uid', 'username', 'password', 'age', 'phone', 'email')
	sql = 'select * from user'
	_rt = []
	_count, _rt_list = excute_mysql(sql)
	for i in _rt_list:
		_rt.append(dict(zip(_cols, i)))
	return _rt


def checkUser(username=None, uid=None):
	_cols = ('uid', 'username', 'password', 'age', 'phone', 'email')
	sql = 'select * from user where username=%s or id=%s'
	args = (username,uid)
	_count, _rt_list = excute_mysql(sql, args)
	return _count, _rt_list


def validate_login(username, password):
	#_sql = 'select * from user where username="{username}" and password=md5("{password}")'.format(username=username, password=password)
	#为了预防SQL注入，SQL语句写成如下：
	sql1 = 'select * from user where username=%s and password=md5(%s)'
	args = (username, password)
	print args
	_count, _rt_list = excute_mysql(sql1, args)
	return _count != 0


def user_list(number):
	users = get_user()
	userlist = sorted(users, key=lambda x:x['username'])
	if len(userlist) > number:
		return userlist[:number]
	else:
		return userlist

def add_user(username, password, age, phone, email):
	_count, _rt_list = checkUser(username=username)
	if _count:
		return False
	else:
		_sql = 'insert into user(username, password, age, phone, email) value (%s, md5(%s), %s, %s, %s)'
		args = (username, password, age, phone, email)
		excute_mysql(_sql, args, fetch=False)
		return True
	#userlist.append(userinfo)
	#result = file_write(gconfig.USER_FILE, json.dumps(userlist))
	#return result
	# f = open(gconfig.USER_FILE, 'wb')
	# f.write(json.dumps(userlist))
	# f.close()

def delUser(uid):
	sql = 'delete from user where id=%s'
	args = (uid, )
	excute_mysql(sql, args, fetch=False)
	return True

	

def modifyUser(uid):
	_count, _rt_list = checkUser(uid=uid)
	print _count, _rt_list
	if _count:
		_cols = ('uid', 'username', 'password', 'age', 'phone', 'email')
		_content = dict(zip(_cols, _rt_list[0]))
		return _content
	else:
		return False


def upToDb(uid, username, password, age, phone, email):
	sql = 'update user set password=md5(%s),age=%s,phone=%s,email=%s where id=%s and username=%s'
	args = (password, age, phone, email, uid, username)
	excute_mysql(sql, args, fetch=False)
	return True


if __name__ == '__main__':
	get_user()