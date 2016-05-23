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
    if user_update(params):
        return True
    else:
        return False


def user_del():
    pass


def user_update(params):
    # json.dumps(a)   字典转化成字符串
    # json.loads(a)   字符串转化成字典
    new_users = json.dumps(params)  #将新建用户信息转换为列表
    users = get_user()
    users.append(json.loads(new_users))
    try:
        handler = open(gconfig.USER_FILE, 'wb')
        handler.write(json.dumps(users))   #写文件需要将字典转化为字符串
        handler.close()
        return True
    except BaseException as e:
        print e
        return False