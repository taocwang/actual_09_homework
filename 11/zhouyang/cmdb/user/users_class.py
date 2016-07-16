#!/bin/env python
#coding:utf-8
from dbutils import MYSQLConnection

class Users(object):
    def __init__(self,id,username,password,age):
        self.id=id
        self.username=username
        self.password=password
        self.age=age

    @classmethod
    def validate_login(cls,username,password):
        _colum=('id','username')
        _sql="select id,username from user where username=%s and password=md5(%s);"
        _args=(username,password)
        _cnt,_rt_list=MYSQLConnection.excute_sql(_sql,_args)
        return None if _cnt == 0 else dict(zip(_colum,_rt_list[0]))

    @classmethod
    def get_list(cls,wheres={}):
        _colum='id,username,password,age'
        _args=[]
        _res=[]
        _sql="select {colume} from user where 1=1 ".format(colume=_colum)
        for _key,_value in wheres.items():
            _sql += "AND {key} = %s".format(key=_key)
            _args.append(_value)

        _cnt,_rt_list=MYSQLConnection.excute_sql(_sql,_args)
        for _line in _rt_list:
            _res.append(dict(zip(_colum.split(','),_line)))

        return  _res

    @classmethod
    def get_user_by_name(cls,username):
        _colum={'username':username}
        _rt=cls.get_list(_colum)
        return _rt[0] if len(_rt) !=0 else None

    @classmethod
    def validate_add(cls,params):
        username=params.get('username')
        password=params.get('password')
        try_password=params.get('try_password')
        age=int(params.get('age')) if params.get('age') else None
        birthday=params.get('birthday')
        if cls.get_user_by_name(username):
            return False,'用户名已存在'

        if password != try_password:
            return False,'两次输入的密码不一致，请重新输入'

        if password==None or len(password) < 6:
            return False,'密码不得小于6位'

        if (not age) or age > 120 or age <0:
            return False,'请输入有效滴年龄'

        return True,'校验通过'

    @classmethod
    def user_add(cls,params):
        username=params.get('username')
        password=params.get('password')
        try_password=params.get('try_password')
        age=int(params.get('age')) if params.get('age') else 0
        birthday=params.get('birthday')
        _sql="insert into user(`username`,`password`,`age`)VALUES(%s,md5(%s),%s);"
        _args=(username,password,age)
        _cnt=MYSQLConnection.excute_sql(_sql,_args,fetch=False)
        print _cnt
        if _cnt == 0:
            print 'sb'
            return False,'入库失败，请联系管理员'
        return True,'用户添加成功'

    @classmethod
    def validate_update(cls,params):
        username=params.get('username')
        old_passwd=params.get('password')
        new_passwd=params.get('new_password')
        try_passwd=params.get('try_password')
        age=int(params.get('age')) if params.get('age') else None
        _colum={'username':username}
        if not cls.validate_login(username,old_passwd):
            return False,'原密码错误，请重新输入！'

        if new_passwd != try_passwd:
            return False,'两次输入的密码不一致，请重新输入'

        if new_passwd==None or len(new_passwd) < 6:
            return False,'密码不得小于6位'

        if (not age) or age > 120 or age <0:
            return False,'请输入有效滴年龄'

        return True,'校验通过'

    @classmethod
    def charge_user_info(cls,params):
        username=params.get('username')
        old_passwd=params.get('password')
        new_passwd=params.get('new_password')
        try_passwd=params.get('try_password')
        age=int(params.get('age')) if params.get('age') else 0
        _sql="update user set password=md5(%s),age=%s where username=%s;"
        _args=(new_passwd,age,username)
        _cnt=MYSQLConnection.excute_sql(_sql,_args,fetch=False)
        if _cnt == 0:
            return False,'信息更新失败，请联系管理员'
        return True,'信息修改成功'

    @classmethod
    def user_del(cls,username):
        _sql="delete from user where username=%s;"
        _args=(username,)
        _cnt=MYSQLConnection.excute_sql(_sql,_args,fetch=False)
        if _cnt == 0:
            return False,'删除用户失败'
        return True,'删除用户%s成功' % username


if __name__== "__main__":
    print user.validate_login('8','123')


