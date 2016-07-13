#encoding: utf-8

import MySQLdb

import gconf


def execute_sql(sql, args=(),fetch=True):
    _conn = None
    _cur = None
    _count = 0
    _rt_list = []
    try:
        #print sql
        _conn = MySQLdb.connect(host=gconf.MYSQL_HOST, port=gconf.MYSQL_PORT, \
                        user=gconf.MYSQL_USER, passwd=gconf.MYSQL_PASSWD, \
                        db=gconf.MYSQL_DB, charset=gconf.MYSQL_CHARSET)

        _cur = _conn.cursor()
        _count = _cur.execute(sql, args)
        if fetch is True:
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

    return _count, _rt_list

if __name__ == '__main__':
    _count,_rt_list = execute_sql('select * from user;')
    print _rt_list
