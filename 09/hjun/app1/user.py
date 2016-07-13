#encoding: utf-8

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

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
		args = (user_id,)
	count, rt_list = execute_sql(sql,args)
	return count == 0	
		
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
	args = (user_id,)
	fetch = False
	count, rt_list = execute_sql(sql, args, fetch)
	return count != 0
			
def user_edit(age, user_id, gender, email):
	if not validate_user(user_id=user_id):
		sql = 'update user set age=%s, gender=%s, email=%s where id = %s'
		args = (age, gender, email, user_id)
		fetch = False
		count, rt_list = execute_sql(sql, args, fetch)
		return count != 0
	else:
		return False

def validate_charge_user_password(user_id, upassword, musername, mpassword):
	if not validate_login(musername, mpassword):
		return False, '管理员密码错误'
	
	if validate_user(user_id=user_id):	
		return False, '用户信息不存在'
	
	if len(upassword) < 6:
		return False, '密码必须大于等于6'
	
	return True, ""	

def charge_user_password(uid, upassword):	
	sql = 'update user set password=md5(%s) where id=%s'
	args = (upassword, uid)
	fetch = False
	count, rt_list = execute_sql(sql, args, fetch)
	return count != 0
	
if __name__ == '__main__':
	print validate_user(user_id=4)
	
