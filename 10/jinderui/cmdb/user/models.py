#coding:utf-8

from dbutils import MySQLConnection
class User(object):
	def __init__(self,id,username,password,age):
		self.id = id
		self.username = username
		self.password = password
		self.age = age

	@classmethod
	def validate_login(self,username,password):
		_columns = ('id','username')
		_sql = 'select id,username from user where username=%s and password=md5(%s)'
		_count,_rt_list = MySQLConnection.execute_sql(_sql,(username,password))
		return dict(zip(_columns,_rt_list[0])) if _count !=0 else None
	@classmethod
	def get_list(self, wheres=[]):
		_columns = ('id', 'username', 'password', 'age')
		_sql = 'select * from user where 1=1'
		_args = []
		for _key, _value in wheres:
			_sql += ' AND {key} = %s'.format(key=_key)
			_args.append(_value)

		_count, _rt_list = MySQLConnection.execute_sql(_sql, _args)
		_rt = []
		for _line in _rt_list:
			_rt.append(dict(zip(_columns, _line)))
		print _rt
		return _rt
	@classmethod
	def get_users(self):

		_columns = ('id','username','password','age')
		_sql = 'select * from user'
		_count,_rt_list= MySQLConnection.execute_sql(_sql)
		_rt=[]
		
		for _line in _rt_list:
			_rt.append(dict(zip(_columns,_line)))

		return _rt
	#添加start
	@classmethod
	def validate_add_user(self,username,password,age):
		user_list = self.get_users()

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
	@classmethod
	def add_user(self,username,password,age,fetch=False):
		_sql = 'insert into user(username,password,age) values(%s,md5(%s),%s)'
		_args = (username,password,age)
		MySQLConnection.execute_sql(_sql,_args)
	#添加end


		#更新start
	@classmethod
	def validate_user(self,age):

		user_list = self.get_users()

		if not str(age).isdigit() or int(age) <= 0 or int(age) > 100:

			return False, u'年龄不正确'	

		return True, ''

	@classmethod
	def change_user(self,userid,updateage):

		user_list = self.get_users()

		for users in user_list:
			if users['age'] != updateage:
				_sql = 'update user set age=%s where id =%s'
				_args = (updateage,userid)
				MySQLConnection.execute_sql(_sql,_args,False)
	#更新end



	#修改密码进行验证
	@classmethod
	def validate_charge_user_password(self,userid,upassword,musername,mpassword):
		if not self.validate_login(musername,mpassword):
			return False,"管理员密码错误"
		if self.get_user(userid) is None:
			return False, u'用户信息不存在'
		if len(upassword) <6:
			return False,u'密码必须大于等于6'
		return True, ''

	@classmethod
	def charge_user_password(self,userid,upassword):
		_sql = 'update user set password=md5(%s) where id=%s'
		_args = (upassword,userid)
		MySQLConnection.execute_sql(_sql,_args,False)


	#通过id获取指定用户的信息
	@classmethod
	def get_user(self,userid):
	    _users = self.get_users()

	    for _user in _users:
	        if _user.get('id') == long(userid):
	        	return _user   
	    return None
	 #修改密码end

	@classmethod
	def del_user(self,delid):
		_sql = 'delete from user where id=%s'
		_args=(delid,)
		MySQLConnection.execute_sql(_sql,_args)


if __name__ == '__main__':
	print User.validate_login('jinderui','123456')
	print User.validate_login('jinderui','1234567')