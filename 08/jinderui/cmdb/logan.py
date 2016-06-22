# encoding: utf-8
import os,sys
import gconf
import MySQLdb

def log(sfile):
	_rt = []
	d = {}
	'''
	打开文件把数据读入到字典里面用ip,url,返回值组成元组作为key。
	先把所有key赋空值，发现key在字典里面就把value加1。直到循环完成
	'''

	with open(sfile,'r') as f:
	    for line in f.readlines():
	        linelist = line.strip().split(' ')
	        dfile = linelist[0],linelist[6],linelist[8]
	        d.setdefault(dfile,0)
	        d[dfile] = d.setdefault(dfile,0) + 1

	# 把字典转换成列表
	dl = d.items()

	# 利用lambda函数 指定key排序
	dl2 = sorted(dl,key=lambda dl:dl[1])


	for lines in dl2:
		line = lines[0][0],lines[0][1],lines[0][2],lines[1]  #把每条数据作为一个元组
		_rt.append(line)	#添加到列表里面

	return _rt


#查询数据库数据
def fetch_accesslog(topn=10):
	sql = 'select * from accesslog order by num desc limit %s'
	args=(int(topn),)

	_count,_rt_list = execute_accesslog_sql(sql,args=args,fetch=True)  #从数据库获取信息

	return _rt_list

#写入数据库
def execute_commit_sql(sfile):
	loginfo = log(sfile)
	sql = 'insert into accesslog (ip,url,code,num) values(%s,%s,%s,%s)'

	execute_accesslog_sql(sql,args=loginfo,fetch=False)


def execute_accesslog_sql(sql,args=(),fetch=True):
	_count=0
	_rt_list=[]
	
	_conn = MySQLdb.connect(host=gconf.MYSQL_HOST,port=gconf.MYSQL_PORT, \
			db=gconf.MYSQL_DB,user=gconf.MYSQL_USER, passwd=gconf.MYSQL_PASSWORD,charset=gconf.MYSQL_CHARSET)
	_cur = _conn.cursor()
	
	if fetch:	
		print type(args)
		_count =_cur.execute(sql,args)	#查询
		_rt_list = _cur.fetchall()	#获取数据
		_cur.close()
		_conn.close()

	else:	
		print type(args)
		_count = _cur.executemany(sql,args)  #批量插入数据args是个list 每个值是一个元组。元组里面包含 ip，url，code ，num
		_conn.commit()
		_cur.close()
		_conn.close()

	return _count,_rt_list

if __name__ == '__main__':
	execute_commit_sql(sfile='log')

