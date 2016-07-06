#encoding:utf-8
import string
from random import choice
from functools import wraps
from dbutils import MySQLConnection as SQL
from flask import session,redirect

class User(object):

    def __init__(self,username,password,age,telphone,email):
        self.id = id
        self.username = username
        self.password = password
        self.age = age
        self.telphone = telphone
        self.email = email
    @classmethod
    # 定义装饰器函数,为了检查是否处于登陆状态
    def login_check(cls,func):
        @wraps(func)  # 为了解决python多装饰器出现的bug
        def check(*args, **kwargs):
            if session.get('username') is None:
                return redirect('/')
            rt = func(*args, **kwargs)
            return rt  # 返回函数的值

        return check  # 返回内层函数的结果

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

    @classmethod
    def user_reset(cls,id, username):
        _sql = 'update user set password = md5(%s) where id=%s and username=%s'
        newpassword = ''.join([choice(string.ascii_letters + string.digits) for i in range(8)])
        args = (newpassword, id, username)
        _sql_count, rt_list = SQL.excute_sql(_sql, args)
        if _sql_count != 0:
            return True, '重置成功', newpassword
        return False, '重置失败', newpassword


class Logs(object):

    pass



class Assets(object):

    def __init__(self,id,sn,ip,hostname,os,cpu,ram,disk,idc_id,admin,business,purchase_date,warranty,vendor,model,status):
        self.id = id
        self.sn = sn
        self.ip = ip
        self.hostname = hostname
        self.os = os
        self.cpu = cpu
        self.ram = ram
        self.disk = disk
        self.idc_id = idc_id
        self.admin = admin
        self.business = business
        self.purchase_date = purchase_date
        self.warranty = warranty
        self.vendor = vendor
        self.model = model
        self.status = status
    @classmethod
    def get_list(cls):
        _column = 'id,sn,ip,hostname,os,cpu,ram,disk,idc_name,admin,business,purchase_date,warranty,vendor,model,status'
        _columns = _column.split(',')
        _sql = 'select {column} from assets,idc_name where assets.status=0 and assets.idc_id = idc_name.idc_id;'.format(column=_column)
        _cnt,_rt_list = SQL.excute_sql(_sql)
        return [dict(zip(_columns,i)) for i in _rt_list]

    @classmethod
    def get_by_id(cls,aid):
        _column = 'id,sn,ip,hostname,os,cpu,ram,disk,idc_id,admin,business,purchase_date,warranty,vendor,model,status'
        # _sql = 'select {coll} from assets,idc_name where assets.status=0 and assets.idc_id = idc_name.idc_id and id = %s'.format(coll=_column)
        _sql = 'select {coll} from assets where id = %s'.format(coll=_column)
        _args = (aid,)
        _cnt, _rt_list = SQL.excute_sql(_sql, _args)
        rt = []
        if _cnt != 0:
            for x in range(len(_column.split(','))):
                rt.append((_column.split(',')[x], _rt_list[0][x]))
            return dict(rt)
        return ''

    @classmethod
    def get_idc_name(cls):
        _sql = 'select idc_id,idc_name from idc_name'
        rt = []
        _cnt, _rt_list = SQL.excute_sql(_sql)
        for i in _rt_list:
            rt.append(i)
        return rt

    @classmethod
    def delete(cls,id):
        _sql = 'update assets set status = 1 where id=%s'
        _args = (id,)
        _cnt, _rtlist = SQL.excute_sql(_sql, _args)
        if _cnt != 0:
            return True, '删除成功'
        return False, '删除失败'

    @classmethod
    def ip_check(cls,ip):
        q = ip.split('.')
        return len(q) == 4 and len(filter(lambda x: x >= 0 and x <= 255, \
                                          map(int, filter(lambda x: x.isdigit(), q)))) == 4

    @classmethod
    def validate_create(cls,params):
        collent = params.keys()
        result = {}
        for i in collent:
            if params[i] == '':
                result[i] = '%s 不能为空' % i
        # 检查SN的唯一
        sn = params.get('sn').strip()
        if len(sn) >= 6:
            _sql = 'select * from assets where sn = %s and status = 0'
            _args = (sn,)
            _cnt, rt_list = SQL.excute_sql(_sql, _args)
            if _cnt != 0:
                result['sn'] = 'SN编码已存在'
        else:
            result['sn'] = 'SN编码太短'

        # 检查IP的唯一
        ip = params.get('ip').strip()
        if cls.ip_check(ip):
            _sql = 'select * from assets where ip = %s and status = 0'
            _args = (ip,)
            _cnt, rt_list = SQL.excute_sql(_sql, _args)
            if _cnt != 0:
                result['ip'] = 'IP地址已存在'
        else:
            result['ip'] = 'IP地址不合法'

        # 检查主机名的唯一
        hostname = params.get('hostname').strip()
        _sql = 'select * from assets where hostname = %s and status = 0'
        _args = (hostname,)
        _cnt, rt_list = SQL.excute_sql(_sql, _args)
        if _cnt != 0:
            result['hostname'] = '主机名已存在'

        if not result:
            return cls.create(params)
        return False, result.values()

    @classmethod
    def create(cls,params):
        _collent = []
        _values = []
        for k, v in params.items():
            _collent.append(k)
            _values.append(v)
        _sql = 'insert into assets({coll}) values%s'.format(coll=','.join(_collent))
        _args = (tuple(_values),)
        # print tuple(_values)
        _cnt, _rtlist = SQL.excute_sql(_sql, _args)
        if _cnt != 0:
            return True, '添加成功'
        return False, '入库失败'

    @classmethod
    def validate_update(cls,params):
        collent = params.keys()
        result = {}
        for i in collent:
            if params[i] == '':
                result[i] = '%s 不能为空' % i
        if not result:
            return cls.update(params)
        return False, result.values()

    @classmethod
    def update(cls,params):
        _column = 'sn,ip,hostname,os,cpu,ram,disk,idc_id,admin,business,purchase_date,warranty,vendor,model'
        id = params.get('id')
        rt_set = []
        _args = []
        for i in _column.split(','):
            # rt_set.append(i+'='+'\'%s\'' % params[i])               #预处理的方式是不需要加''的
            rt_set.append('{collens}=%s'.format(collens=i))
            _args.append(params.get(i))
        _args.append(id)
        _sql = 'update assets set {coll} where id = %s'.format(coll=','.join(rt_set))
        # _args = (id,)
        _cnt, _rtlist = SQL.excute_sql(_sql, _args)
        if _cnt != 0:
            return True, '更新成功'
        return False, '更新失败'