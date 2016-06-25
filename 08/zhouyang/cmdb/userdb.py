#!/bin/env python
#coding:utf-8
import uconf
import MySQLdb
from db_act import db_act

def get_users():
    _rt=[]
    user_form=['id','username','password','age']
    _sql="select * from user;"
    cnt,user_list=db_act(_sql)
    for line in user_list:
        _rt.append(dict(zip(user_form,line)))
    return _rt

def get_user(username):
    _sql="select count(1) from user where username=%s;"
    args=username
    db_cnt,rt_list=db_act(_sql,args)
    return db_cnt != 0

def check_user(username,password):
    _sql="select * from user where username=%s and password=md5(%s)"
    args=(username,password)
    db_cnt,rt_list=db_act(_sql,args)
    return db_cnt != 0

def valid_user(username,userpasswd,admin_name,admin_passwd):
    if check_user(admin_name,admin_passwd):
        if get_user(username):
            if len(userpasswd) < 6:
                return False,"用户密码长度必须不小于6位"
            return True,''
    return False,"管理员密码错误"
