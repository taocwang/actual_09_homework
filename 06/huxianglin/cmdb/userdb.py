import dbutil

def GetUsers():
    #return json.load(open(UserFile,'rb'),encoding='utf-8')
    _colums=('id','username','password','age')
    _sql='select * from user'
    _count,_rt_list=dbutil.execute_fetch_sql(_sql)
    _rt=[]
    for _line in _rt_list:
        _rt.append(dict(zip(_colums,_line)))
    return _rt
def GetUser(id):
    _sql='select * from user where id=%s'
    _count,_rt_list=dbutil.execute_fetch_sql(_sql,(id))
    if _count:
        return _rt_list[0]
    else:
        return False

def validate_user(username,password):
    _sql='select * from user where username=%s and password=md5(%s)'
    _count,_rt_list=dbutil.execute_fetch_sql(_sql,(username,password))
    if _count==0:
        return False
    else:
        return True

def JudgUser(username):
    _sql='select * from user where username=%s'
    _count,_rt_list=dbutil.execute_fetch_sql(_sql,(username,))
    if _count:
        return True
    return False
        
def AddUser(username,password,age):
    _sql='insert into user(username,password,age) values(%s,md5(%s),%s)'
    _args=(username,password,age)
    _count=dbutil.execute_commit_sql(_sql,_args)
    if _count:
        return True
    else:
        return False

def ChangeUser(id,username,password,age):
    _sql='select * from user where id=%s and username=%s'
    _args=(id,username)
    _count,_rt_list=dbutil.execute_fetch_sql(_sql,_args)
    if not _count:
        _sql='select * from user where username=%s'
        _args=(username,)
        _count,_rt_list=dbutil.execute_fetch_sql(_sql,_args)
        if _count:
            return 'sameusername'
    _sql='select * from user where username=%s and password=md5(%s)'
    _args=(username,password)
    _count,_rt_list=dbutil.execute_fetch_sql(_sql,_args)
    if _count:
        return 'samepassword'
    else:
        _sql='update user set username=%s,password=md5(%s),age=%s where id=%s'
        _args=(username,password,age,id)
        _count=dbutil.execute_commit_sql(_sql,_args)
        if _count:
            return True
        else:
            return False

def DelUser(id):
    _sql='delete from user where id=%s'
    _args=(id,)
    _count=dbutil.execute_commit_sql(_sql,_args)
    if _count:
        return True
    else:
        return False