#encoding: utf-8
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

import json
import gconf
import MySQLdb

from dbutils import MySQLConnection

class User(object):	
	@classmethod
	def validate_login(cls, username, password):
		_columns = ('id', 'username')
		_sql = 'select id, username from user where username=%s and password=md5(%s)'
		_count, _rt_list = MySQLConnection.execute_sql(_sql, (username, password))
		return dict(zip(_columns, _rt_list[0])) if _count != 0 else None

	@classmethod		
	def get_list(cls):
		sql = 'select * from user'
		rt = []
		columns=("id","username","password","age","gender","email")
		count, rt_list = MySQLConnection.execute_sql(sql)
		for line in rt_list:
			rt.append(dict(zip(columns, line)))
		return rt	

	def validate_user(self, username=None, user_id=None):
		if username:
			sql = 'select * from user where username=%s'
			args = (username,)
		elif user_id:
			sql = 'select * from user where id=%s'
			args = (user_id,)
		count, rt_list = MySQLConnection.execute_sql(sql,args)
		return count == 0
	
	@classmethod		
	def add(cls, username, password, age, gender, email):
		user = User()
		if user.validate_user(username):
			sql = 'insert into user(username, password, age, gender, email) values(%s, md5(%s), %s, %s, %s)'
			args = (username, password, age, gender, email)
			fetch = False
			count, rt_list = MySQLConnection.execute_sql(sql, args, fetch)
			return count != 0
		else:
			return False	
			
	@classmethod
	def update(cls, age, user_id, gender, email):
		user = User()
		if not user.validate_user(user_id=user_id):
			sql = 'update user set age=%s, gender=%s, email=%s where id = %s'
			args = (age, gender, email, user_id)
			fetch = False
			count, rt_list = MySQLConnection.execute_sql(sql, args, fetch)
			return count != 0
		else:
			return False	
			
	@classmethod
	def delete(cls, user_id):
		sql = 'delete from user where id = %s'
		args = (user_id,)
		fetch = False
		count, rt_list = MySQLConnection.execute_sql(sql, args, fetch)
		return count != 0			
	
	@classmethod
	def validate_charge_user_password(cls, user_id, upassword, musername, mpassword):
		if not cls.validate_login(musername, mpassword):
			return False, '管理员密码错误'
		
		user = User()
		if user.validate_user(user_id=user_id):	
			return False, '用户信息不存在'
		
		if len(upassword) < 6:
			return False, '密码必须大于等于6'
		
		return True, ""	

	@classmethod
	def charge_user_password(cls, uid, upassword):	
		sql = 'update user set password=md5(%s) where id=%s'
		args = (upassword, uid)
		fetch = False
		count, rt_list = MySQLConnection.execute_sql(sql, args, fetch)
		return count != 0
	
class Asset(object):
	@classmethod
	def get_list(cls,asset_id=None):
		rt = []
		columns=("id","sn","ip","hostname","os","cpu","ram","disk","idc_id","admin","business","purchase_date","warranty","vendor","model","status","idc_name")
		if asset_id:
			sql = 'SELECT a.id,a.sn,a.ip,a.hostname,a.os,a.cpu,a.ram,a.disk,a.idc_id,a.admin,a.business,a.purchase_date,a.warranty,a.vendor,a.model,a.status, b.`name` idc_name from assets a, idcs b WHERE a.id=%s and a.idc_id=b.id'
			args = (asset_id,)
		else:
			sql = 'SELECT a.id,a.sn,a.ip,a.hostname,a.os,a.cpu,a.ram,a.disk,a.idc_id,a.admin,a.business,a.purchase_date,a.warranty,a.vendor,a.model,a.status, b.`name` idc_name from assets a, idcs b WHERE a.status=0 and a.idc_id=b.id'	
			args = ()
		count, rt_list = MySQLConnection.execute_sql(sql,args)
		for line in rt_list:
			rt.append(dict(zip(columns, line)))
		rt[0]['purchase_date']=str(rt[0]['purchase_date'])	
		return rt	
	
	@classmethod	
	def idcs_list(cls):
		sql = 'select id,name from idcs where status=0'
		count, rt_list = MySQLConnection.execute_sql(sql)
		return rt_list		
	
	@classmethod
	def validate(cls,asset_info,repeat=True):
		errors = {}
		for value in asset_info:
			if asset_info[value] == "":
				errors[value] = "%s为空" % value
		if errors != {}:
			return False, errors			
		if not asset_info["cpu"].isdigit():
			errors["cpu"] = "cpu核数只能写整数,请重新填写"
		if not asset_info["disk"].isdigit():
			errors["disk"] = "硬盘大小只能写整数,请重新填写"
		if not asset_info["ram"].isdigit():
			errors["ram"] = "内存大小只能写整数,请重新填写"
		if not asset_info["warranty"].isdigit():
			errors["warranty"] = "保修时间只能写整数,请重新填写"
		if errors != {}:
			return False, errors
		if repeat:	
			sql = 'select sn from assets where sn=%s'
			args =(asset_info['sn'],)
			count, rt_list = MySQLConnection.execute_sql(sql,args)
			if count != 0:
				errors['sn'] = "sn编码重复,请重新输入"
		if errors != {}:
			return False, errors
		else:
			return True, {}
	
	@classmethod
	def create(cls,asset_info):
		sql = 'insert into assets (sn,ip,hostname,os,cpu,ram,disk,idc_id,admin,business,purchase_date,warranty,vendor,model) values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'
		args = (asset_info.get('sn'),asset_info.get('ip'),asset_info.get('hostname'),asset_info.get('os'),asset_info.get('cpu'),asset_info.get('ram'),asset_info.get('disk'),asset_info.get('idc_id'),asset_info.get('admin'),asset_info.get('business'),asset_info.get('purchase_date'),asset_info.get('warranty'),asset_info.get('vendor'),asset_info.get('model'))
		fetch = False
		count, rt_list = MySQLConnection.execute_sql(sql, args, fetch)
		return count != 0		

	@classmethod		
	def update(cls,asset_info):
		sql = 'update assets set ip=%s,hostname=%s,os=%s,cpu=%s,ram=%s,disk=%s,idc_id=%s,admin=%s,business=%s,purchase_date=%s,warranty=%s,vendor=%s,model=%s where id=%s'
		args = (asset_info.get('ip'),asset_info.get('hostname'),asset_info.get('os'),asset_info.get('cpu'),asset_info.get('ram'),asset_info.get('disk'),asset_info.get('idc_id'),asset_info.get('admin'),asset_info.get('business'),asset_info.get('purchase_date'),asset_info.get('warranty'),asset_info.get('vendor'),asset_info.get('model'),asset_info.get('id'))
		fetch = False
		count, rt_list = MySQLConnection.execute_sql(sql, args, fetch)
		return count != 0	
		
	@classmethod	
	def drop(cls,asset_id):
		sql = 'update assets set status=1 where id=%s'
		args = (asset_id,)
		fetch = False
		count, rt_list = MySQLConnection.execute_sql(sql, args, fetch)
		return count != 0	

class Logscount(object):
	#格式化日志文件
	@classmethod
	def format_logs(cls,logs_filename):
		path = logs_filename
		log = {}	
		rh = open(path,'r')
		for rf in rh:
			x = (rf.split(' ')[0], rf.split(' ')[6], rf.split(' ')[8])
			log[x] = log.get(x,1) + 1
		rh.close()
		return log.items()
		
	#使用load data导入数据	
	@classmethod
	def load_data_logs(cls,logs_filename, clear_logs=True):
		print logs_filename
		logs = format_logs(logs_filename)	
		#print logs
		wh = open('access_logs.txt', 'w')
		for i, ii in logs:
			for iii in i:
				wh.write(iii)
				wh.write(",")
			wh.write(str(ii))	
			wh.write("\n")
		wh.close()	
		if clear_logs:
			sql = 'delete from access_logs'
			args = ()
			fetch = False
			MySQLConnection.execute_sql(sql, args, fetch)
		#sql = 'load data local infile "access_logs.txt" into table access_logs fields terminated by "," lines terminated by "\n"'
		sql = 'load data local infile "access_logs.txt" into table access_logs fields terminated by "," lines terminated by "\n"'
		args = ()
		fetch = False
		MySQLConnection.execute_sql(sql, args, fetch)
	
	@classmethod	
	def logscount(cls,cut=10):
		rt_list = []
		sql = 'select * from access_logs order by TOTAL desc limit %s'
		args = (cut,)
		count, rt_list = MySQLConnection.execute_sql(sql, args)
		return rt_list
	
if __name__ == '__main__':
	print User.add('reboot', 'reboot', '30', '女', 'reboot@reboot.com')