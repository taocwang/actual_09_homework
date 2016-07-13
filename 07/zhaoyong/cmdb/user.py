#encoding: utf-8
import json

import gconf

'''
获取用户信息
'''
def get_users():
    try:
        fhandler = open(gconf.USER_FILE, 'rb')
        cxt = fhandler.read()
        fhandler.close()
        return json.loads(cxt)
    except BaseException as e:
        print e
        return []

'''
保存用户信息
'''
def save_users(users):
    fhandler = open(gconf.USER_FILE, 'wb')
    fhandler.write(json.dumps(users))
    fhandler.close()

'''
进行用户登录验证
True/False: 用户名和密码验证成功/用户名或密码错误
如果有一个用户的username&password 与输入相同则登录成功
如果所有用户的username&password 与输入不相同则登录失败
'''
def validate_login(username, password):
    users = get_users()
    for user in users:
        if username == user.get('username') and password == user.get('password'):
            return True
    return False

'''
验证添加用户的信息
True/False, 描述信息
'''
def validate_add_user(username, password, age):
    users = get_users()
    for user in users:
        if user.get('username') == username:
            return False, u'用户名已经存在'

    if len(password) < 6:
        return False, u'密码长度至少为6位'

    if not str(age).isdigit() or int(age) < 0 or int(age) > 100:
        return False, u'年龄不正确'

    return True, ''


'''
添加用户信息
'''
def add_user(username, password, age):
    users = get_users()
    users.append({"username" : username, "password" : password, "age" : age})
    save_users(users)


'''
删除用户信息
'''
def delete_user(username):
    users = get_users()
    _idx = -1
    for user in users:
        _idx += 1
        if user.get('username') == username:
            _user = users.pop(_idx)
            save_users(users)
            return _user

    return None


'''
获取用户信息
'''
def get_user(username):
    users = get_users()
    for user in users:
        if user.get('username') == username:
            return user

    return None

'''
验证用户更新
'''
def validate_update_user(username, password, age):
    if get_user(username) is None:
        return False, u'用户信息不存在'

    if len(password) < 6:
        return False, u'密码长度至少为6位'

    if not str(age).isdigit() or int(age) < 0 or int(age) > 100:
        return False, u'年龄不正确'

    return True, ''

'''
更新用户信息
'''
def update_user(username, password, age):
    users = get_users()
    _idx = -1
    for user in users:
        _idx += 1
        if user.get('username') == username:
            users[_idx]['password'] = password
            users[_idx]['age'] = age
            #users[_idx].update({'password' : password, 'age' : age})
            save_users(users)

if __name__ == '__main__':
    print get_users()
    print validate_login('kk', '123456')
    print validate_login('kk', '1234567')
    print validate_login('woniu', '123456')
    username = 'woniu1'
    password = '123456'
    age = '28'
    _is_ok, _error = validate_add_user(username, password, age)
    if _is_ok:
        add_user(username, password, age)
    else:
        print _error

    print delete_user('woniu2')
    print validate_update_user('woniu2', password, age)[1]
    print validate_update_user('kk', password, 'ac')[1]
    _is_ok, _error = validate_update_user('kk', password, 30)
    if _is_ok:
        update_user('kk', 'abcdef', 31)
