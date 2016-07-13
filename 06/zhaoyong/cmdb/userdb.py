#encoding: utf-8
import json

import gconf
import MySQLdb
from dbutils import execute_fetch_sql
from dbutils import execute_commit_sql

'''
获取用户信息
'''
def get_users():
    _columns = ('id','username','password','age')
    _sql = 'select * from user'
    _count,_rt_list = execute_fetch_sql(_sql)
    _rt = []

    for _line in _rt_list:
        _rt.append(dict(zip(_columns, _line)))
    print _rt
    return _rt

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
    #_sql = 'select * from user where username="{username}" and password=md5("{password}")'.format(username=username,password=password)
    _sql = 'select * from user where username=%s and password=md5(%s)'
    _count,_rt_list = execute_fetch_sql(_sql,(username,password))
    return _count != 0



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
    _sql = 'insert into user(username,password,age) values (%s,md5(%s),%s) '
    _args = (username,password,age)
    _count = execute_commit_sql(_sql,(username,password,age))

'''
获取用户信息
'''
def get_user(username):
    users = get_users()
    for user in users:
        if user.get('username') == username:
            return user

    return None

def get_user_id(id,fetch=True):
    _columns = ('id','username','password','age')
    _sql = 'select * from user where id=%s'
    _args = (id)
    _count, _rt_list = execute_fetch_sql(_sql,_args)
    _rt = []

    for _line in _rt_list:
        _rt.append(dict(zip(_columns, _line)))
    return _rt

#get_user_id(19)

'''
验证用户更新
'''
def validate_update_user(username, password, age,*args):
    #if get_user(username) is None:
    #    return False, u'用户信息不存在'

    if len(password) < 6:
        return False, u'密码长度至少为6位'

    if not str(age).isdigit() or int(age) < 0 or int(age) > 100:
        return False, u'年龄不正确'

    return True, ''

'''
更新用户信息
'''
def update_user(username, password, age, id):
    _sql = 'update user set username=%s,password=md5(%s),age=%s where id=%s'
    _args = (username,password,age,id)
    _count = execute_commit_sql(_sql,(username,password,age,id))


'''
删除用户信息
'''
def delete_user(id):
    _sql = 'delete from user where id=%s '
    _args = (id)
    _count = execute_commit_sql(_sql,_args)

'''
日志信息显示
'''
def accesslog(topn):
    _columns = ('count','url','ip','code')
    _sql = 'select * from accesslog limit %s'
    _args = (topn)
    _count, _rt_list = execute_fetch_sql(_sql,_args)
    _rt = []

    for _line in _rt_list:
        _rt.append(dict(zip(_columns, _line)))
    return _rt


if __name__ == '__main__':
    print accesslog(1)
    # update_user('aa','123456',88,18)
    #get_userid("aa")
    #print get_userid()
    #print validate_login('kk', '123456')
    #print validate_login('kk', '1234567')
    #print validate_login('woniu', '123456')
    #username = 'woniu1'
    #password = '123456'
    #age = '28'
    #_is_ok, _error = validate_add_user(username, password, age)
    #if _is_ok:
    #    add_user(username, password, age)
    #else:
    #    print _error
#
    #print delete_user('woniu2')
    #print validate_update_user('woniu2', password, age)[1]
    #print validate_update_user('kk', password, 'ac')[1]
    #_is_ok, _error = validate_update_user('kk', password, 30)
    #if _is_ok:
    #    update_user('kk', 'abcdef', 31)
