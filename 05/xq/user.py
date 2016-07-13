#!/usr/bin/env python
# coding=utf-8


import gconf
import json

def get_user():
    """
   获取所有用户信息，并返回

    """
    try:
        with open(gconf.DB_FILE,'rb') as f:
            cxt = f.read()
        return json.loads(cxt)
    except Exception as e:
        print e
        return False

def save_user(user_list):
    try:
        with open(gconf.DB_FILE,'w+') as f:
            f.write(user_list)
        return True
    except Exception as e:
        print e
        return False

def modify_user(username,password,age):
    new_user = {'username':username,'password':password,'age':age}
    users = get_user()
    """"
   判断用户名是否存在于数据库中. 若存在，且信息没变化，则提示用户没有变化;否则新增一条记录。
    """
    #判断username已存在数据库中
    for user in users:
    #用户信息没变化
        if user == new_user:
            return 'same'
    #用户已存在数据库
        elif new_user.get('username') == user.get('username'):
            return "flag"
    else:
        users.append(new_user)
    user_list = json.dumps(users)
    save_user(user_list)

def find_user(username):
    """
    模糊查找，输入的用户名为任意一条记录的子集，则匹配。
    """
    users = get_user()
    new_users = []
    flag = 0
    for user in users:
        if username.strip() in user.get('username') :
            new_users.append(users[users.index(user)])
            flag +=1
    if flag>0:
        return new_users
    else:
        return False

def del_user(username,password,age):
    """
    构造出将要删除的用户信息，然后直接del。
    """
    users = get_user()
    del_user = {'username':username,'password':password,'age':age}
    del users[users.index(del_user)]
    user_list = json.dumps(users)
    save_user(user_list)

def add_user(username,password,age):
    """
    添加用户。如果添加的用户名为空或重复，则提示用户；否则直接新增入库。
    """
    users = get_user()
    d={}
    for user in users:
        if user.get('username') == username or username == '':
            return False
    #if len(password) <6:
    #    return False,u'密码长度至少为6位'
    #if not str(age).isdigit() or int(age) <0 or int(age) >150:
    #    return False,u'年龄不正确'
    else:
        d['username'] = username
        d['password'] = password
        d['age'] =  age
        users.append(d)
    user_list = json.dumps(users)
    save_user(user_list)

def validate_login(username,password):
    """
    判断输入用户名和密码均正确。
    """
    users = get_user()
    for user in users:
         if user.get('username') == username and  user.get('password') == password:
             return True
    return False
