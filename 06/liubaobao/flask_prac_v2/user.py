#encoding:utf-8
import useruntils

'''
获取用户信息列表用过数据库
'''
def get_users():
    _coulmns = ('id','username','password','age')
    sql = 'select * from user'
    args=()
    _rt=[]
    count,rt_list = useruntils.execute_sql(sql,args,fetch=True)
    if not count:
        return []
    for lines in rt_list:
        _rt.append(dict(zip(_coulmns,lines)))
    return _rt





'''
保存用户信息废弃代码用于文件存储
'''
'''
def save_users(users):
        fhandler = open(gconf.USER_FILE,'wb')
        fhandler.write(json.dumps(users))
        fhandler.close()
'''







'''
进行用户登陆验证
True/False:用户名和密码验证成功/用户名和密码错误
如果有一个用户的username&password 与输入相同则登陆成功
如果所有用户的username&password 与输入不相同则登陆失败
'''
def validate_login(username,password):
    #sql = 'select * from user where name="{username}" and password = "{password}"'.format(username=username,password=password)
    sql = 'select * from user where name=%s and password = md5(%s)'
    args=(username,password)
    count,rt_list = useruntils.execute_sql(sql,args,fetch=True)
    #return count != 0
    if count:
        return True
    else:
        return False





'''
验证添加用户信息
True/False,描述信息是否符合要求
'''
def validate_add_user(username,password,age):
    users = get_users()
    for user in users:
        if user.get('username') == username:
            return False, '用户名已经存在'

    if len(password) < 6:
        return False,'密码长度小于6位'

    if not str(age).isdigit() or int(age) < 0 or int(age) >100:
        return False,'年龄不正确'

    return True,''





'''
添加用户信息通过数据库
'''

def add_user(username,password,age):
        sql = 'insert into user(name,password,age) values(%s,md5(%s),%s)'
        args=(username,password,age)
        useruntils.execute_sql(sql,args,fetch=False)





'''
删除用户信息通过数据库
'''

def delete_user(id):
    sql = "delete from user where id=%s"
    args = id
    useruntils.execute_sql(sql,args,fetch=False)





'''
查询 用 （用户id） 获取用户信息通过数据库
'''
def get_user(id):
    coulmns = ('id','username','password','age')
    sql = 'select * from user where id=%s'
    args = (id)
    count,rt_list = useruntils.execute_sql(sql,args,fetch=True)
    if not rt_list:
        return None
    else:
        _rt_list = rt_list[0]
    rt = dict(zip(coulmns,_rt_list))
    if count:
        return rt
    else:
        return None






'''
查询用（年龄）获取用户信息通过数据库
'''
def get_age(age):
    _coulmns = ('id','username','password','age')
    sql = 'select * from user where age=%s'
    args= (age)
    _rt=[]
    count,rt_list = useruntils.execute_sql(sql,args,fetch=True)
    if not count:
        return []
    for lines in rt_list:
        _rt.append(dict(zip(_coulmns,lines)))
    return _rt



'''
用 用户名 获取用户信息通过数据库
'''
def get_username(username):
    coulmns = ('id','username','password','age')
    sql = 'select * from user where name="{username}"'.format(username=username)
    args = ()
    count,rt_list = useruntils.execute_sql(sql,args,fetch=True)
    if not rt_list:
        return None
    else:
        _rt_list = rt_list[0]
    rt = dict(zip(coulmns,_rt_list))
    if count:
        return rt
    else:
        return None




'''
id验证户更新引用上面的函数get_user(id)进行验证
'''
def validate_update_user(username,password,age,id):
    if get_user(id) is None:
        return False,'用户信息不存在'
    if len(password) < 6:
        return False,'密码长度小于6位'

    if not str(age).isdigit() or int(age) < 0 or int(age) >100:
        return False,'年龄不正确'
    user_list = get_users()
    for user in user_list:
        if user.get('username') == username:
            return False,'1'

    return True,''




'''
更新用户信息用过数据库
'''
def update_user(username,password,age,id):
    sql = 'update user SET name=%s,password=md5(%s),age=%s where id=%s'
    args=(username,password,age,id)
    useruntils.execute_sql(sql,args,fetch=False)




'''
搜索查询用户信息通过数据库年龄
'''
def query_user_age(age):
    ages = get_age(str(age))
    if not ages:
        return False,()
    else:
        return True,ages



'''
搜索查询用户信息通过数据库name名字
'''
def query_user_name(username):
    username = get_username(username)
    if not username:
        return False,()
    else:
        return True,username




'''
进行正序和反序的一个排序通过前端get的请求方式
'''
def sort_user(order):
    sql = 'select * from user order by id {order}'.format(order=order)
    #sql = 'select * from user order by id %s'
    coulmns = ('id','username','password','age')
    args = ()
    _rt=[]
    count,rt_list = useruntils.execute_sql(sql,args,fetch=True)
    if not count:
        return []
    for lines in rt_list:
        _rt.append(dict(zip(coulmns,lines)))
    return _rt




'''
将日志的数据插入数据库(数据库的表结构已经建立好了)并且进行排序1000插入数据库。
'''
def sort_log(log):
    log_dic = {}
    log_list = open(log,'rb')
    for line in log_list.readlines():
        ip,url,code = line.split()[0],line.split()[6],line.split()[8]
        key = (ip,url,code)
        log_dic[key]=log_dic.get(key,0) + 1
    for lin in sorted(log_dic.items(),key=lambda x:-x[1])[:1000]:
        sql = 'insert into log (ip,url,code,count) values(%s,%s,%s,%s)'
        args = (lin[0][0],lin[0][1],lin[0][2],lin[1])
        useruntils.execute_sql(sql,args,fetch=False)



'''
查询日志数据为前端进行展示
'''
def select_log (id_c):
    sql = 'select * from log where id <= %s'
    args = (id_c)
    _count,_rt_list = useruntils.execute_sql(sql,args,fetch=True)
    print _rt_list
    _coulmns = ('id','ip','url','code','count')
    _rt=[]
    if not _count:
        return []
    for lines in _rt_list:
        _rt.append(dict(zip(_coulmns,lines)))
    return _rt





if __name__ == '__main__':
    print query_user_name('kk')
