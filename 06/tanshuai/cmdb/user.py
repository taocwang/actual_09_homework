#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by Nick on 2016/5/29日15点53分
import dbutils

# 获取用户信息
def get_users():
    _columns = ('id','username','password','age')
    sql = 'select * from user'
    _count, _rt_list = dbutils.execute_sql(sql, args=())
    _rt = []
    for _list in _rt_list:
        _rt.append(dict(zip(_columns, _list)))
    return _rt

# 添加用户信息
def add_users(username, password, age):
    sql = 'insert into user(username, password, age) values(%s,md5(%s),%s)'
    args = (username, password, age)
    _count, _rt_list = dbutils.execute_sql(sql, args, fetch=False)
    return _count != 0

# 更新用户信息
def update_users(username, password, age, uid):
    sql = 'update user set username = %s ,password=md5(%s),age=%s where id=%s'
    args = (username, password, age, uid)
    _count, _rt_list = dbutils.execute_sql(sql, args, fetch=False)
    return _count != 0

# 删除用户信息
def del_users(uid):
    sql = 'delete from user where id=%s'
    _count, _rt_list = dbutils.execute_sql(sql, uid, fetch=False)
    return _count != 0

# 登录验证
def validate_login(username, password):
    sql = 'select * from user where username=%s and password=md5(%s)'
    _count, _rt_list = dbutils.execute_sql(sql, (username, password))
    return _count != 0

# 添加和更新用户验证
def validate_find(username):
    users = get_users()
    for user in users:
        if user.get('username') == username:
            return True
    return False
