#encoding: utf-8
import MySQLdb
import json
import base64
#
from gconfig import gconfig

from functools import wraps
from flask import session ,redirect
from dbutils import excute_fetch_sql,exectue_commit_sql

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
    # try:
    #     handler = open(gconfig.USER_FILE, 'rb')
    #     cxt = handler.read()
    #     handler.close()
    #     return json.loads(cxt)
    #
    # except BaseException as e:
    #     print e
    #     return []

def validate_login(username,password):
    _sql = 'select * from user where username = %s and password = md5(%s)'
    args = (username,password)
    sql_count, rt_list = excute_fetch_sql(_sql,args)
    return sql_count != 0
    # users = get_user()
    # for user in users:
    #     if user.get('username') == username and user.get('password') == password:
    #         return True
    # return False


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
    exectue_commit_sql(_sql_insert,args2)
    return True


    # users = get_user()
    # username = params.get('username', '')
    # for user in users:
    #     if user.get('username') == username:
    #         return False
    # # json.dumps(a)   字典转化成字符串
    # # json.loads(a)   字符串转化成字典
    # new_users = json.dumps(params)  # 将新建用户信息转换为列表
    # users = get_user()
    # users.append(json.loads(new_users))
    # if user_write(users):
    #     return True
    # else:
    #     return False


def user_del(username):
    users = get_user()
    [users.remove(x) for x in users if x.get('username') == username]
    if user_write(users):
        return True
    return False

def user_write(users):
    try:
        handler = open(gconfig.USER_FILE, 'wb')
        handler.write(json.dumps(users))  # 写文件需要将字典转化为字符串
        handler.close()
        return True
    except BaseException as e:
        print e
        return False

def user_update(params):
    users = get_user()
    new_users = json.dumps(params)
    new_users = json.loads(new_users)
    [users.remove(x) for x in users if x.get('username') == new_users.get('username')]
    users.append(new_users)
    if user_write(users):
        return True
    return False

