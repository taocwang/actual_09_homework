#!encoding:utf-8

import MySQLdb
import gconf

def execute_sql(sql,args=(),fetch=True):
    _conn = None
    _cur = None
    _count = None
    _rt_list = []
    _rt =[]
    try:
        _conn = MySQLdb.connect(host=gconf.MYSQL_HOST,
                                port=gconf.MYSQL_PORT,
                                user=gconf.MYSQL_USER,
                                passwd=gconf.MYSQL_passwd,
                                db=gconf.MYSQL_DB,
                                charset=gconf.MYSQL_CHARSET)

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










