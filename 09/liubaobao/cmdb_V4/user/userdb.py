#encoding:utf-8

from dbutils import execute_commit_sql,execute_fetch_sql    #导入操作数据库的模块函数




'''
获取用户列表
'''
def get_users():
    _counlms = ('id','username','password','age')           #组成一个字典的元组
    _sql = "select * from user"
    args = ()
    _rt = []
    _count,_rt_list = execute_fetch_sql(_sql,args)
    if _count:
        for line in _rt_list:
            _rt.append(dict(zip(_counlms,line)))            #利用zip函数来组成字典
        return _rt




'''
另外一种获取用户列表的方法
'''
def get_users_2(wheres=[]):
    _columns = ('id', 'username', 'password', 'age')
    _sql = "select * from user where 1=1"
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




'''
通过用户名进行查找用户
'''
def get_user_by_name(username):
    _coulmns = ('id','username','password','age')
    _sql = "select * from user where username = %s"
    args = (username,)
    _count,_rt_list = execute_fetch_sql(_sql,args)
    _rt = []
    for line in _rt_list:
        _rt.append(dict(zip(_coulmns,line)))
    return _rt[0] if len(_rt)>0 else None




'''
通过用户id进行查找用户
'''
def get_user_by_uid(uid):
    _coulmns = ('id','username','password','age')
    _sql = "select * from user where id = %s"
    args=(uid,)
    _count,_rt_list = execute_fetch_sql(_sql,args)
    _rt = []
    for line in _rt_list:
        _rt.append(dict(zip(_coulmns,line)))
    return _rt[0] if len(_rt)>0 else None



'''
验证用户登录
'''
def validate_login(username,password):
    _sql = "select * from user where username=%s and password=md5(%s)"
    args = (username,password)
    _count,_rt_list = execute_fetch_sql(_sql,args)
    #return _count != 0
    if _count:
        return True
    else:
        return False




'''
验证用户添加验证
'''
def validate_add_user(username,password,age):
    if str(username).strip() == '':
        return False,u'用户名为空'
    if len(password) < 6:
        return False,u'密码不能少于6位'
    if not str(age).isdigit() or int(age) > 100 or int(age) < 0:
        return False,u'年龄不符合规则'
    if get_user_by_name(username):
        return False,u'用户名已存在'
    return True,''




'''
用户添加
'''
def add_user(username,password,age):
    _sql = "insert into user(username,password,age) values(%s,md5(%s),%s)"
    args = (username,password,age)
    execute_commit_sql(_sql,args)



'''
验证更新用户
'''
def validate_update_user(uid,username,passwod,age):
    if get_user_by_uid(uid) is None:
        return False,u'用户信息不存在啊!'
    if username.strip() == '':
        return False,u'用户名不能为空!'
    # _user = get_user_by_name(username)
    # if _user and _user.get('id') != int(uid):
    #     return False,u'用户名信息已经存在!'
    # if len(passwod) < 6:
    #     return False,u'密码不能小于6位'

    if not str(age).isdigit() or int(age) <=0 or int(age) > 100:
        return False,'年龄必须是100区间以内的数字'
    return True,''




'''
更新用户
'''
def update_user(uid,username,password,age):
    _sql = 'update user set age=%s,password=md5(%s),username=%s where id=%s'
    args = (age,password,username,uid)
    execute_commit_sql(_sql,args)




'''
删除用户
'''
def delete_user(uid):
    _sql = "delete from user where id = %s"
    args=(uid,)
    execute_commit_sql(_sql,args)



'''
修改用户密码弹窗验证操作
'''
def validate_change_user_password(uid,upassword,musername,mpassword):
    if not validate_login(musername,mpassword):
        return False, u'管理员密码错误!'
    if get_user_by_uid(uid) is None:
        return False, u'用户信息不存在!'
    if len(upassword) < 6:
        return False, u'密码不能小于6位'
    return True, ''


'''
修改用户密码弹窗更改密码操作
'''
def change_user_password(uid,upassword):
    _sql = 'update user set password=md5(%s) where id=%s'
    execute_commit_sql(_sql, (upassword, uid))




'''
添加用户弹窗操作验证
'''
def validate_create_user(username,password,age):
    if get_user_by_name(username):
        return False, '用户名已经存在'
    if len(password) < 6:
        return False, '密码不能小于6位'
    if not str(age).isdigit() or int(age) <=0 or int(age) > 100:
        return False, '年龄必须是100区间以内的数字'
    return True,''

'''
添加用户弹窗操作
'''
def create_user(username,password,age):
    _sql = "insert into user(username,password,age) values(%s,md5(%s),%s)"
    execute_commit_sql(_sql, (username, password, age))



'''
更新用户验证弹窗操作
'''
def validate_update_user(id,username,age):
    if get_user_by_uid(id) is None:
        return False, u'用户信息不存在'
    if str(username).strip() == '':
        return False, u'用户名不能为空'
    if not str(age).isdigit() or int(age) <=0 or int(age) > 100:
        return False, '年龄必须是100区间以内的数字'
    return True,''




'''
更新用户信息弹窗操作
'''
def update__user(id,username,age):
    _sql = "update user set username=%s,age=%s where id=%s"
    execute_commit_sql(_sql,(username,age,id))



'''
测试代码
'''
if __name__ == '__main__':
    print get_users()
    print validate_login('lbb','123456')
    print get_user_by_name('kk')
    print get_user_by_uid(1)