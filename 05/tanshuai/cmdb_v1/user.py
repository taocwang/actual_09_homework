#!/usr/bin/env python
# -*- coding: utf-8 -*-
import gconf
import json

# 获取用户信息
def get_users():
    try:
        handler = open(gconf.USER_FILE, 'rb')
        cxt = handler.read()
        handler.close()
        return json.loads(cxt)
    except:
        return []

# 添加用户信息
def add_users(username, age, password):
    # 获取新用户数据
    newUser = {'username': username, 'age': age, 'password': password}
    # 获取旧用户数据
    srcUsers = get_users()
    if srcUsers:
        # 将新旧用户数据添加到一个list列表中，并做json格式转换
        srcUsers.append(newUser)
        newUsers = json.dumps(srcUsers)
        try:
            # 写入文件
            handler = open(gconf.USER_FILE, 'wb')
            handler.write(newUsers)
            handler.close()
            return True
        except:
            return False
    else:
        return False

# 更新用户信息
def update_users(username, age, password):
    # 获取user.json文件用户信息
    srcUsers = get_users()
    # 判断srcUsers为空则返回False，不为空则获取更新用户所在的索引位置
    if srcUsers:
        index = 0
        for user in get_users():
            if user.get("username") == username:
                break
            index += 1
    else:
        return False
    # 更新用户操作部分
    try:
        # 获取需要更新的用户旧数据
        upUser = srcUsers.pop(index)
        # 更新用户对应属性
        upUser['age'] = int(age)
        upUser['password'] = password
        # 将更新的新用户数据加入到源数据列表
        srcUsers.append(upUser)
        # 将源数据列表写入user.json文件
        handler = open(gconf.USER_FILE, 'wb')
        handler.write(json.dumps(srcUsers))
        handler.close()
        return True
    except:
        return False

# 删除用户信息
def del_users(username):
    # 获取user.json文件用户信息
    srcUsers = get_users()
    # 判断srcUsers为空则返回False，不为空则获取更新用户所在的索引位置
    if srcUsers:
        index = 0
        for user in get_users():
            if user.get("username") == username:
                break
            index += 1
    else:
        return False
    # 删除用户操作部分
    try:
        # 删除用户
        srcUsers.pop(index)
        # 将源数据列表写入user.json文件
        handler = open(gconf.USER_FILE, 'wb')
        handler.write(json.dumps(srcUsers))
        handler.close()
        return True
    except:
        return False

# 验证用户名和密码是否重复
def validate_login(username, password):
    users = get_users()
    for user in users:
        if user.get('username') == username and user.get('password') == password:
            return True
    return False

# 验证用户名是否重复
def validate_find(username):
    users = get_users()
    for user in users:
        if user.get('username') == username:
            return True
    return False

# 测试代码块
username = 'tan'
age = '32'
password = '234234'
if __name__ == '__main__':
    # print validate_login('kk', '123123')
    # print validate_find('nick')
    # print add_users(username, age, password)
    # print update_users(username, age, password)
    print del_users(username)