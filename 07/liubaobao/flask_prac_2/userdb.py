#encoding:utf-8
import dbutils
'''
检查用户名信息,根据数据库操作影响的行数来进行判断,然后进行返回True和False
'''
def validate_login(username,password):
    sql = 'select * from user where username=%s and password=md5(%s)' #进行数据库查看固定位置是否和前端页面的相同用户名字和密码
    args = (username,password)
    count,rt_list = dbutils.execute_sql(sql,args) #数据库操作得到返回值
    if count:                                      #影响的行数来判断用户是否存在然后进行返回
        return True
    else:
        return False



'''
获得所有的用户列表显示信息
'''
def get_users():
    _coulmns = ('id','username','password','age') #进行字典的一个组合,因为字典的应用比较多.
    _rt = []
    sql = 'select * from user'
    args = ()
    count,rt_list = dbutils.execute_sql(sql,args,fetch=True)    #数据库操作进行得到返会的列表
    if count:
        for line in rt_list:
            _rt.append(dict(zip(_coulmns,line)))            #把返回列表得到变回一个列表给前端传回去
        return _rt
    else:
        return []



'''
通过用户名进行查找用户
'''
def get_username(username):
    _coulmns = ('id','username','password','age')
    sql = 'select * from user where username=%s'
    args =(username,)
    rt = []
    count,rt_list = dbutils.execute_sql(sql,args,fetch=True)
    for line in rt_list:
        rt.append(dict(zip(_coulmns,line)))
    return rt[0] if len(rt) > 0 else None


'''
通过用户id来进行查找用户
'''
def get_user(id):
    _coulmns = ('id','username','password','age')
    sql = 'select * from user where id=%s'
    args = (id,)
    count,rt_list=dbutils.execute_sql(sql,args,fetch=True)
    rt = []
    for line in rt_list:
        rt.append(dict(zip(_coulmns,line)))
    return rt[0] if len(rt) > 0 else None



'''
验证添加用户的时候会出现什么问题
'''
def validate_add(username,password,age):
    if username.strip() == '':
        return False,u'用户名不能为空'
    if len(password) < 6:
        return False,u'密码不能小于6位'
    if not str(age).isdigit() or int(age) < 0 or int(age) > 100:
        return False,u'你输入的年龄有误'
    if get_username(username):
        return False,u'你输入得用户名重复'
    return True,''



'''
添加用户信息
'''
def user_add(username,password,age):
    sql = 'insert into user(username,password,age) values(%s,md5(%s),%s)'
    args = (username,password,age)
    dbutils.execute_sql(sql,args,fetch=False)



'''
删除用户信息
'''
def user_delete(id):
    sql = 'delete from user where id=%s'
    args=(id,)
    dbutils.execute_sql(sql,args,fetch=False)


'''
验证更新用户时候是否不符合规范
'''
def validate_user_update(id,username,password,age):
    if username.strip() == '':
        return False,u'用户名不能空'
    if len(password) < 6:
        return False,u'密码不能为空'
    if not str(age).isdigit() or int(age) < 0 or int(age) > 100:
        return False,'您输入的年龄是不正确的!'
    _user = get_username(username)
    if _user.get('username') == username and _user.get('id') != int(id):
        return False,u'用户名已经存在!'
    return True,''



'''
更新用户信息
'''
def update_user(id,username,password,age):
    sql = 'update user set username=%s,password=md5(%s),age=%s where id=%s'
    args=(username,password,age,id)
    dbutils.execute_sql(sql,args,fetch=False)



'''
将日志数据插入数据库
'''
# def sort_log(log):
#     log_dic = {}
#     log_list = open(log,'rb')
#     for line in log_list.readlines():
#         ip,url,code = line.split()[0],line.split()[6],line.split()[8]
#         key = (ip,url,code)
#         log_dic[key]=log_dic.get(key,0) + 1
#     for lin in sorted(log_dic.items(),key=lambda x:-x[1])[:200]:
#         sql = 'insert into log (ip,url,code,count) values(%s,%s,%s,%s)'
#         args = (lin[0][0],lin[0][1],lin[0][2],lin[1])
#         dbutils.execute_sql(sql,args,fetch=False)


# def select_log ():
#     sql = 'select * from log'
#     args = ()
#     _count,_rt_list = dbutils.execute_sql(sql,args,fetch=True)
#     _coulmns = ('url','ip','code','count')
#     _rt=[]
#     if not _count:
#         return []
#     for lines in _rt_list:
#         _rt.append(dict(zip(_coulmns,lines)))
#     return _rt



print get_username('kk')

# print validate_user_update(13,'kk1','123456',12)