#encoding: utf-8
import gconf
import MySQLdb

class MySQLConnection(object):
	def __init__(self, host, port, user, passwd, db, charset="utf8"):
		self.__host = host
		self.__port = port
		self.__user = user
		self.__passwd = passwd
		self.__db = db
		self.__charset = charset
		self.__conn = None
		self.__cur = None
		self.__connect()
		
	def __connect(self):
		try:
			self.__conn = MySQLdb.connect(host=self.__host, port=self.__port, \
							user=self.__user, passwd=self.__passwd, db=self.__db, charset=self.__charset)
			self.__cur = self.__conn.cursor()
		except BaseException as e:
			print e
	
	def execute(self, sql, args=()):
		__cnt = 0
		if self.__cur:
			__cnt = self.__cur.execute(sql, args)
		return __cnt
	
	def fetch(self, sql, args=()):
		_cnt = 0
		_rt_list = []
		if self.__cur:
			_cnt = self.__cur.execute(sql, args)
			_rt_list = self.__cur.fetchall()
		return _cnt, _rt_list	
		
	def commit(self):
		if self.__conn:
			self.__conn.commit()
	
	def close(self):
		self.commit()
		if self.__cur:
			self.__cur.close()
			self.__cur = None
		
		if self.__conn:
			self.__conn.close()
			self.__conn = None
	
	@classmethod
	def execute_sql(cls, sql, args=(), fetch=True):
		_count = 0
		_rt_list = []
		_conn = MySQLConnection(host=gconf.MYSQL_HOST, port=gconf.MYSQL_PORT, user=gconf.MYSQL_USER, passwd=gconf.MYSQL_PASSWORD, db=gconf.MYSQL_DB, charset=gconf.MYSQL_CHARSET)
		if fetch:
			_count, _rt_list = _conn.fetch(sql, args)
		else:
			_count = _conn.execute(sql, args)
			_conn.close()
		return _count, _rt_list	
	
def execute_sql(sql, args=(), fetch=True):
	conn = None
	cur = None
	count = 0
	rt_list = []
	try:
		print sql
		conn = MySQLdb.connect(host=gconf.MYSQL_HOST, port=gconf.MYSQL_PORT, user=gconf.MYSQL_USER, passwd=gconf.MYSQL_PASSWORD, db=gconf.MYSQL_DB, charset=gconf.MYSQL_CHARSET)
		cur = conn.cursor()
		count = cur.execute(sql,args)
		if fetch:
			rt_list = cur.fetchall()
		else:	
			conn.commit()
	except BaseException as e:
		print e
	finally:
		if cur:
			cur.close()
		if conn:
			conn.close()		
	return count, rt_list	

if __name__ == '__main__':
	sql='select * from user where username=%s and password=md5(%s)'
	print MySQLConnection.execute_sql(sql,args=('kk', 111))	