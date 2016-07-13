#!/usr/bin/env python
# -*- coding: utf-8 -*-
import dbutil

def get_list():
    _column='id,sn,ip,hostname,os,cpu,ram,disk,idc_id,admin,business,purchase_date,warranty,vendor,model'
    _columns=_column.split(',')
    _sql='select {column} from assets where status=0'.format(column=_column)
    _cnt,_rt_list=dbutil.execute_fetch_sql(_sql)
    return [dict(zip(_columns,_line)) for _line in _rt_list]
    return []

def get_by_id():
    return None

def validate_create(params):
    _errors,_form_keys={},{'sn':u'sn编号','ip':u'IP地址','hostname':u'主机名','os':u'操作系统','cpu':u'cpu',
                           'ram':u'内存','disk':u'硬盘','idc_id':u'机房','admin':u'使用人', 'business':u'业务',
                           'purchase_date':u'采购日期','warranty':u'保修时间','vendor':u'供应商','model':u'型号'}
    for i in params:
        if params[i][0].strip()=="":
            _errors[i]=u'请填写%s！' %(_form_keys[i])
    try:
        int(params['warranty'][0].strip())
    except Exception as e:
        _errors['warranty_num']=u'保修时间必须为数字！'
    if _errors:
        return False,_errors
    _sql='select sn from assets where sn=%s'
    _cnt=dbutil.execute_commit_sql(_sql,(params['sn'][0]).strip())
    if _cnt:
        return False,{'sn':'sn编号重复！'}
    return True,{}

def create(params):
    _keys=params.keys()
    _values=[params[i][0].strip() for i in _keys]
    _keys.append('status'),_values.append(0)
    _sql='insert into assets({_keys}) values({_values})'.format(_keys=','.join(_keys),_values=','.join(['%s']*len(_keys)))
    _cnt=dbutil.execute_commit_sql(_sql,(_values))
    if _cnt:
        return True
    else:
        return False

def validate_update(params):
    _errors,_form_keys={},{'sn':u'sn编号','ip':u'IP地址','hostname':u'主机名','os':u'操作系统','cpu':u'cpu',
                           'ram':u'内存','disk':u'硬盘','idc_id':u'机房','admin':u'使用人', 'business':u'业务',
                           'purchase_date':u'采购日期','warranty':u'保修时间','vendor':u'供应商','model':u'型号'}
    for i in params:
        if params[i][0].strip()=="":
            _errors[i]=u'请填写%s！' %(_form_keys[i])
    try:
        int(params['warranty'][0].strip())
    except Exception as e:
        _errors['warranty_num']=u'保修时间必须为数字！'
    if _errors:
        return False,_errors
    _sql='select sn from assets where id=%s and sn=%s'
    _cnt=dbutil.execute_commit_sql(_sql,(int(params['id'][0]),params['sn'][0].strip()))
    if _cnt:
        return True,{}
    else:
        _sql= 'select sn from assets where sn=%s'
        _cnt=dbutil.execute_commit_sql(_sql,(params['sn'][0]).strip())
        if _cnt:
            return False,{'sn':'sn编号重复！'}
        else:
            return True,{}

def update(params):
    _column='sn,ip,hostname,os,cpu,ram,disk,idc_id,admin,business,purchase_date,warranty,vendor,model'
    _columns=_column.split(',')
    _values=[params[i][0].strip() for i in _columns]
    _values.append(int(params['id'][0].strip()))
    _sql='update assets set sn=%s,ip=%s,hostname=%s,os=%s,cpu=%s,ram=%s,disk=%s,idc_id=%s,admin=%s,business=%s,purchase_date=%s,warranty=%s,vendor=%s,model=%s where id=%s'
    _cnt=dbutil.execute_commit_sql(_sql,(_values))
    if _cnt:
        return True
    else:
        return False

def delete(id):
    _sql='update assets set status=1 where id=%s'
    _cnt=dbutil.execute_commit_sql(_sql,(int(id),))
    if _cnt:
        return True
    else:
        return False

if __name__=='__main__':
    print get_list()