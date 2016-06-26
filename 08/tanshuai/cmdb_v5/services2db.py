#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by Nick on 2016/6/13日13点13分
# 建库SQL语句
# create table service_manage (
#   id int primary key auto_increment,
# 	domain_name varchar(128),
# 	username text,
# 	password text,
# 	function text
# )default charset=utf8;
import dbutils

'''获取域名管理信息
返回值: True/False
'''
def get_service():
    _columns = ('id', 'domain_name', 'username', 'password', 'function')
    _sql = 'select * from service_manage'
    _count, _rt_list = dbutils.execute_sql(_sql, fetch=True)
    _rt = []
    for _list in _rt_list:
        _rt.append(dict(zip(_columns, _list)))
    return _rt

'''删除数据
返回值: True/False
'''
def servicedel(uid):
    sql = 'delete from service_manage where id=%s'
    _count, _rt_list = dbutils.execute_sql(sql, uid)
    return _count != 0

'''更新数据
返回值: True/False
'''
def update_service(_url, _username, _password, _func, _id):
    sql = 'update service_manage set domain_name=%s, username=%s, password=%s, function=%s where id=%s'
    args = (_url, _username, _password, _func, _id)
    _count, _rt_list = dbutils.execute_sql(sql, args)
    return _count != 0

'''添加数据
返回值: True/False
'''
def add_service(_url, _username, _password, _func):
    sql = 'insert into service_manage(domain_name,username,password,function) values(%s,%s,%s,%s)'
    args = (_url, _username, _password, _func)
    _count, _rt_list = dbutils.execute_sql(sql, args)
    return _count != 0