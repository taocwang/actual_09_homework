#encoding: utf-8

import json
import gconf
import MySQLdb
from dbutils import execute_sql

def get_users():
	sql = 'select * from user'
	rt = []
	columns=("id","username","password","age","gender","email")
	count, rt_list = execute_sql(sql)
	for line in rt_list:
		rt.append(dict(zip(columns, line)))
	return rt		

def validate_login(username, password):
	sql = 'select * from user where username=%s and password=md5(%s)'
	args = (username, password)
	count, rt_list = execute_sql(sql,args)
	return count != 0	

def validate_user(username=None, user_id=None):
	if username:
		sql = 'select * from user where username=%s'
		args = username
	elif user_id:
		sql = 'select * from user where id=%s'
		args = int(user_id)
	count, rt_list = execute_sql(sql,args)
	return count == 0	

def get_user(user_id):
	sql = 'select * from user where id=%s'
	args = user_id
	count,rt_list = execute_sql(sql,args)
	#return rt_list[0]
	if rt_list:
		columns=("user_id","username","password","age","gender","email")
		return dict(zip(columns, rt_list[0]))
	else:
		return False
		
def user_add(username, password, age, gender, email):
	if validate_user(username):
		sql = 'insert into user(username, password, age, gender, email) values(%s, md5(%s), %s, %s, %s)'
		args = (username, password, age, gender, email)
		fetch = False
		count, rt_list = execute_sql(sql, args, fetch)
		return count != 0
	else:
		return False
		
def user_del(user_id):
	sql = 'delete from user where id = %s'
	args = user_id
	fetch = False
	count, rt_list = execute_sql(sql, args, fetch)
	return count != 0
			
def user_edit(age, user_id, password, gender, email):
	sql = 'update user set password=%s, age=%s, gender=%s, email=%s where id = %s'
	args = (password, age, gender, email, user_id)
	fetch = False
	count, rt_list = execute_sql(sql, args, fetch)
	return count != 0
		
if __name__ == '__main__':
	print get_user(6)