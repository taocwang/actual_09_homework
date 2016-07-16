#encoding: utf-8
import json

import MySQLdb

import gconf
from dbutils import execute_fetch_sql, execute_commit_sql


'''获取所有用户的信息
返回值: [
            {"username" : "kk", "password" : "123456", "age" : 29},
            {"username" : "woniu", "password" : "abcdef", "age" : 28}
        ]
'''
def get_users(wheres=[]):
    _columns = ('id', 'username', 'password', 'age')
    _sql = 'select * from user where 1=1'
    _args = []
    for _key, _value in wheres:
        _sql += ' AND {key} = %s'.format(key=_key)
        _args.append(_value)

    _count, _rt_list = execute_fetch_sql(_sql, _args)
    _rt = []
    for _line in _rt_list:
        #(6L, u'kk4', u'e10adc3949ba59abbe56e057f20f883e', 29L)
        _rt.append(dict(zip(_columns, _line)))
    return _rt


'''验证用户名，密码是否正确
返回值: True/False
'''
def validate_login(username, password):

    #_sql = 'select * from user where username="{username}" and password=md5("{password}")'.format(username=username, password=password)
    print username, password
    _sql = 'select * from user where username=%s and password=md5(%s)'
    _count, _rt_list = execute_fetch_sql(_sql, (username, password))
    return _count != 0


'''检查新建用户信息
返回值: True/False, 错误信息
'''
def validate_add_user(username, password, age):
    if username.strip() == '':
        return False, u'用户名不能为空'

    #检查用户名是否重复
    #get_user_by_name()
    if get_user_by_name(username):
        return False, u'用户名已存在'

    #密码要求长度必须大于等于6
    if len(password) < 6:
        return False, u'密码必须大于等于6'

    if not str(age).isdigit() or int(age) <= 0 or int(age) > 100:
        return False, u'年龄必须是0到100的数字'

    return True, ''


'''添加用户信息
'''
def add_user(username, password, age):
    _sql = 'insert into user(username, password, age) values(%s, md5(%s), %s)'
    _args = (username, password, age)
    execute_commit_sql(_sql, _args)


'''获取用户信息
'''
def get_user(uid):
    _rt = get_users([('id', uid)])
    return _rt[0] if len(_rt) > 0 else None
    '''
    _columns = ('id', 'username', 'password', 'age')
    _sql = 'select * from user where id = %s'
    _count, _rt_list = execute_fetch_sql(_sql, (uid, ))
    _rt = []
    for _line in _rt_list:
        _rt.append(dict(zip(_columns, _line)))
    return _rt[0] if len(_rt) > 0 else None
    '''


'''检查更新用户信息
返回值: True/False, 错误信息
'''
def validate_update_user(uid, username, password, age):
    if get_user(uid) is None:
        return False, u'用户信息不存在'

    # if username.strip() == '':
    #     return False, u'用户名不能为空'

    # _user = get_user_by_name(username)
    # if _user and _user.get('id') != int(uid):
    #     return False, u'用户名已存在'

    #密码要求长度必须大于等于6
    # if len(password) < 6:
    #     return False, u'密码必须大于等于6'

    if not str(age).isdigit() or int(age) <= 0 or int(age) > 100:
        return False, u'年龄必须是0到100的数字'

    return True, ''


'''更新用户信息
'''
def update_user(uid, username, password, age):
    _sql = 'update user set age=%s where id=%s'
    execute_commit_sql(_sql, (age, uid))

'''删除用户信息
'''
def delete_user(uid):
    _sql = 'delete from user where id=%s'
    execute_commit_sql(_sql, (uid, ))

def get_user_by_name(username):
    _rt = get_users([('username', username)])
    return _rt[0] if len(_rt) > 0 else None
    '''
    _columns = ('id', 'username', 'password', 'age')
    _sql = 'select * from user where username = %s'
    _count, _rt_list = execute_fetch_sql(_sql, (username, ))
    _rt = []
    for _line in _rt_list:
        _rt.append(dict(zip(_columns, _line)))
    return _rt[0] if len(_rt) > 0 else None
    '''

def validate_charge_user_password(uid, upassword, musername, mpassword):
    #检查管理员密码是否正确
    if not validate_login(musername, mpassword):
        return False, '管理员密码错误'

    if get_user(uid) is None:
        return False, u'用户信息不存在'

    #密码要求长度必须大于等于6
    if len(upassword) < 6:
        return False, u'密码必须大于等于6'

    return True, ''



def charge_user_password(uid, upassword):
    _sql = 'update user set password=md5(%s) where id=%s'
    print _sql, uid, upassword
    execute_commit_sql(_sql, (upassword, uid)) 

if __name__ == '__main__':
    # _is_ok, _error = validate_add_user('ada', 'ada23', 26)
    # print _is_ok, _error
    # _is_ok, _error = validate_add_user('ada1', 'ada23', 26)
    # print _is_ok, _error
    # _is_ok, _error = validate_add_user('ada1', 'ada2d3', 'abc')
    # print _is_ok, _error
    # _is_ok, _error = validate_add_user('xiaoxia', 'ada2d3', 26)
    # if _is_ok:
    #     add_user('xiaoxia', 'ada2d3', 26)
    # print get_users()
    # print get_user('kk')
    # update_user('kk', 'abcdef', 30)
    # print get_user('kk')
    # print get_user('kk2')

    _is_ok, _error = validate_update_user('ada', 'ada23', 26)
    print _is_ok, _error
    _is_ok, _error = validate_update_user('ada1', 'ada23', 26)
    print _is_ok, _error
    _is_ok, _error = validate_update_user('ada1', 'ada2d3', 'abc')
    print _is_ok, _error
    _is_ok, _error = validate_update_user('xiaoxia', 'ada2d3', 26)
    print _is_ok, _error
