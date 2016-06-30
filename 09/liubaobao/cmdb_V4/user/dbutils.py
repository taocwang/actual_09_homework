#encoding:utf-8

import MySQLdb                                          #导入mysql的模块
import gconf                                            #导入数据的配置文件




def execute_fetch_sql(sql,args=(),fetch=True):          #查看数据库函数
    return execute_sql(sql,args,fetch)




def execute_commit_sql(sql,args=(),fetch=False):        #操作数据库函数
    return execute_sql(sql,args,fetch)




def execute_sql(sql,args=(),fetch=True):
    _conn = None                                        #使用变量前的好习惯,先给变量设置成默认值
    _cur = None
    _count = 0
    _rt_list = []                                       #给处理程序返回数据
    try:
        _conn = MySQLdb.connect(host=gconf.MYSQL_HOST,  #进行连接数据库,这些里面都是参数.包括(主机,端口,用户,密码,数据库,字符集)
                                port=gconf.MYSQL_PORT,
                                user=gconf.MYSQL_USER,
                                passwd=gconf.MYSQL_PASSWD,
                                db=gconf.MYSQL_DB,
                                charset=gconf.MYSQL_CHARSET)
        _cur = _conn.cursor()                           #设置指针
        _count = _cur.execute(sql,args)                 #进行提交处理数据库的sql和参数
        if fetch:                                       #判断数据是查看还不是其他的操作并进行sql的操作
            _rt_list = _cur.fetchall()
        else:
            _conn.commit()
    except BaseException as e:                          #进行异常处理
        print e
    finally:                                            #关闭数据库连接
        if _cur:
            _cur.close()
        if _conn:
            _conn.close()
    return _count, _rt_list                              #返回数据



def bulker_commit_sql(sql,args_list=[]):
    _conn =None
    _cur = None
    _count = 0
    _rt_list = []
    try:
        _conn = MySQLdb.connect(host=gconf.MYSQL_HOST,
                                port=gconf.MYSQL_PORT,
                                user=gconf.MYSQL_USER,
                                passwd=gconf.MYSQL_PASSWD,
                                db=gconf.MYSQL_DB,
                                charset=gconf.MYSQL_CHARSET)

        _cur = _conn.cursor()
        for _args in args_list:
            _count += _cur.execute(sql,_args)
        _conn.commit()
    except BaseException as e:
        print e
    finally:
        if _cur:
            _cur.close()
        if _conn:
            _conn.close()
    return _count, _rt_list



'''
测试代码
'''
if __name__ == '__main__':
    # sql = "insert into user(username,password,age) VALUES ('lbb','123',23)"
    # execute_commit_sql(sql)
    sql = "select * from user"
    print execute_fetch_sql(sql)