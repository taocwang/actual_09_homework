#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by Nick on 2016/7/3日16点43分

from utils import Md5Str, MySQLConnection
import time
import paramiko
import traceback

# 用户管理类
class User(object):

    def __init__(self, id, username, password, age):
        self.id = id
        self.username = username
        self.password = password
        self.age = age

    '''验证用户登录
    '''
    def validate_login(self):
        _columns = ('id', 'username')
        sql = 'select * from user where username=%s and password=%s'
        _count, _rt_list = MySQLConnection.execute_sql(sql, (self.username, Md5Str.md5(self.password)), fetch=True)
        return dict(zip(_columns, _rt_list[0])) if _count != 0 else None

    '''查询用户信息
    '''
    @classmethod
    def get_list(cls):
        _columns = ('id','username','password','age')
        _sql = 'select * from user'
        _count, _rt_list = MySQLConnection.execute_sql(_sql, fetch=True)
        # return [User(**dict(zip(_columns, _list))) for _list in _rt_list]
        _rt = []
        for _list in _rt_list:
            _rt.append(dict(zip(_columns, _list)))
        return _rt

    '''添加用户信息
    '''
    # 验证用户信息
    def validate_add(self):
        if self.username.strip() == '':
            return False, u'用户名不能为空'
        # 检查用户名是否重复
        users = self.get_list()
        for user in users:
            if user.get('username') == self.username:
                return False, u'用户名已存在'
        # 密码要求长度必须大于6位
        if len(self.password) < 6:
            return False, u'密码长度不能少于6位'
        # 年龄要求0到100的整数
        if not str(self.age).isdigit() or int(self.age) <= 0 or int(self.age) > 100:
            return False, u'年龄必须是0到100的整数'
        return True, ''
    # 执行添加用户操作，返回：True/False
    def save(self):
        sql = 'insert into user(username, password, age) values(%s,%s,%s)'
        args = (self.username, Md5Str.md5(self.password), self.age)
        _count, _rt_list = MySQLConnection.execute_sql(sql, args, fetch=False)
        return _count != 0

    '''更新用户信息
    '''
    # 执行更新用户操作，返回：True/False
    def update(self):
        sql = 'update user set age=%s where id=%s'
        _count, _rt_list = MySQLConnection.execute_sql(sql, (self.age, self.id))
        return _count != 0
    # 检查用户信息
    def validate_update(self):
        # 检查用户信息是否存在
        if self.get_user_by_id() is None:
            return False, u'用户信息不存在'
        # 检查管理员密码
        if not self.validate_login():
            return False, u'管理员密码错误'
        # 年龄必须是0到100的数字
        if not str(self.age).isdigit() or int(self.age) <= 0 or int(self.age) > 100:
            return False, u'年龄必须是0到100的数字'
        return True, ''
    def get_user_by_id(self):
        _users = self.get_list()
        for _user in _users:
            if _user.get('id') == int(self.id):
                return _user
        return None

    '''更新用户密码
    '''
    def validate_user_pass(self, newpwd, new2pwd):
        # 检查用户信息是否存在
        if self.get_user_by_id() is None:
            return False, u'用户信息不存在'
        # 检查管理员密码
        elif not self.password:
            return False, u'原密码不能为空'
        elif not self.validate_login():
            return False, u'原密码验证失败'
        # 密码要求长度必须大于6位
        elif len(newpwd) < 6 and len(new2pwd) < 6:
            return False, u'密码长度不能少于6位'
        elif not newpwd == new2pwd:
            return False, u'两次密码输入不一致，请重新输入'
        return True, ''
    # 执行更新用户操作，返回：True/False
    def update_user_pass(self, newpassword):
        sql = 'update user set password=%s where id=%s'
        _count, _rt_list = MySQLConnection.execute_sql(sql, (Md5Str.md5(newpassword), self.id))
        return _count != 0

    '''删除用户信息
    '''
    def delete(self):
        sql = 'delete from user where id=%s'
        _count, _rt_list = MySQLConnection.execute_sql(sql, self.id)
        return _count != 0

# 资产管理类
class Asset(object):

    def __init__(self, *args, **kwargs):
        pass

    '''显示资产信息
    '''
    @classmethod
    def get_list(cls):
        _column = 'id,sn,ip,hostname,idc_id,purchase_date,warranty,vendor,model,admin,business,cpu,ram,disk,os,status'
        _columns = _column.split(',')
        _sql = 'select {column} from assets where status=0'.format(column=_column)
        _count, _rt_list = MySQLConnection.execute_sql(_sql, fetch=True)
        return [dict(zip(_columns, _list)) for _list in _rt_list]
    @classmethod
    def get_idcs_by_id(cls, uid):
        sql = 'select * from idcs where id=%s and status=0'
        _count, _rt_list = MySQLConnection.execute_sql(sql, args=(uid,), fetch=True)
        return _rt_list

    '''创建资产信息
    '''
    # 通过ID标识符，查询IDC机房信息；创建的dialog页面选择机房的时候使用
    @classmethod
    def get_idc_list(cls):
        _sql = 'select id,name from idcs where status=0'
        _count, _rt_list = MySQLConnection.execute_sql(_sql, fetch=True)
        return _rt_list
    # 创建资产时验证
    @classmethod
    def validate_create(cls, asset_dict):
        if asset_dict.get('_sn').strip().count(' ') != 0:
            return False, u'资产编号不能有空格'
        elif asset_dict.get('_sn') == '':
            return False, u'请填写资产编号'
        assets = cls.get_list()
        for asset in assets:
            if asset.get('sn') == asset_dict.get('_sn'):
                return False, u'资产编号已存在'
        if asset_dict.get('_purchase_date') == '':
            return False, u'请选择采购日期'
        if asset_dict.get('_warranty').strip() == '':
            return False, u'请填写保修时间'
        elif not asset_dict.get('_warranty').strip().isdigit():
            return False, u'保修时长必须为整数'
        return True, ''
    # 将验证后的资产信息写入数据库
    @classmethod
    def create(cls, asset_dict):
        sql = 'insert into assets(sn,ip,hostname,idc_id,purchase_date,warranty,vendor,model,admin,business,cpu,ram,disk,os) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'
        args_list = []
        lists = ['sn','ip','hostname','idc_id','purchase_date','warranty','vendor','model','admin','business','cpu','ram','disk','os']
        for i in lists:
            args_list.append(asset_dict.get('_'+i))
        _count, _rt_list = MySQLConnection.execute_sql(sql, args_list, fetch=False)
        return _count != 0

    '''更新资产信息
    '''
    # 更新资产时验证
    @classmethod
    def validate_update(cls, asset_dict):
        if asset_dict.get('_purchase_date') == '':
            return False, u'请选择采购日期'

        if asset_dict.get('_warranty').strip() == '':
            return False, u'请填写保修时间'
        elif not asset_dict.get('_warranty').strip().isdigit():
            return False, u'保修时长必须为整数'
        return True, ''
    # 将验证后的资产信息写入数据库
    @classmethod
    def update(cls, asset_dict, _id):
        sql = 'update assets set sn=%s,ip=%s,hostname=%s,idc_id=%s,purchase_date=%s,warranty=%s,vendor=%s,model=%s,admin=%s,business=%s,cpu=%s,ram=%s,disk=%s,os=%s where id=%s'
        args_list = []
        lists = ['sn','ip','hostname','idc_id','purchase_date','warranty','vendor','model','admin','business','cpu','ram','disk','os']
        for i in lists:
            args_list.append(asset_dict.get('_'+i))
        args_list.append(_id)
        _count, _rt_list = MySQLConnection.execute_sql(sql, args_list, fetch=False)
        return _count != 0

    '''删除资产信息
    '''
    @classmethod
    def delete(cls, uid):
        sql = 'update assets set status=1 where id=%s'
        _count, _rt_list = MySQLConnection.execute_sql(sql, uid)
        return _count != 0

# 日志统计类
class Log2db(object):

    # 读取日志信息
    def log_fetch(self, topn):
        _rt = []
        _columns = ('id', 'ip', 'url', 'status', 'count')
        sql = 'select * from accesslog order by count desc limit %s'
        _count, _rt_list = MySQLConnection.execute_sql(sql, args=(topn,), fetch=True)
        for _list in _rt_list:
            _rt.append(dict(zip(_columns, _list)))
        return _rt

    # 写入日志信息
    def log_execute(self, log_files):
        sql = 'DELETE FROM accesslog;'
        MySQLConnection.execute_sql(sql, fetch=False)
        sql = 'insert into accesslog(ip,url,status,count) values(%s, %s, %s, %s)'
        rt_dict = {}
        try:
            log_files = open(log_files, 'r')
            while True:
                line = log_files.readline()
                if not line:
                    break
                logs = line.split()
                (ip, url, status) = logs[0], logs[6], logs[8]
                if (ip, url, status) not in rt_dict:
                    rt_dict[(ip, url, status)] = 1
                else:
                    rt_dict[(ip, url, status)] += 1
            log_files.close()
            # args_list = sorted(rt_dict.items(), key=lambda x:x[1], reverse=True)
            _count = MySQLConnection.bulker_commit_sql(sql, args=rt_dict.items())
            return _count != 0
        except BaseException as e:
            print traceback.format_exc()
            print e
            return False

# 服务管理类
class Service(object):

    '''获取域名管理信息
    返回值: True/False
    '''
    @classmethod
    def get_list(cls):
        _columns = ('id', 'domain_name', 'username', 'password', 'function')
        _sql = 'select * from service_manage'
        _count, _rt_list = MySQLConnection.execute_sql(_sql, fetch=True)
        _rt = []
        for _list in _rt_list:
            _rt.append(dict(zip(_columns, _list)))
        return _rt

    '''删除数据
    返回值: True/False
    '''
    @classmethod
    def del_service(cls, uid):
        sql = 'delete from service_manage where id=%s'
        _count, _rt_list = MySQLConnection.execute_sql(sql, uid, fetch=False)
        return _count != 0

    '''更新数据
    返回值: True/False
    '''
    @classmethod
    def update_service(cls, _url, _username, _password, _func, _id):
        sql = 'update service_manage set domain_name=%s, username=%s, password=%s, function=%s where id=%s'
        args = (_url, _username, _password, _func, _id)
        _count, _rt_list = MySQLConnection.execute_sql(sql, args, fetch=False)
        return _count != 0

    '''添加数据
    返回值: True/False
    '''
    @classmethod
    def add_service(cls, _url, _username, _password, _func):
        sql = 'insert into service_manage(domain_name,username,password,function) values(%s,%s,%s,%s)'
        args = (_url, _username, _password, _func)
        _count, _rt_list = MySQLConnection.execute_sql(sql, args, fetch=False)
        return _count != 0


# 主机监控类
class Performs(object):

    @classmethod
    def add(cls, req):
        _ip = req.get('ip')
        _cpu = req.get('cpu')
        _ram = req.get('ram')
        _time = req.get('time')
        _sql = 'insert into performs(ip, cpu, ram, time) values(%s,%s,%s,%s)'
        MySQLConnection.execute_sql(_sql, (_ip, _cpu, _ram, _time), fetch=False)

    @classmethod
    def get_list(cls, ip):
        _sql = 'select cpu,ram,time from performs where ip=%s and time>=%s order by time asc'
        _args = (ip, time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time() - 60 * 60)))
        _count, _rt_list = MySQLConnection.execute_sql(_sql, _args, fetch=True)
        datetime_list = []
        cpu_list = []
        ram_list = []
        for _cpu, _ram, _time in _rt_list:
            cpu_list.append(_cpu)
            ram_list.append(_ram)
            datetime_list.append(_time.strftime('%H:%M:%S'))
        return datetime_list, cpu_list, ram_list


# 远程执行命令类
class Ssh(object):
    def __init__(self, host, cmds):
        self.__host = host
        self.__cmds = cmds
        self.__port = 22
        self.__username = 'root'
        self.__password = '123456'

    def ssh_execute(self):
        _rt_list = []
        ssh = paramiko.SSHClient()
        try:
            ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            ssh.connect(self.__host, self.__port, self.__username, self.__password)
            for _cmd in self.__cmds:
                stdin, stdout, stderr = ssh.exec_command(_cmd)
                _rt_list.append([_cmd, stdout.readlines(), stderr.readlines()])
        except BaseException as e:
            print traceback.format_exc()
            print e
        finally:
            ssh.close()
        return _rt_list

if __name__ == '__main__':
    _host = '192.168.2.209'
    _cmds = ['ip a']
    ssh = Ssh(_host, _cmds)
    _rt_list = ssh.ssh_execute()
    print _rt_list
    # for _cmd, _out, _err in _rt_list:
    #     print _cmd, _out, _err
