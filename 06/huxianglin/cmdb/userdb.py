import dbutil

def GetUser():
    #return json.load(open(UserFile,'rb'),encoding='utf-8')
    _colums=('id','username','password','age')
    _sql='select * from user'
    _count,_rt_list=dbutil.execute_fetch_sql(_sql)
    _rt=[]
    for _line in _rt_list:
        _rt.append(dict(zip(_colums,_line)))
    return _rt

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

def ChangeUser(username,password,age):
    _sql='select * from user where username=%s and password=md5(%s)'
    _args=(username,password)
    _count,_rt_list=dbutil.execute_fetch_sql(_sql,_args)
    if _count:
        return 'samepassword'
    else:
        _sql='update user set password=md5(%s),age=%s where username=%s'
        _args=(password,age,username)
        _count=dbutil.execute_commit_sql(_sql,_args)
        if _count:
            return True
        else:
            return False

def DelUser(username):
    _sql='delete from user where username=%s'
    _args=(username,)
    _count=dbutil.execute_commit_sql(_sql,_args)
    if _count:
        return True
    else:
        return False