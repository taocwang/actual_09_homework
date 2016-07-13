# -*- coding: utf-8 -*-
# @Author: liuli
# @Date:   2016-07-03 16:42:59
# @Last Modified by:   liuli
# @Last Modified time: 2016-07-04 21:20:47

from  dbutils import MySQLConnection
import hashlib
import codecs
import os


class User(object):
    def __init__(self,id,username,password,age):
        self.id = id
        self.username = username
        self.password = password
        self.age = age

    #类方法，实例可是调用
    #类方法，一般不需要实例化的函数才使用
    @classmethod
    def validate_login(cls,username,password):
        _columns = ('id','username','password')
        _sql = 'select * from user where username=%s and password=md5(%s)'
        _cnt, _rt_list = MySQLConnection.execute_sql(_sql, (username, password),fetch=True)
        return dict(zip(_columns,_rt_list[0])) if _cnt!=0 else None

    @classmethod
    def get_info(cls,_sql=None,_count=None,_user=None,_id=None,username=None,_args=()):
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
        _cnt, _rt_list = MySQLConnection.execute_sql(_sql,_args,fetch=True)
        for _line in _rt_list:
            _rt.append(dict(zip(_columns, _line)))
        return _rt,''


    @classmethod
    def validate_add_user(cls,s_username,username, password, age):
        #处理密码，判断是否有大写、小写和数字
        _up_pass = [x for x in password if x.isupper()]
        _low_pass = [x for x in password if x.islower()]
        _isdigit_pass = [x for x in password if x.isdigit()]

        if s_username!='admin':
            return False,u'权限不够，只有管理员才能添加用户！'
        #_users,_error = get_info(username=username)                          #根据更新时的id，提取用户记录
        if username.strip() == '':
            return False, u'用户名不能为空'
        #检查用户名是否重复
        _users,_error = cls.get_info()
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

    @classmethod
    def add_user(cls,username, password, age):
        _sql = 'insert into user(username, password, age) values(%s, md5(%s), %s)'
        _args = (username, password, age)
        MySQLConnection.execute_sql(_sql, _args,fetch=False)


    @classmethod
    def validate_update_user(cls,id,s_id,username,s_username,password, age):
        _up_pass = [x for x in password if x.isupper()]
        _low_pass = [x for x in password if x.islower()]
        _isdigit_pass = [x for x in password if x.isdigit()]
        if s_username!='admin':
            if int(id) != s_id:
                return False,u'权限不够，只能修改自己的信息！'
        if not str(age).isdigit() or int(age) <= 0 or int(age) > 150:
            return False, u'年龄必须是0到150的数字'

        return True, ''


    @classmethod
    def update_user(cls,id,username, password, age):
        #id唯一，直接可以根据ID获取用户在数据库中的数据
        _users,_error = cls.get_info(_id=id)
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
            MySQLConnection.execute_sql(_sql, _args,fetch=False)
        #如果密码没有变化，直接修改另外2项
        else:
            _sql = 'update  user set username=%s,age=%s where id=%s;'
            _args = (username,int(age),int(id))
            MySQLConnection.execute_sql(_sql, _args,fetch=False)

    @classmethod
    def delete_user(cls,id):
        _sql = 'delete  from user where id=%s;'
        _args = (id,)
        MySQLConnection.execute_sql(_sql, _args,fetch=False)

    @classmethod
    def check_is_admin(cls,username):
        if username == 'admin':
            return True
        return False
    @classmethod
    def upload_validate_check(cls,path):
        pic_list = ['bmp','jpg','png','tiff','gif','pcx','tga','exif','fpx','svg','psd','cdr','pcd','dxf','ufo','eps','ai','raw']
        pic=pic_list[:]
        for p in pic:
            pic_list.append(p)
        if os.path.basename(path).split('.')[-1] in pic_list:
            return True,path
        return False,u'上传格式不对！'

    @classmethod
    def validate_charge_user_password(cls,uid, upassword, musername, mpassword):
        #检查管理员密码是否正确
        if not cls.validate_login(musername, mpassword):
            return False, '管理员密码错误'

        # if get_user(uid) is None:
        #     return False, u'用户信息不存在'

        #密码要求长度必须大于等于6
        if len(upassword) < 6:
            return False, u'密码必须大于等于6'

        #只有管理员才能修改其他用户密码
        if not cls.check_is_admin(musername):
            return False,u'您不是管理员，没有修改其他用户权限！'
        return True, ''


    @classmethod
    def charge_user_password(cls,uid, upassword):
        _sql = 'update user set password=md5(%s) where id=%s'
        _args = (upassword, uid)
        MySQLConnection.execute_sql(_sql, _args,fetch=False)

    @classmethod
    def validate_new_password(cls,_id,_password1,_password2):
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

    @classmethod
    def validate_password(cls,_id,_password):
        _user,_error = cls.get_info(_id=_id)
        if hashlib.md5(_password).hexdigest() == _user[0].get('password'):
            return True
        else:
            return False

    @classmethod
    def update_password(cls,_id,_password):
        _sql = 'update  user set password=md5(%s) where id=%s;'
        _args = (_password,int(_id))
        MySQLConnection.execute_sql(_sql, _args,fetch=False)


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
    def get_by_id(cls,_id):
        _column = 'id,sn,ip,hostname,os,cpu,ram,disk,idc_id,admin,business,purchase_date,warranty,vendor,model,status'
        _columns = _column.split(',')
        _sql = 'select * from assets where id=%s;'
        _args = (_id,)
        _cnt, _rt_list =MySQLConnection.execute_sql(_sql,_args,fetch=True)
        if _cnt:
            for _line in _rt_list:
                _rt = dict(zip(_columns, _line))
            return _rt,''
        return False,u'数据不存在！'

    @classmethod
    def get_list(cls):
        _column = 'id,sn,ip,hostname,idc_id,purchase_date,warranty,vendor,model,admin,business,cpu,ram,disk,os,status'
        _columns = _column.split(',')
        #print _columns
        _sql = 'select {column} from assets where status=0' .format(column=_column)
        _cnt, _rt_list = MySQLConnection.execute_sql(_sql,fetch=True)
        #print _rt_list
        return [dict(zip(_columns,_line)) for _line in _rt_list]

    @classmethod
    def validate_create(cls,_sn,_ip,_hostname,_os,_cpu,_ram,_disk,_idc_id,_admin,_business,_purchase_date,_warranty,_vendor,_model):
        _rt = cls.get_list()
        _col_dic = {'资产编号':_sn,'IP地址':_ip,'购买日期':_purchase_date,'设备厂商':_vendor,'设备型号':_model,'CPU个数':_cpu,'内存':_ram,'硬盘':_disk}
        #判断某些列不能为空
        for k in _col_dic.keys():
            if _col_dic[k] == '':
                return False,u'%s不能为空，请重新填写！' %k
        #判断某些列重复
        for _rrt in _rt:
            if _rrt['ip'] == _ip and _rrt['status']==0:
                return False,u'新增资产中的IP正在使用中，请重新分配！'
            if _rrt['sn'] == _sn:
                return False,u'sn号重复，请重新填写！'
        #判断某些列格式问题
        return True,''

    @classmethod
    def create(cls,_sn,_ip,_hostname,_os,_cpu,_ram,_disk,_idc_id,_admin,_business,_purchase_date,_warranty,_vendor,_model):
        _column = 'sn,ip,hostname,os,cpu,ram,disk,idc_id,admin,business,purchase_date,warranty,vendor,model'

        _rt,_error = cls.validate_create(_sn,_ip,_hostname,_os,_cpu,_ram,_disk,_idc_id,_admin,_business,_purchase_date,_warranty,_vendor,_model)
        if _rt:
            _sql = 'insert into assets({column}) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);'.format(column=_column)
            _args = (_sn,_ip,_hostname,_os,_cpu,_ram,_disk,_idc_id,_admin,_business,_purchase_date,_warranty,_vendor,_model)
            #print _sql
            #print _args
            MySQLConnection.execute_sql(_sql, _args,fetch=False)

    @classmethod
    def validate_update(cls,_sn,_ip,_hostname,_os,_cpu,_ram,_disk,_idc_id,_admin,_business,_purchase_date,_warranty,_vendor,_model):
        _rt = cls.get_list()
        #判断重复问题
        #判断格式问题
        #判断为空
        return True,''

    @classmethod
    def update(cls,_sn,_ip,_hostname,_os,_cpu,_ram,_disk,_idc_id,_admin,_business,_purchase_date,_warranty,_vendor,_model,_id):
        _sql = 'update assets set sn=%s,ip=%s,hostname=%s,os=%s,cpu=%s,ram=%s,disk=%s,idc_id=%s,admin=%s,business=%s,purchase_date=%s,warranty=%s,vendor=%s,model=%s where id=%s;'
        _args = (_sn,_ip,_hostname,_os,_cpu,_ram,_disk,_idc_id,_admin,_business,_purchase_date,_warranty,_vendor,_model,int(_id))
        MySQLConnection.execute_sql(_sql, _args,fetch=False)

    @classmethod
    def delete(cls,id):
        _sql = 'update  assets set status=1 where id=%s;'
        _args = (id,)
        MySQLConnection.execute_sql(_sql, _args,fetch=False)

    @classmethod
    def get_idcs(cls):
        _sql = 'select id,name from idcs where status=0;'
        _cnt,_idcs = MySQLConnection.execute_sql(_sql,fetch=True)
        if _cnt:
            return list(_idcs)
        return []


    @classmethod
    def idc_create(cls,name):
        _column = 'name'
        name=str(name)
        _sql = 'insert into idcs(name) values(%s);'
        _args = (name)
        #print _sql
        #print _args
        MySQLConnection.execute_sql(_sql, _args,fetch=False)

if __name__ == '__main__':
    print User.validate_login('admin','xuequn')
    print User.validate_login('admin','xuequn1')

