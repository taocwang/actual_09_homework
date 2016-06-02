# encoding: utf-8
import os,sys
reload(sys)
sys.setdefaultencoding( "utf-8" )
import gconf
import MySQLdb

#查询
def execute_fetch_sql(sql,args=(),fetch=True):
	return execute_sql(sql,args,fetch)
#添加
def execute_commit_sql(sql,args=(),fetch=False):
	return execute_sql(sql,args,fetch)
#删除
def execute_del_sql(sql,args=(),fetch=False):
	return execute_sql(sql,args,fetch)
#更新
def execute_update_sql(sql,args=(),fetch=False):
	return execute_sql(sql,args,fetch)


#连接数据库，执行增删改
def execute_sql(sql,args=(),fetch=True):  
	_conn =None
	_cur = None
	_count = 0 
	_rt_list =[]

	try:
		_conn = MySQLdb.connect(host=gconf.MYSQL_HOST,port=gconf.MYSQL_PORT, \
				db=gconf.MYSQL_DB,user=gconf.MYSQL_USER, passwd=gconf.MYSQL_PASSWORD,charset=gconf.MYSQL_CHARSET)
		_cur = _conn.cursor()
		_count = _cur.execute(sql,args)
		if fetch:
			_rt_list = _cur.fetchall()
		else:
			_conn.commit()
	except BaseException as e:
		print e
	finally:
		if _cur:
			_cur.close()
		if _conn:
			_conn.close()

	return _count,_rt_list
