#encoding: utf-8
from dbutils import execute_sql
import hashlib
import codecs

'''
sql操作函数：
说明：这个函数只有一个功能：从数据库中获取指定条件的记录
返回值：（True/False,错误提示）
1.获取危险操作的sql，比如包括delete、drop字段的sql语句

2.获取任意指定条数的log
通过在输入框输入log条数进行查询
返回值：log记录的列表

3.获取指定id的用户信息，id是唯一的
返回值: [
            {"username" : "kk", "password" : "123456", "age" : 29},
            {"username" : "woniu", "password" : "abcdef", "age" : 28}
        ]
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
        _sql = "select * from user where username=%s;"
        _args = (username,)
        _columns = ('id','username','password','age')
    else:
        _columns = ('id','username','password','age')
        _sql = 'select * from user;'
    _cnt, _rt_list = execute_sql(_sql,_args,fetch=True)
    for _line in _rt_list:
        _rt.append(dict(zip(_columns, _line)))
    return _rt,''


'''
check_user_login
验证用户名，密码是否正确
返回值: True/False
'''
def validate_login(username, password):
    _sql = 'select * from user where username=%s and password=md5(%s)'
    _cnt, _rt_list = execute_sql(_sql, (username, password),fetch=True)
    if _cnt:
        return True


'''
check_add_new_user
检查新建用户信息
返回值: (True/False, 错误信息)
'''
def validate_add_user(username, password, age):
    #处理密码，判断是否有大写、小写和数字
    _up_pass = [x for x in password if x.isupper()]
    _low_pass = [x for x in password if x.islower()]
    _isdigit_pass = [x for x in password if x.isdigit()]

    #_users,_error = get_info(username=username)                          #根据更新时的id，提取用户记录
    if username.strip() == '':
        return False, u'用户名不能为空'
    #检查用户名是否重复
    _users,_error = get_info()
    for _user in _users:
        if username == _user.get('username'):
            return False, u'用户名已存在'

    if len(password) < 6:
        return False, u'密码长度必须大于等于6'

    if len(_up_pass)==0 or len(_low_pass)==0 or len(_isdigit_pass)==0:
        return False,u'密码必须由大小写字母和数字组成！'

    if not str(age).isdigit() or int(age) <= 0 or int(age) > 150:
        return False, u'年龄必须是0到150的数字'

    return True, ''

'''
add
添加用户信息
'''
def add_user(username, password, age):
    _sql = 'insert into user(username, password, age) values(%s, md5(%s), %s)'
    _args = (username, password, age)
    execute_sql(_sql, _args,fetch=False)


'''
check_update
检查更新用户信息
返回值: True/False, 错误信息
增加同名用户判断，把ID加进去
'''
def validate_update_user(id,username, password, age):
    _up_pass = [x for x in password if x.isupper()]
    _low_pass = [x for x in password if x.islower()]
    _isdigit_pass = [x for x in password if x.isdigit()]

    # if len(password) < 6:
    #     return False, u'密码长度必须大于等于6'

    # if len(_up_pass)==0 or len(_low_pass)==0 or len(_isdigit_pass)==0:
    #     return False,u'密码必须由大小写字母和数字组成！'

    if not str(age).isdigit() or int(age) <= 0 or int(age) > 150:
        return False, u'年龄必须是0到150的数字'

    #获取post的username用户信息，和数据库中的对比，如果有不同id拥有相同username，则提示已注册！
    # _users,_error = get_info(username=username)                          #根据更新时的id，提取用户记录
    # for _user in _users:
    #     if _user['id'] != int(id):
    #         return False,u'该用户名已经注册，请重新输入用户名！'
    #     return True,''

    return True, ''


'''
update
更新用户信息
id,username, password, age为POST数据
需要根据ID获取数据库中的username、password、age，然后和post数据对比
注意：密码有变化要单独处理
'''
def update_user(id,username, password, age):
    #id唯一，直接可以根据ID获取用户在数据库中的数据
    _users,_error = get_info(_id=id)
    _username = _users[0]['username']
    _password = _users[0]['password']
    _age = _users[0]['age']

    #password = hashlib.md5(password).hexdigest()
    print "new post %s" %(password)
    print "database’s old %s" %(_password)
    #将从数据中获取的信息与post的数据进行对比，密码有变化时才修改
    if _password != password:
        _sql = 'update  user set username=%s,age=%s,password=md5(%s) where id=%s;'
        _args = (username,int(age),password,int(id))
        execute_sql(_sql, _args,fetch=False)
    #如果密码没有变化，直接修改另外2项
    else:
        _sql = 'update  user set username=%s,age=%s where id=%s;'
        _args = (username,int(age),int(id))
        execute_sql(_sql, _args,fetch=False)

'''
delete
删除用户信息
'''
def delete_user(id):
    _sql = 'delete  from user where id=%s;'
    _args = (id,)
    execute_sql(_sql, _args,fetch=False)

'''
检查用户输入原密码是否正确
'''
def validate_password(_id,_password):
    _user,_error = get_info(_id=_id)
    if hashlib.md5(_password).hexdigest() == _user[0].get('password'):
        return True
    else:
        return False

def validate_new_password(_id,_password1,_password2):
    _up_pass1 = [x for x in _password1 if x.isupper()]
    _low_pass1 = [x for x in _password1 if x.islower()]
    _isdigit_pass1 = [x for x in _password1 if x.isdigit()]

    _up_pass2 = [x for x in _password2 if x.isupper()]
    _low_pass2 = [x for x in _password2 if x.islower()]
    _isdigit_pass2 = [x for x in _password2 if x.isdigit()]

    if _password1 != _password2:
        return False,u'两次输入密码不一致，请重新输入！'
    if len(_password1) < 6:
        return False,u'密码长度必须大于6位！'
    if len(_up_pass1)==0 or len(_low_pass1)==0 or len(_isdigit_pass1)==0 or len(_up_pass2)==0 or len(_low_pass2)==0 or len(_isdigit_pass2)==0:
        return False,u'密码必须由大小写数字组成！'
    return True,''

def update_password(_id,_password):
    _sql = 'update  user set password=md5(%s) where id=%s;'
    _args = (_password,int(_id))
    execute_sql(_sql, _args,fetch=False)

def upload_file_content(path,encoding="gbk"):
    try:
        with codecs.open(path,"r",encoding) as f:
            content = f.readlines()
            return True,content
    except Exception as e:
        print e
        return False,''

if __name__ == '__main__':
    # _is_ok, _error = validate_add_user('ada', 'ada23', 26)
    # print _is_ok, _error
    #sql = 'select * from logs limit 10;'
    print get_sql(sql)
    #print get_logs(10)
