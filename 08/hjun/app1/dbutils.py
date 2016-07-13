#encoding: utf-8
import gconf
import MySQLdb
	
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
	