#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by Nick on 2016/5/29日15点53分
import dbutils

'''
添加用户信息
返回值: True/False
'''
def add_users(username, password, age):
    sql = 'insert into user(username, password, age) values(%s,md5(%s),%s)'
    args = (username, password, age)
    _count, _rt_list = dbutils.execute_sql(sql, args)
    return _count != 0

'''
删除用户信息
返回值: True/False
'''
def del_users(uid):
    sql = 'delete from user where id=%s'
    _count, _rt_list = dbutils.execute_sql(sql, uid)
    return _count != 0

'''
更新用户信息
返回值: True/False
'''
def update_users(uid, password, age):
    sql = 'update user set password=md5(%s),age=%s where id=%s'
    args = (password, age, uid)
    _count, _rt_list = dbutils.execute_sql(sql, args)
    return _count != 0

'''
查询用户信息
返回值: list[用户信息]/list[空]
'''
def get_users():
    _columns = ('id','username','password','age')
    sql = 'select * from user'
    _count, _rt_list = dbutils.execute_sql(sql, fetch=True)
    _rt = []
    for _list in _rt_list:
        _rt.append(dict(zip(_columns, _list)))
    return _rt

'''
用户登录验证
返回值: True/False
'''
def validate_login(username, password):
    sql = 'select * from user where username=%s and password=md5(%s)'
    _count, _rt_list = dbutils.execute_sql(sql, (username, password), fetch=True)
    return _count != 0

'''使用ID验证用户是否存在
返回值: username/None
'''
def get_user_id(uid):
    uid = int(uid)
    _users = get_users()
    for _user in _users:
        if _user.get('id') == uid:
            return _user
    return None

'''检查新建用户信息
返回值: True/False, 错误信息
'''
def validate_add_user(username, password, age):
    if username.strip() == '':
        return False, u'用户名不能为空'
    # 检查用户名是否重复
    users = get_users()
    for user in users:
        if user.get('username') == username:
            return False, u'用户名已存在'
    # 密码要求长度必须大于6位
    if len(password) < 6:
        return False, u'密码长度必须大于6位'
    # 年龄要求0到100的整数
    if not str(age).isdigit() or int(age) <= 0 or int(age) > 100:
        return False, u'年龄必须是0到100的整数'
    return True, ''

'''检查更新用户信息
返回值: True/False, 错误信息
'''
def validate_update_user(uid, musername, mpassword, password, age):
    if not validate_login(musername, mpassword):
        return False, u'管理员密码错误'
    # 检查用户名是否重复
    if get_user_id(uid) is None:
        return False, u'用户信息不存在'
    # 密码要求长度必须大于6位
    if len(password) < 6:
        return False, u'密码长度必须大于6位'
    # 密码要求长度必须大于6位
    if not str(age).isdigit() or int(age) <= 0 or int(age) > 100:
        return False, u'年龄必须是0到100的数字'
    return True, ''


if __name__ == '__main__':
    print get_user_id(20)