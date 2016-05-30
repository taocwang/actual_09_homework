#encoding: utf-8
import MySQLdb
import json
import base64
#
from gconfig import gconfig

from functools import wraps
from flask import session ,redirect
from dbutils import excute_fetch_sql,excute_commit_sql,excute_update_sql,excute_delete_sql

#定义装饰器函数,为了检查是否处于登陆状态
def login_check(func):
    @wraps(func)       #为了解决python多装饰器出现的bug
    def check(*args,**kwargs):
        if session.get('username') is None:
            return redirect('/')
        rt = func(*args,**kwargs)
        return rt  #返回函数的值
    return check   #返回内层函数的结果


def get_user():
    colloens = ('username','password','age','telphone','email')
    _sql = 'select username,password,age,telphone,email from user'
    rt = []
    sql_count,rt_list = excute_fetch_sql(_sql)
    for i in rt_list:
        rt.append(dict(zip(colloens,i)))
    return rt


def get_alone_user(username):
    users = get_user()
    for i in users:
        if i.get('username') == username:
            return i
    return None


def validate_login(username,password):
    _sql = 'select * from user where username = %s and password = md5(%s)'
    args = (username,password)
    sql_count, rt_list = excute_fetch_sql(_sql,args)
    return sql_count != 0


def user_add(params):
    username = params.get('username')
    password = params.get('password')
    age = params.get('age')
    telphone = params.get('telphone')
    email = params.get('email')
    _sql_select = 'select * from user where username = %s'
    _sql_insert = 'insert into user(username,password,age,telphone,email) values(%s,md5(%s),%s,%s,%s)'
    agrs1 = (username,)
    _sql_count,rt_list = excute_fetch_sql(_sql_select,agrs1)
    if _sql_count != 0:
        return False
    args2 = (username,password,age,telphone,email)
    excute_commit_sql(_sql_insert,args2)
    return True

def user_del(username):
    _sql = 'delete from user where username=%s'
    args = (username,)
    _sql_count, rt_list = excute_update_sql(_sql, args)
    if _sql_count != 0:
        return True
    return False

def user_update(params):
    username = params.get('username')
    password = params.get('password')
    age = params.get('age')
    telphone = params.get('telphone')
    email = params.get('email')
    _sql = 'update user set password=md5(%s) ,age=%s ,telphone=%s ,email=%s where username=%s'
    args = (password,age,telphone,email,username)
    _sql_count, rt_list = excute_update_sql(_sql,args)
    if _sql_count != 0:
        return True
    return False


