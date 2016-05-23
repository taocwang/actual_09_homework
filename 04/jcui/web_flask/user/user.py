#encoding: utf-8

import json
#
from gconfig import gconfig


# from ..gconfig import gconfig

def get_user():
    try:
        handler = open(gconfig.USER_FILE, 'rb')
        cxt = handler.read()
        handler.close()
        return json.loads(cxt)

    except BaseException as e:
        print e
        return []

def validate_login(username,password):
    users = get_user()
    for user in users:
        if user.get('username') == username and user.get('password') == password:
            return True
    return False


def user_add(params):
    users = get_user()
    username = params.get('username', '')
    for user in users:
        if user.get('username') == username:
            return False
    # json.dumps(a)   字典转化成字符串
    # json.loads(a)   字符串转化成字典
    new_users = json.dumps(params)  # 将新建用户信息转换为列表
    users = get_user()
    users.append(json.loads(new_users))
    if user_write(users):
        return True
    else:
        return False


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