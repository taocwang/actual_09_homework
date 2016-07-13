#!/bin/env python
#encoding:utf-8

import db_act

def username_check(username):
    _sql="select * from user where username=%s;"
    _args=(username,)
    _cnt,rt_list=db_act.db_act(_sql,_args)
    return _cnt

def user_passwd_check(username,in_passwd):
    _sql="select * from user where username=%s and password=md5(%s);"
    _args=(username,in_passwd)
    _cnt,rt_list=db_act.db_act(_sql,_args)
    print bool(rt_list)
    if _cnt == 0:
        return False,"用户密码校验失败，请输入正确密码！"
    return True,""

def update_user(username,passwd,newpasswd,try_passwd,age):
    _res,msg=user_passwd_check(username,passwd)
    if _res:
        if newpasswd == try_passwd:
            _sql="update user set password=md5(%s),age=%s where username=%s;"
            _args=(newpasswd,age,username)
            if db_act.db_act(_sql,_args,fetch=False):
                return True,"密码修改成功"
            return False,"密码修改失败，请联系管理员"
        return False,"两次输入的新密码不一致，请重新输入！"
    return _res,msg

def create_user(params):
    username=params.get('username')
    passwd=params.get('password')
    tr_passwd=params.get('try_password')
    age=params.get('age')
    birthday=params.get('birthday')
    if username_check(username) != 0:
        return False,"用户已存在！"
    elif passwd != tr_passwd:
        return False,"两次输入的密码不一致！"
    _sql="insert into user(username,password,age)values(%s,md5(%s),%s);"
    _args=(username,passwd,age)
    if db_act.db_act(_sql,_args,fetch=False):
        return True,'用户注册成功'
    else:
        return False,'用户录入失败，请联系管理员'