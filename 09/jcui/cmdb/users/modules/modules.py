#encoding:utf-8

from dbutils import MySQLConnection as SQL

class User(object):

    def __init__(self,username,password,age,telphone,email):
        self.id = id
        self.username = username
        self.password = password
        self.age = age
        self.telphone = telphone
        self.email = email

    @classmethod
    def validate_login(cls,username, password):
        _columns  = ('id','username')
        _sql = 'select * from user where username = %s and password = md5(%s)'
        args = (username, password)
        sql_count, rt_list = SQL.excute_sql(_sql, args)
        return dict(zip(_columns,rt_list[0])) if sql_count != 0 else None


    @classmethod
    def get_list(cls):
        colloens = ('id', 'username', 'password', 'age', 'telphone', 'email')
        _sql = 'select * from user'
        rt = []
        sql_count, rt_list = SQL.excute_sql(_sql)  # 函数调用
        for i in rt_list:
            rt.append(dict(zip(colloens, i)))
        return rt

    @classmethod
    def get_alone_user(cls,id):
        users = cls.get_list()
        return [i for i in users if i.get('id') == id ]

    @classmethod
    def user_add(cls,params):
        username = params.get('username')
        password = params.get('password')
        age = params.get('age')
        telphone = params.get('telphone')
        email = params.get('email')
        _sql_select = 'select * from user where username = %s'
        _sql_insert = 'insert into user(username,password,age,telphone,email) values(%s,md5(%s),%s,%s,%s)'
        agrs1 = (username,)
        _sql_count, rt_list = SQL.excute_sql(_sql_select, agrs1)
        if _sql_count != 0:
            return False, username + '已存在,请尝试其他的名字'
        args2 = (username, password, age, telphone, email)
        SQL.excute_sql(_sql_insert, args2)
        return True, '添加成功'

    @classmethod
    def user_update(cls,params):
        username = params.get('username')
        id = params.get('id')
        age = params.get('age')
        telphone = params.get('telphone')
        email = params.get('email')
        _sql = 'update user set age=%s ,telphone=%s ,email=%s where id=%s and username=%s'
        args = (age, telphone, email, id, username)
        _sql_count, rt_list = SQL.excute_sql(_sql, args)
        if _sql_count != 0:
            return True, '更新成功'
        return False, '更新失败'

    @classmethod
    def user_del(cls,id, username):
        _sql = 'delete from user where id=%s and username=%s'
        args = (id, username)
        _sql_count, rt_list = SQL.excute_sql(_sql, args)
        if _sql_count != 0:
            return True
        return False

    @classmethod
    def valid_change_passwd(cls,uid, upass, muser, mpass):
        if not cls.validate_login(muser, mpass):
            return False, '管理员密码错误'
        if cls.get_alone_user(uid):  # 逻辑有问题,需要看
            return False, '用户不存在'
        if len(upass) < 6:
            return False, '密码长度小于6个字符'
        return True, '验证成功'

    @classmethod
    def change_passwd(cls,uid, upass):
        _sql = 'update user set password = md5(%s) where id = %s'
        _args = (upass, uid)
        _sql_count, rt_list = SQL.excute_sql(_sql, _args)
        if _sql_count:
            return True, '修改成功'
        return False, '修改失败'



class Assets(object):
    pass