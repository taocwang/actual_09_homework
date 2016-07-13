#encoding: utf-8

import json
import gconf
import MySQLdb
from dbutils import execute_sql

def get_users():
	sql = 'select * from user'
	rt = []
	columns=("id","username","password","age")
	count, rt_list = execute_sql(sql)
	for line in rt_list:
		rt.append(dict(zip(columns, line)))
	return rt		

def validate_login(username, password):
	sql = 'select * from user where username=%s and password=md5(%s)'
	args = (username,password)
	count, rt_list = execute_sql(sql,args)
	return count != 0	

def validate_user(username):
	sql = 'select * from user where username=%s'
	args = username
	count, rt_list = execute_sql(sql,args)
	return count == 0	

def get_user(username):
	users = get_users()
	user_dict={}
	for user in users:
		if user.get('username') == username:
			user_dict['username'] = username
			user_dict['password'] = user['password']
			user_dict['age'] = user['age']			
	return user_dict
			
def user_add(username,password,age):
	if validate_user(username):
		sql = 'insert into user(username, password, age) values(%s, md5(%s), %s)'
		args = (username, password, age)
		fetch = False
		count, rt_list = execute_sql(sql, args, fetch)
		return count != 0
	else:
		return False
		
def user_del(username):
	sql = 'delete from user where id = (select id from (select id from user where username = %s) temp)'
	args = username
	fetch = False
	count, rt_list = execute_sql(sql, args, fetch)
	return count != 0
			
def user_edit(username, password, age):
	sql = 'update user set password=md5(%s), age=%s where id = (select id from (select id from user where username = %s) temp)'
	args = (password, age, username)
	fetch = False
	count, rt_list = execute_sql(sql, args, fetch)
	return count != 0
		
if __name__ == '__main__':
	print user_edit(username='hjun', password='222', age=666)