#!/usr/bin/env python
# -*- coding: utf-8 -*-

import MySQLdb
import gconf

def execute_fetch_sql(sql,args=(),fetch=True):
    return execute_sql(sql,args,fetch)

def execute_commit_sql(sql,args=(),fetch=False):
    return execute_sql(sql,args,fetch)

def execute_sql(sql,args=(),fetch=True):
    _conn,_cur,_count,_rt_list=None,None,0,[]
    try:
        print sql
        _conn=MySQLdb.connect(host=gconf.MYSQL_HOST,port=gconf.MYSQL_PORT,user=gconf.MYSQL_USER,\
                              passwd=gconf.MYSQL_PASSWD,db=gconf.MYSQL_DB,charset=gconf.MYSQL_CHARSET)
        _cur=_conn.cursor()
        _count=_cur.execute(sql,args)
        if fetch:
            _rt_list=_cur.fetchall()
        else:
            _conn.commit()
    except BaseException as e:
        print "ERROR:"+str(e)
    finally:
        if _cur:
            _cur.close()
        if _conn:
            _conn.close()
    if fetch:
        return _count,_rt_list
    else:
        return _count

def execute_aggregation_sql(sql,args_list):
    _conn,_cur,_count,_rt_list=None,None,0,[]
    try:
        print sql
        _conn=MySQLdb.connect(host=gconf.MYSQL_HOST,port=gconf.MYSQL_PORT,user=gconf.MYSQL_USER,\
                              passwd=gconf.MYSQL_PASSWD,db=gconf.MYSQL_DB,charset=gconf.MYSQL_CHARSET)
        _cur=_conn.cursor()
        for i in range(0,len(args_list)):
            args=(args_list[i][1],args_list[i][0][0],args_list[i][0][1],args_list[i][0][2])
            _count+=_cur.execute(sql,args)
        _conn.commit()
    except BaseException as e:
        print "ERROR:"+str(e)
    finally:
        if _cur:
            _cur.close()
        if _conn:
            _conn.close()
    return _count