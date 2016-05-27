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

def modify_user(username,password,age):
    new_user = {'username':username,'password':password,'age':age}
    users = get_user()
    """"
   遍历用户，判断将要修改的用户名是否存在于数据库中. 存在，如果信息没变化，则提示用户，信息没变化；如果除了用户名之外的信息有修改，则会新增一条记录，所以要记得把老记录删掉；如果用户不存在，则直接新增用户。
    """
    for user in users:
    #用户信息完全一致，则返回same，提示用户，没有任何修改
        if user.get('username') == username and user.get('age') == age and user.get('password') == password:
            return "same"
    #如果只有除了用户名之外的信息修改，则直接修改用户信息,同时要记得把老的记录删除
        elif user.get('username') == username:
            user['username'] = username
            user['password'] = password
            user['age']  = age
            return 'flag'
    #否则，直接添加新的用户信息
    else:
        users.append(new_user)
    user_list = json.dumps(users)
    try:
        with open(gconf.DB_FILE,'w+') as f:
            f.write(user_list)
        return True
    except Exception as e:
        print e
        return False

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
    try:
        del users[users.index(del_user)]
        user_list = json.dumps(users)
        with open(gconf.DB_FILE,'w+') as f:
            f.write(user_list)
        return True
    except Exception as e:
        print e
        return False


def add_user(username,password,age):
    """
    添加用户。如果添加的用户名为空或重复，则提示用户；否则直接新增入库。
    """
    users = get_user()
    d={}
    for user in users:
        if user.get('username') == username or username == '':
            return False
    else:
        d['username'] = username
        d['password'] = password
        d['age'] =  age
        users.append(d)
    user_list = json.dumps(users)
    try:
        with open(gconf.DB_FILE,'w+') as f:
            f.write(user_list)
        return True
    except Exception as e:
        print e
        return False
            
def validate_login(username,password):
    """
    判断输入用户名和密码均正确。
    """
    users = get_user()
    for user in users:
         if user.get('username') == username and  user.get('password') == password:
             return True
    return False
