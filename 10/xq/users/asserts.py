# -*- coding: utf-8 -*-
# @Author: liuli
# @Date:   2016-06-26 13:56:39
# @Last Modified by:   liuli
# @Last Modified time: 2016-07-03 17:40:21

from dbutils import MySQLConnection
import time

'''
返回所有资产信息
[{'sn':11111},{'id':22}......]
'''
def get_list():
    _column = 'id,sn,ip,hostname,idc_id,purchase_date,warranty,vendor,model,admin,business,cpu,ram,disk,os,status'
    _columns = _column.split(',')
    #print _columns
    _sql = 'select {column} from assets where status=0' .format(column=_column)
    _cnt, _rt_list = execute_sql(_sql,fetch=True)
    #print _rt_list
    return [dict(zip(_columns,_line)) for _line in _rt_list]


'''
通过逐渐返回资产信息
None/{}
'''
def get_by_id(_id):
    _column = 'id,sn,ip,hostname,os,cpu,ram,disk,idc_id,admin,business,purchase_date,warranty,vendor,model,status'
    _columns = _column.split(',')
    _sql = 'select * from assets where id=%s;'
    _args = (_id,)
    _cnt, _rt_list = execute_sql(_sql,_args,fetch=True)
    if _cnt:
        for _line in _rt_list:
            _rt = dict(zip(_columns, _line))
        return _rt,''
    return False,u'数据不存在！'

'''
在创建资产时，对输入信息进行检查
True/False,error
'''
def validate_create(_sn,_ip,_hostname,_os,_cpu,_ram,_disk,_idc_id,_admin,_business,_purchase_date,_warranty,_vendor,_model):
    print _cpu
    _rt = get_list()
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

'''
在创建资产,操作数据库
返回True/False

'''

def create(_sn,_ip,_hostname,_os,_cpu,_ram,_disk,_idc_id,_admin,_business,_purchase_date,_warranty,_vendor,_model):
    _column = 'sn,ip,hostname,os,cpu,ram,disk,idc_id,admin,business,purchase_date,warranty,vendor,model'

    _rt,_error = validate_create(_sn,_ip,_hostname,_os,_cpu,_ram,_disk,_idc_id,_admin,_business,_purchase_date,_warranty,_vendor,_model)
    if _rt:
        _sql = 'insert into assets({column}) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);'.format(column=_column)
        _args = (_sn,_ip,_hostname,_os,_cpu,_ram,_disk,_idc_id,_admin,_business,_purchase_date,_warranty,_vendor,_model)
        #print _sql
        #print _args
        execute_sql(_sql, _args,fetch=False)

'''
在修改资产时对输入信息进行检查
True/False，error信息

'''
def validate_update(_sn,_ip,_hostname,_os,_cpu,_ram,_disk,_idc_id,_admin,_business,_purchase_date,_warranty,_vendor,_model):
    _rt = get_list()
    #判断重复问题
    #判断格式问题
    #判断为空
    return True,''


'''
更新资产，操作数据库
返回True/False

'''
def update(_sn,_ip,_hostname,_os,_cpu,_ram,_disk,_idc_id,_admin,_business,_purchase_date,_warranty,_vendor,_model,_id):
    _sql = 'update assets set sn=%s,ip=%s,hostname=%s,os=%s,cpu=%s,ram=%s,disk=%s,idc_id=%s,admin=%s,business=%s,purchase_date=%s,warranty=%s,vendor=%s,model=%s where id=%s;'
    _args = (_sn,_ip,_hostname,_os,_cpu,_ram,_disk,_idc_id,_admin,_business,_purchase_date,_warranty,_vendor,_model,int(_id))
    execute_sql(_sql, _args,fetch=False)


'''
删除资产，操作数据库
返回True/False

'''
def delete(id):
    _sql = 'update  assets set status=1 where id=%s;'
    _args = (id,)
    execute_sql(_sql, _args,fetch=False)

'''
获取IDC资产，操作数据库
返回True/False

'''
def get_idcs():
    _sql = 'select id,name from idcs where status=0;'
    _cnt,_idcs = execute_sql(_sql,fetch=True)
    if _cnt:
        return list(_idcs)
    return []

'''
在创建IDC资产,操作数据库
返回True/False

'''

def idc_create(name):
    _column = 'name'
    name=str(name)
    _sql = 'insert into idcs(name) values(%s);'
    _args = (name)
    #print _sql
    #print _args
    execute_sql(_sql, _args,fetch=False)

#_idcs = [('1', '北京鲁谷'), ('2', '北京森华'), ('3', '北京亦庄'), ('4', '北京大兴')]
if __name__ == '__main__':
    #create('115','192.168.1.100','bjlg-bgp.xsjcs.com',time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()),'hp','380g5','admin','jx1',10,128,50,'linux',_idc_id=1,_warranty=3)
    # _rt,_error = get_by_id(19)
    # print _rt
    # print get_idcs()
    print get_idcs()

