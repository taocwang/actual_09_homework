#encoding: utf-8
import json
import MySQLdb
import gconf
from dbutils import execute_fetch_sql,execute_commit_sql,execute_del_sql,execute_update_sql

#查询所有用户信息
def get_users():

	_columns = ('id','username','password','age')
	_sql = 'select * from user'
	_count,_rt_list= execute_fetch_sql(_sql)
	_rt=[]
	
	for _line in _rt_list:
		_rt.append(dict(zip(_columns,_line)))

	return _rt


#检查 用户名密码是否正确。正确返回True 不正确返回False
def validate_login(username,password):
	# _sql = 'select * from user where username="{username}" and password=md5("{password}")'.format(username=username,password=password)
	_sql = 'select * from user where username=%s and password=md5(%s)'
	_count,_rt_list= execute_fetch_sql(_sql,(username,password))
	return _count != 0

def validate_add_user(username,password,age):
	user_list = get_users()

	for users in user_list:
		if users['username'] == username:
			return False, u'用户名已存在'

	if username.strip() == '':
		return False, u'用户名不能为空'
	if len(password) < 6:
		return False, u'密码长度至少为6位'
	if not str(age).isdigit() or int(age) <= 0 or int(age) > 100:
		return False, u'年龄不正确'	

	return True, ''


#检查用户信息，如果不满足就返回False和错误信息，此处返回值是个元组和apptest1.py里面要对应。
def validate_user(username,password,age):
	user_list = get_users()

	# for users in user_list:
	# 	if line['username'] == username:
	# 		return False, u'用户名已存在'

		# if username.strip() == '':
		# 	return False, u'用户名不能为空'
		# if len(password) < 6:
		# 	return False, u'密码长度至少为6位'
	if not str(age).isdigit() or int(age) <= 0 or int(age) > 100:

		return False, u'年龄不正确'	

	return True, ''



#添加用户，id唯一。自增长
def add_user(username,password,age):
	_sql = 'insert into user(username,password,age) values(%s,md5(%s),%s)'
	_args = (username,password,age)
	execute_commit_sql(_sql,_args)


#删除用户，通过id删除。id唯一
def del_user(delid):
	_sql = 'delete from user where id=%s'

	execute_del_sql(_sql,(delid,))

#更新用户，根据更新的内容调用不同的sql 但是id是一个。id唯一
def change_user(userid,updateuser,updateage,updatepassword):

	user_list = get_users()

	for users in user_list:
		# if users['id'] == long(userid):
		# 	if users['username'] != updateuser:
		# 		_sql = 'update user set username=%s where id =%s'
		# 		_args = (updateuser,userid)
		# 		execute_update_sql(_sql,_args)
			if users['age'] != updateage:
				_sql = 'update user set age=%s where id =%s'
				_args = (updateage,userid)
				execute_update_sql(_sql,_args)
			# if users['password'] != updatepassword:
			# 	_sql = 'update user set password=md5(%s) where id =%s'
			# 	_args = (updatepassword,userid)
			# 	execute_update_sql(_sql,_args)


#通过id获取指定用户的信息
def get_user(userid):
    _users = get_users()

    for _user in _users:
        if _user.get('id') == long(userid):
        	return _user   
    return None
