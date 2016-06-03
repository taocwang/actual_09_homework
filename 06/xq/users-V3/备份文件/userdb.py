#encoding: utf-8
from dbutils import execute_sql
import hashlib

'''获取所有用户的信息
返回值: [
            {"username" : "kk", "password" : "123456", "age" : 29},
            {"username" : "woniu", "password" : "abcdef", "age" : 28}
        ]
'''
'''
def get_users():
    _sql = 'select * from user;'
    _columns = ('id','username','password','age')
    _rt = []
    _count, _rt_list = execute_sql(_sql,fetch=True)
    for _line in _rt_list:
        _rt.append(dict(zip(_columns, _line)))
    return _rt


获取日志信息

def get_logs(count):
    _sql = 'select * from logs limit %s;'
    _args = (int(count),)
    _columns = ('id','ip','url','code','cnt')
    _rt = []
    _count, _rt_list = execute_sql(_sql,_args,fetch=True)
    for _line in _rt_list:
        _rt.append(dict(zip(_columns, _line)))
    #print _rt
    return _rt


获取自定义sql语句

def get_sql(sql):
    _sql = sql
    for i in _sql.split():
        if i in ['drop','delete']:
            return False,u'sql语句中有危险操作！'
    _columns = ('id','ip','url','code','cnt')
    _rt = []
    _count, _rt_list = execute_sql(_sql,fetch=True)
    for _line in _rt_list:
        _rt.append(dict(zip(_columns, _line)))
    #print _rt
    return _rt,''
'''

'''
说明：这个函数只有一个功能：获取指定条件的记录
从数据库中获取信息：
1.获取危险操作的sql，比如包括delete、drop字段的sql语句
返回值：（True/False,错误提示）

2.获取任意指定条数的log
通过在输入框输入log条数进行查询

3.获取指定id的用户信息，id是唯一的

4.通过username获取用户信息：这里有问题，username可能不唯一；
但是，可以作为判断是否已存在同名记录，此时id如果不同，就判断有重名

5.获取所有用户信息列表
返回值: [
            {"username" : "kk", "password" : "123456", "age" : 29},
            {"username" : "woniu", "password" : "abcdef", "age" : 28}
        ]
'''
def get_info(_sql=None,_count=None,_user=None,_id=None,username=None,_args=()):

    _rt = []
    if _sql:
        #_sql = sql
        _columns = ('id','ip','url','code','cnt')
        for i in _sql.split():
            if i in ['drop','delete']:
                return False,u'sql语句中有危险操作！'
    elif _count:
        _sql = 'select * from logs limit %s;'
        _columns = ('id','ip','url','code','cnt')
        _args = (int(_count),)
        _count = _count
    elif _id:
        _sql = 'select * from user where id=%s;'
        _args = (_id,)
        _columns = ('id','username','password','age')
    elif username:
        _sql = 'select * from user where username=%s;'
        _args = (username,)
        _columns = ('id','username','password','age')
    else:
        _columns = ('id','username','password','age')
        _sql = 'select * from user;'
    _cnt, _rt_list = execute_sql(_sql,_args,fetch=True)
    for _line in _rt_list:
        _rt.append(dict(zip(_columns, _line)))
    #print _rt
    return _rt,''


'''验证用户名，密码是否正确
返回值: True/False
'''
def validate_login(username, password):
    _sql = 'select * from user where username=%s and password=md5(%s)'
    _cnt, _rt_list = execute_sql(_sql, (username, password),fetch=True)
    if _cnt:
        return True


'''检查新建用户信息
返回值: True/False, 错误信息
'''
def validate_add_user(username, password, age):
    if username.strip() == '':
        return False, u'用户名不能为空'

    #检查用户名是否重复
    #_users = get_users()
    _users,_error = get_info()
    for _user in _users:
        if username == _user.get('username'):
            return False, u'用户名已存在'

    #密码要求长度必须大于等于6
    if len(password) < 6:
        return False, u'密码必须大于等于6'

    if not str(age).isdigit() or int(age) <= 0 or int(age) > 150:
        return False, u'年龄必须是0到150的数字'

    return True, ''


'''添加用户信息
'''
def add_user(username, password, age):
    _sql = 'insert into user(username, password, age) values(%s, md5(%s), %s)'
    _args = (username, password, age)
    execute_sql(_sql, _args,fetch=False)


'''
获取用户信息根据username，由get_info（）函数整合了
'''
'''
def get_user(username=False,id=False):
    #_users = get_users()
    _users,_error = get_info()
    #print _users
    if username:
        for _user in _users:
            if _user.get('username') == username:
                return _user
        return None
    elif id:
        for _user in _users:
            if _user.get('id') == int(id):
                return _user
        return None
    else:
        return None
'''


'''
获取用户信息

[
     {'username': u'xuequn', 'age': 33L, 'password': u'6f3a650fbd8177b4b855d91ae097fb1e', 'id': 19L},
     {'username': u'admin', 'age': 23L, 'password': u'51ab1ad11b85fd34cbeb29e7eb0e9c5d', 'id': 24L},
     {'username': u'laofang', 'age': 33L, 'password': u'6f3a650fbd8177b4b855d91ae097fb1e', 'id': 36L}

 ]
'''
'''
已被get_info(username)函数整合！

def find_user(username):
    #_users = get_users()
    _users,_error = get_info()
    new_users=[]
    flag = 0
    for _user in _users:
        if username in _user.get('username'):
            new_users.append(_user)
            flag +=1
    if flag>0:
        return new_users
    else:
        return []
'''

'''检查更新用户信息
返回值: True/False, 错误信息
还要增加一个同名用户，把ID加进去
'''
def validate_update_user(id,username, password, age):
    _users,_error = get_info(username=username)                          #根据更新时的id，提取用户记录
    #获取post的username用户信息，和数据库中的对比，如果有不同id拥有相同username，则提示已注册！
    for _user in _users:
        if _user['id'] != int(id):
            return False,u'用户已经注册，使用其他用户名'
        return True,''

    #if get_info(username=username) is not None:
     #   return False, u'用户信息不存在'

    #密码要求长度必须大于等于6
    if len(password) < 6:
        return False, u'密码必须大于等于6'

    if not str(age).isdigit() or int(age) <= 0 or int(age) > 100:
        return False, u'年龄必须是0到100的数字'

    return True, ''


'''
更新用户信息
id,username, password, age为POST数据
需要根据ID获取数据库中的username、password、age，然后和post数据对比，有变化的进行修改！
'''
def update_user(id,username, password, age):
    _users,_error = get_info(_id=id)
    print _users
    _username = _users[0]['username']
    _password = _users[0]['password']
    _age = _users[0]['age']

    #password = hashlib.md5(password).hexdigest()
    print "new post %s" %(password)
    print "old %s" %(_password)
    if _password != password:
        _sql = 'update  user set username=%s,age=%s,password=md5(%s) where id=%s;'
        _args = (username,int(age),password,int(id))
        execute_sql(_sql, _args,fetch=False)
    else:
        _sql = 'update  user set username=%s,age=%s where id=%s;'
        _args = (username,int(age),int(id))
        execute_sql(_sql, _args,fetch=False)
'''
    #改年龄
    if _username == username and _password == password and _age != int(age):
        _sql = 'update  user set age=%s where id=%s;'
        _args = (int(age),int(id))
        execute_sql(_sql, _args,fetch=False)
        return 1
    #改密码
    elif _username == username  and _password != password and _age == int(age):
        _sql = 'update  user set password=md5(%s) where id=%s;'
        _args = (password,int(id))
        execute_sql(_sql, _args,fetch=False)
        return 2
    #改用户名
    elif  _username != username and _password == password and _age == int(age) :
        _sql = 'update  user set username=%s where id=%s;'
        _args = (username,int(id))
        execute_sql(_sql, _args,fetch=False)
        return 3
    #改用户名、年龄
    elif _username != username and _password == password and _age != int(age):
        _sql = 'update  user set username=%s,age=%s where id=%s;'
        _args = (username,int(age),int(id))
        execute_sql(_sql, _args,fetch=False)
        return 4
    #改用户名、密码
    elif _username != username and _password != password and _age == int(age):
        _sql = 'update  user set username=%s,password=md5(%s) where id=%s;'
        _args = (username,password,int(id))
        execute_sql(_sql, _args,fetch=False)
        return 5
    #改密码、年龄
    elif _username == username and _password != password and _age != int(age):
        _sql = 'update  user set password=md5(%s),age=%s where id=%s;'
        _args = (password,int(age),int(id))
        execute_sql(_sql, _args,fetch=False)
        return 6
    #改用户名、密码、年龄
    elif _username != username and _password != password and _age != int(age):
        _sql = 'update  user set username=%s,age=%s,password=md5(%s) where id=%s;'
        _args = (username,int(age),password,int(id))
        execute_sql(_sql, _args,fetch=False)
        return 7
    else:
        return 8
'''
'''删除用户信息
'''
def delete_user(id):
    _sql = 'delete  from user where id=%s;'
    _args = (id,)
    execute_sql(_sql, _args,fetch=False)


if __name__ == '__main__':
    # _is_ok, _error = validate_add_user('ada', 'ada23', 26)
    # print _is_ok, _error
    #sql = 'select * from logs limit 10;'
    print get_sql(sql)
    #print get_logs(10)
