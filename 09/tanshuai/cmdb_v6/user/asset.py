#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by Nick on 2016/6/26日13点56分
import dbutils


'''返回所有资产信息
返回值：[{'sn': '', 'id': '',...},{},{}]
'''
def get_list():
    _column = 'id,sn,ip,hostname,idc_id,purchase_date,warranty,vendor,model,admin,business,cpu,ram,disk,os,status'
    _columns = _column.split(',')
    _sql = 'select {column} from assets where status=0'.format(column=_column)
    _count, _rt_list = dbutils.execute_sql(_sql, fetch=True)
    return [dict(zip(_columns, _list)) for _list in _rt_list]
    # _rt = []
    # for _list in _rt_list:
    #     _rt.append(dict(zip(_columns, _list)))
    # return _rt

'''创建资产，操作数据库
返回值：True/False
'''
def create(asset_dict):
    sql = 'insert into assets(sn,ip,hostname,idc_id,purchase_date,warranty,vendor,model,admin,business,cpu,ram,disk,os) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'
    args_list = []
    lists = ['sn','ip','hostname','idc_id','purchase_date','warranty','vendor','model','admin','business','cpu','ram','disk','os']
    for i in lists:
        args_list.append(asset_dict.get('_'+i))
    _count, _rt_list = dbutils.execute_sql(sql, args_list)
    return _count != 0

'''更新资产，操作数据库
返回值：True/False
'''
def update(asset_dict, _id):
    sql = 'update assets set sn=%s,ip=%s,hostname=%s,idc_id=%s,purchase_date=%s,warranty=%s,vendor=%s,model=%s,admin=%s,business=%s,cpu=%s,ram=%s,disk=%s,os=%s where id=%s'
    args_list = []
    lists = ['sn','ip','hostname','idc_id','purchase_date','warranty','vendor','model','admin','business','cpu','ram','disk','os']
    for i in lists:
        args_list.append(asset_dict.get('_'+i))
    args_list.append(_id)
    _count, _rt_list = dbutils.execute_sql(sql, args_list)
    return _count != 0

'''删除资产，操作数据库
返回值：True/False
'''
def delete(uid):
    sql = 'update assets set status=1 where id=%s'
    _count, _rt_list = dbutils.execute_sql(sql, uid)
    return _count != 0

'''通过ID标识符，查询IDC机房信息
返回值：True/False，IDC机房信息
'''
def get_by_id(uid):
    sql = 'select * from idcs where id=%s and status=0'
    _count, _rt_list = dbutils.execute_sql(sql, uid, fetch=True)
    return _rt_list

'''返回所有IDC机房信息
返回值：
'''
def get_idc():
    _sql = 'select id,name from idcs where status=0'
    _count, _rt_list = dbutils.execute_sql(_sql, fetch=True)
    return _rt_list


'''在创建资产时对输入信息进行检查
返回值：True/False, error_msg{}
'''
def validate_create(asset_dict):
    assets = get_list()
    if asset_dict.get('_sn').strip().count(' ') != 0:
        return False, u'资产编号不能有空格'
    elif asset_dict.get('_sn') == '':
        return False, u'请填写资产编号'
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

'''在修改资产时对输入信息进行验证
返回值：True/False, error_msg{}
'''
def validate_update(asset_dict):
    if asset_dict.get('_purchase_date') == '':
        return False, u'请选择采购日期'

    if asset_dict.get('_warranty').strip() == '':
        return False, u'请填写保修时间'
    elif not asset_dict.get('_warranty').strip().isdigit():
        return False, u'保修时长必须为整数'
    return True, ''

if __name__ == '__main__':
    print get_list()
    print get_by_id(3)
    print get_idc()