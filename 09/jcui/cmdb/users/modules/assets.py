#encoding:utf-8
import json

from dbutils import excute_fetch_sql,excute_commit_sql


''
'''
返回所有资产信息
[{'sn':'','id':''}]

'''
def get_list():
    _column = 'id,sn,ip,hostname,os,cpu,ram,disk,idc_name,admin,business,purchase_date,warranty,vendor,model,status'
    _columns = _column.split(',')
    _sql = 'select {column} from assets,idc_name where assets.status=0 and assets.idc_id = idc_name.idc_id;'.format(column=_column)
    # _sql = 'select {column} from assets where status=0'.format(column=_column)
    _cnt,_rt_list = excute_fetch_sql(_sql)
    rt_list = [dict(zip(_columns,i)) for i in _rt_list]
    return [dict(zip(_columns,i)) for i in _rt_list]

'''
通过主键返回资产信息
None/{}
'''
def get_by_id(aid):
    _column = 'id,sn,ip,hostname,os,cpu,ram,disk,idc_id,admin,business,purchase_date,warranty,vendor,model,status'
    # _sql = 'select {coll} from assets,idc_name where assets.status=0 and assets.idc_id = idc_name.idc_id and id = %s'.format(coll=_column)
    _sql = 'select {coll} from assets where id = %s'.format(coll=_column)
    _args = (aid,)
    _cnt,_rt_list = excute_fetch_sql(_sql,_args)
    rt = []
    if _cnt != 0:
        for x in range(len(_column.split(','))):
            # print _column.split(',')[x],_rt_list[0][x]
            rt.append((_column.split(',')[x],_rt_list[0][x]))
        return dict(rt)
    return ''

'''
创建资产时对输入信息检查
True/False,error_msg{}
'''
def validate_create(params):
    collent =  params.keys()
    result = {}
    for i in collent:
        if params[i] == '':
            result[i] = '%s 不能为空' % i
    #检查SN的唯一
    sn = params.get('sn').strip()
    if len(sn) >= 6:
        _sql = 'select * from assets where sn = %s and status = 0'
        _args = (sn,)
        _cnt,rt_list = excute_fetch_sql(_sql,_args)
        if _cnt != 0:
            result['sn'] = 'SN编码已存在'
    else:
        result['sn'] = 'SN编码太短'

    #检查IP的唯一
    ip = params.get('ip').strip()
    if ip_check(ip):
        _sql = 'select * from assets where ip = %s and status = 0'
        _args = (ip,)
        _cnt, rt_list = excute_fetch_sql(_sql, _args)
        if _cnt != 0:
            result['ip'] = 'IP地址已存在'
    else:
        result['ip'] = 'IP地址不合法'

    #检查主机名的唯一
    hostname = params.get('hostname').strip()
    _sql = 'select * from assets where hostname = %s and status = 0'
    _args = (hostname,)
    _cnt, rt_list = excute_fetch_sql(_sql, _args)
    if _cnt != 0:
        result['hostname'] = '主机名已存在'

    if not result:
        return create(params)
    return False,result.values()

'''
创建资产,操作数据库
返回True/False
'''

def create(params):
    _collent = []
    _values = []
    for k,v in params.items():
        _collent.append(k)
        _values.append(v)
    _sql = 'insert into assets({coll}) values%s'.format(coll=','.join(_collent))
    _args = (tuple(_values),)
    # print tuple(_values)
    _cnt,_rtlist = excute_commit_sql(_sql,_args)
    if _cnt != 0:
        return True,'添加成功'
    return False,'入库失败'

'''
获取机房名称
'''
def get_idc_name():
    _sql  = 'select idc_id,idc_name from idc_name'
    rt = []
    _cnt, _rt_list = excute_fetch_sql(_sql)
    for i in _rt_list:
        rt.append(i)
    return rt


'''
修改资产时对输入信息检查
True/False,error_msg{}
'''
def validate_update(params):
    collent = params.keys()
    result = {}
    for i in collent:
        if params[i] == '':
            result[i] = '%s 不能为空' % i
    if not result:
        return update(params)
    return False, result.values()

'''
修改资产,操作数据库
返回True/False
'''
def update(params):
    _column = 'sn,ip,hostname,os,cpu,ram,disk,idc_id,admin,business,purchase_date,warranty,vendor,model'
    id = params.get('id')
    rt_set = []
    for i in _column.split(','):
        rt_set.append(i+'='+'\'%s\'' % params[i])
    _sql = 'update assets set {coll} where id = %s'.format(coll=','.join(rt_set))
    _args = (id,)
    _cnt, _rtlist = excute_commit_sql(_sql, _args)
    if _cnt != 0:
        return True,'更新成功'
    return False, '更新失败'

'''
删除资产,操作数据库
True/False
'''
def delete(id):
    _sql = 'update assets set status = 1 where id=%s'
    _args = (id,)
    _cnt, _rtlist = excute_commit_sql(_sql, _args)
    if _cnt != 0:
        return True,'删除成功'
    return False,'删除失败'

'''
IP地址检查
'''
def ip_check(ip):
    q = ip.split('.')
    return len(q) == 4 and len(filter(lambda x: x >= 0 and x <= 255, \
        map(int, filter(lambda x: x.isdigit(), q)))) == 4

if __name__ == '__main__':
   print ip_check('123.123.123.123')