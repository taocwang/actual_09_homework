#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by Nick on 2016/5/29日17点
import MySQLdb as mysql
import gconf

def execute_sql(sql, args=(), args_list=[], fetch=True):
    _conn = None
    _cur = None
    _count = 0
    _rt_list = []
    try:
        # print sql,args_list
        _conn = mysql.connect(host=gconf.MYSQL_HOST,port=gconf.MYSQL_PORT,\
                              user=gconf.MYSQL_USER,passwd=gconf.MYSQL_PASSWD,\
                              db=gconf.MYSQL_DB,charset=gconf.MYSQL_CHARSET)
        _cur = _conn.cursor()
        if fetch == True:
            _count = _cur.execute(sql, args)
            _rt_list = _cur.fetchall()
        elif type(fetch) == type(''):
            for _args in args_list:
                _count = _cur.execute(sql, args=(_args[0][0], _args[0][1], _args[0][2], _args[1]))
            _conn.commit()
        else:
            _count = _cur.execute(sql, args)
            _conn.commit()
    except BaseException as e:
        print e
    finally:
        if _cur:
            _cur.close()
        if _conn:
            _conn.close()
    return _count, _rt_list