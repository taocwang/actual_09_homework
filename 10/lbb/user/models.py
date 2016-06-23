#!encoding:utf-8


from dbutils import MySQLConnection
import re


class User(object):
    def __init__(self,id,username,password,age):
        self.id = id
        self.username = username
        self.password = password
        self.age = age

    @classmethod
    def validate_login(cls,username,password):
        _columns = ('id','username')
        _sql = 'select id,username from user where username=%s and password=md5(%s)'
        _count,_rt_list = MySQLConnection.execute_sql(_sql,(username,password))
        return dict(zip(_columns,_rt_list[0])) if _count != 0 else None

    @classmethod
    def get_list(cls,wheres=[]):
        _columns = ('id','username','password','age')
        _args = []
        _rt = []
        _sql = 'select * from user where 1=1'
        for _key,_value in wheres:
            _sql += ' and {key} = %s'.format(key=_key)
            _args.append(_value)
        _count,_rt_list = MySQLConnection.execute_sql(_sql,_args)
        for _line in _rt_list:
            _rt.append(dict(zip(_columns,_line)))


        return _rt

    @classmethod
    def get_by_id(cls,uid):
        _rt = cls.get_list([('id',uid)])
        return _rt[0] if len(_rt) > 0 else None

    @classmethod
    def get_by_name(cls,username):
        _rt = cls.get_list([('username',username)])
        return _rt[0] if len(_rt) > 0 else None


    @classmethod
    def validate_add(cls,username,password,age):
        if username.strip() == '':
            return False,u'用户名不能为空'
        if cls.get_by_name(username):
            return False,u'用户名已经存在'

        if len(password) < 6:
            return False,u'密码不能小于6位'

        if not str(age).isdigit() and int(age) <= 0 and int(age) > 100:
            return False,u'年龄不正确'
        return True,''


    @classmethod
    def add(cls,username,password,age):
        _sql = 'insert into user(username,password,age) values(%s,md5(%s),%s)'
        _args = (username,password,age)
        MySQLConnection.execute_sql(_sql,_args)

    @classmethod
    def validate_update(cls,uid,username,password,age):
        if cls.get_by_id(uid) is None:
            return False,u'用户信息不存在'

        if not str(age).isdigit() and int(age) <=0 and int(age) > 100:
            return False,u'年龄信息不正确'

        return True,''

    @classmethod
    def update(cls,uid,username,password,age):
        _sql = 'update user set age =%s where id=%s'
        _args = (age,uid)
        MySQLConnection.execute_sql(_sql,_args,False)

    @classmethod
    def validate_change_password(cls,uid,upassword,musername,mpassword):
        if not cls.validate_login(musername,mpassword):
            return False,u'管理员密码错误'

        if cls.get_by_id(uid) is None:
            return False,u'用户信息不存在'

        if len(upassword) < 6:
            return False,u'密码必须大于等于6'

        return True,''

    @classmethod
    def change_password(cls,uid,upassword):
        _sql = 'update user set password=md5(%s) where id=%s'
        _args = (upassword,uid)
        MySQLConnection.execute_sql(_sql,_args,False)


    def validate_add2(self):
        if self.username.strip() == '':
            return False,u'用户名不能为空'
        if self.get_by_name(self.username):
            return False,u'用户名已经存在'

        if len(self.password) < 6:
            return False,u'密码必须大于等于6'

        if not str(self.age).isdigit() and int(self.age) <= 0 or int(self.age) > 100:
            return False,u'年龄输入的不正确'

        return True,''

    def save(self):
        _sql='insert into user(username,password,age) values(%s,md5(%s),%s)'
        _args = (self.username,self.password,self.age)
        MySQLConnection.execute_sql(_sql,_args)

    @classmethod
    def delete(cls,uid):
        _sql = 'delete from user where id = %s'
        _args = (uid,)
        MySQLConnection.execute_sql(_sql,_args)




class Asset2(object):
    _columns = 'id,sn,ip,hostname,os,cpu,ram,disk,idc_id,admin,business,purchase_date,warranty,vendor,model'.split(',')
    def __init__(self,ob):
        self.id = ob.get('id')
        self.sn = ob.get('sn')
        self.ip = ob.get('ip')
        self.hostname = ob.get('hostname')
        self.os = ob.get('os')
        self.cpu = ob.get('cpu')
        self.ram = ob.get('ram')
        self.disk = ob.get('disk')
        self.idc_id = ob.get('idc_id')
        self.admin = ob.get('admin')
        self.business = ob.get('business')
        self.purchase_date = ob.get('purchase_date')
        self.warranty = ob.get('warranty')
        self.vendor = ob.get('vendor')
        self.model = ob.get('model')
        self.ob = ob

    @classmethod
    def get_idc_list(cls):
        _columns = 'id,name'
        _sql = 'select {column} from idcs where status=0'.format(column=_columns)
        _cnt,_rt_list = MySQLConnection.execute_sql(_sql)
        return [ _line for _line in _rt_list]

    @classmethod
    def get_list(cls,wheres=[]):
        _columns = ','.join(cls._columns)
        _args = []
        _sql = 'SELECT {column} FROM assets WHERE status=0'.format(column=_columns)
        for _key,_value in wheres:
            _sql += ' and {key} = %s'.format(key=_key)
            _args.append(_value)
        _cnt,_rt_list = MySQLConnection.execute_sql(_sql,_args)
        return [Asset2(dict(zip(cls._columns,_line))) for _line in _rt_list] if _cnt != 0 else []

    @classmethod
    def get_by_id(cls,aid):
        _rt = cls.get_list([('id',aid)])
        return _rt[0] if len(_rt) > 0 else None


    @classmethod
    def get_by_sn(cls,sn):
        _rt = cls.get_list([('sn',sn)])
        return _rt[0] if len(_rt) > 0 else None

    @classmethod
    def get_by_hostname(cls,hostname):
        _rt = cls.get_list([('hostname',hostname)])
        return _rt[0] if len(_rt) > 0 else None


    def validate_ip(self):
        p = re.compile("^((?:(2[0-4]\d)|(25[0-5])|([01]?\d\d?))\.){3}(?:(2[0-4]\d)|(255[0-5])|([01]?\d\d?))$")
        if len(self.ip)>6:
            if re.match(p, self.ip):
                return True
        return False

    def validate_create(self):
        _is_ok = True
        _errors = {}
        for _key in 'sn,ip,hostname,os,admin,business,vendor,model'.split(','):
            _value = self.ob.get(_key,'').strip()
            if _value == '':
                _is_ok = False
                _errors[_key] = '%s不允许为空' % _key
            elif len(_value) > 64:
                _is_ok = False
                _errors[_key] = '%s不允许为空' % _key

        if self.get_by_sn(self.ob.get('sn')):
            _is_ok = False
            _errors['sn'] = 'sn已经存在'

        if self.get_by_hostname(self.ob.get('hostname')):
            _is_ok = False
            _errors['hostname'] = 'hostname已经存在'

        if not self.validate_ip():
            _is_ok = False
            _errors['ip'] = 'ip格式不对'

        if self.ob.get('idc_id') not in [str(_value[0]) for _value in self.get_idc_list()]:
            _is_ok = False
            _errors['idc'] = '机房输入的不正确'

        _rules = {
            'cpu' : {'min':2,'max':64},
            'ram' : {'min':2,'max':512},
            'disk' : {'min':2,'max':2048},
            'warranty' : {'min':1,'max':6},

        }
        for _key in 'cpu,ram,disk,warranty'.split(','):
            _value = self.ob.get(_key,'').strip()
            print _key,_value
            if not _value.isdigit():
                _is_ok = False
                _errors[_key] = '%s不是整数' %_key
            else:
                _value = int(_value)
                _min = _rules.get(_key).get('min')
                _max = _rules.get(_key).get('max')
                if _value < _min or _value > _max:
                    _is_ok = False
                    _errors[_key] = '%s取值范围应该是%s ~ %s' %(_key,_min,_max)

        if not self.ob.get('purchase_date',''):
            _is_ok = False
            _errors['purchase_date'] = '采购日期不同为空'
        return _is_ok,_errors

    def create(self):
        _columns = self._columns[1::]
        _column_str = ','.join(_columns)
        _args = []
        for _column in _columns:
            _args.append(self.ob.get(_column,''))
        _sql = 'insert into assets({columns}) values({values})'.format(columns=_column_str,values=','.join(['%s'] * len(_columns)))
        MySQLConnection.execute_sql(_sql,_args,False)


    def validate_update(self):
        _is_ok = True
        _errors = {}
        for _key in 'sn,ip,hostname,os,admin,business,vendor,model'.split(','):
            _value = self.ob.get(_key,'').strip()
            if _value == '':
                _is_ok = False
                _errors[_key] = '%s不允许为空' % _key
            elif len(_value) > 64:
                _is_ok = False
                _errors[_key] = '%s不允许为空' % _key

        if self.get_by_sn(self.ob.get('sn')) and self.get_by_sn(self.ob.get('sn')).id != self.get_by_id(self.id).id:
            _is_ok = False
            _errors['sn'] = 'sn已经存在'

        if self.get_by_hostname(self.ob.get('hostname')) and self.get_by_hostname(self.ob.get('hostname')).id != self.get_by_id(self.id).id:
            _is_ok = False
            _errors['hostname'] = 'hostname已经存在'

        if not self.validate_ip():
            _is_ok = False
            _errors['ip'] = 'ip格式不对'

        if self.ob.get('idc_id') not in [str(_value[0]) for _value in self.get_idc_list()]:
            _is_ok = False
            _errors['idc'] = '机房输入的不正确'

        _rules = {
            'cpu' : {'min':2,'max':64},
            'ram' : {'min':2,'max':512},
            'disk' : {'min':2,'max':2048},
            'warranty' : {'min':1,'max':6},

        }
        for _key in 'cpu,ram,disk,warranty'.split(','):
            _value = self.ob.get(_key,'').strip()
            print _key,_value
            if not _value.isdigit():
                _is_ok = False
                _errors[_key] = '%s不是整数' %_key
            else:
                _value = int(_value)
                _min = _rules.get(_key).get('min')
                _max = _rules.get(_key).get('max')
                if _value < _min or _value > _max:
                    _is_ok = False
                    _errors[_key] = '%s取值范围应该是%s ~ %s' %(_key,_min,_max)

        if not self.ob.get('purchase_date',''):
            _is_ok = False
            _errors['purchase_date'] = '采购日期不同为空'
        return _is_ok,_errors


    def update(self):
        _columns = self._columns[1::]
        _values = []
        _args = []
        for _column in _columns:
            _values.append('{column}=%s'.format(column=_column))
            _args.append(self.ob.get(_column,''))
        _args.append(self.ob.get('id'))
        _sql = 'update assets SET {values} where id=%s'.format(values=','.join(_values))
        MySQLConnection.execute_sql(_sql,_args)

    @classmethod
    def delete(cls,aid):
        _sql = 'update assets set status=1 where id=%s'
        _args = (aid,)
        _count, _rt_list = MySQLConnection.execute_sql(_sql,_args)
        return _count != 0







if  __name__ == '__main__':
    print Asset2.get_list()
    print Asset2.get_by_id(5)
    print Asset2.get_by_hostname()

