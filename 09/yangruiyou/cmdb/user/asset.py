# encoding: utf-8
from dbutils import execute_fetch_sql, execute_commit_sql


def get_idc_list():
    return [('1', '北京-亦庄'), ('2', '北京-酒仙桥'), ('3', '北京-西单'), ('4', '北京-东单')]


'''
返回所有资产信息
[
    {'sn' : '', 'id' : '', 'hostname':'', 'ip':'', .....}
]
'''


def get_list():
    _column = 'asset_id,sn,ipaddr,hostname,os,cpu,ram,disk,idc_id,admin,business,purchase_date,warranty_date,vendor,model'
    _columns = _column.split(',')
    _sql = 'SELECT {column} FROM assets WHERE status=0'.format(column=_column)
    _cnt, _rt_list = execute_fetch_sql(_sql)
    return [dict(zip(_columns, _line)) for _line in _rt_list]


'''
通过主键返回资产信息
None/{}
'''


def get_by_id(aid):
    _column = 'asset_id,sn,ipaddr,hostname,os,cpu,ram,disk,idc_id,admin,business,purchase_date,warranty_date,vendor,model'
    _columns = _column.split(',')
    _sql = 'SELECT {column} FROM assets WHERE status=0 and asset_id=%s'.format(column=_column)
    _args = (aid,)
    _cnt, _rt_list = execute_fetch_sql(_sql, _args)
    #print _cnt, _rt_list
    return None if _cnt == 0 else dict(zip(_columns, _rt_list[0]))


def get_by_sn(sn):
    _column = 'asset_id,sn,ipaddr,hostname,os,cpu,ram,disk,idc_id,admin,business,purchase_date,warranty_date,vendor,model'
    _columns = _column.split(',')
    _sql = 'SELECT {column} FROM assets WHERE status=0 and sn=%s'.format(column=_column)
    _args = (sn,)
    _cnt, _rt_list = execute_fetch_sql(_sql, _args)
    return None if _cnt == 0 else dict(zip(_columns, _rt_list[0]))


'''
在创建资产时对输入信息进行检查
True/False, error_msg{}
'''


def validate_create(asset):
    _is_ok = True
    _errors = {}
    '''
    字符串类型: sn,ip,hostname,os,admin,business,vendor,model
    检查是否为空(不允许),最小长度,最大长度
    '''
    for _key in 'sn,ipaddr,hostname,os,admin,business,vendor,model'.split(','):
        _value = asset.get(_key, '').strip()
        if _value == '':
            _is_ok = False
            _errors[_key] = '%s不允许为空' % _key
        elif len(_value) > 64:
            _is_ok = False
            _errors[_key] = '%s不允许超过64个字符' % _key

    if get_by_sn(asset.get('sn')):
        _is_ok = False
        _errors[_key] = 'sn已存在'
    '''
    取值选项:idc_id
    '''
    if asset.get('idc_id') not in [_value[0] for _value in get_idc_list()]:
        _is_ok = False
        _errors['idc'] = '机房选择不正确'

    '''
    数字类型: cpu,ram,disk,warranty
    检查数字类型isdigit, 最大值, 最小值
    '''
    _rules = {
        'cpu': {'min': 2, 'max': 64},
        'ram': {'min': 2, 'max': 512},
        'disk': {'min': 2, 'max': 2048},
        'warranty_date': {'min': 1, 'max': 5},
    }
    for _key in 'cpu,ram,disk,warranty_date'.split(','):
        _value = asset.get(_key, '').strip()
        print _key, _value
        if not _value.isdigit():
            _is_ok = False
            _errors[_key] = '%s不是整数' % _key
        else:
            _value = int(_value)
            _min = _rules.get(_key).get('min')
            _max = _rules.get(_key).get('max')
            if _value < _min or _value > _max:
                _is_ok = False
                _errors[_key] = '%s取值范围应该为%s ~ %s' % (_key, _min, _max)

    '''
    日期类型: purchase_date
    '''
    if not asset.get('purchase_date', ''):
        _is_ok = False
        _errors['purchase_date'] = '采购日期不同为空'

    return _is_ok, _errors


'''
创建资产，操作数据库
返回True/False
'''


def create(asset):
    _column_str = 'sn,ipaddr,hostname,os,admin,business,vendor,model,idc_id,cpu,ram,disk,warranty_date,purchase_date'
    _columns = _column_str.split(',')
    _args = []
    for _column in _columns:
        _args.append(asset.get(_column, ''))

    _sql = 'INSERT INTO assets({columns}) VALUES({values})'.format(columns=_column_str,
                                                                   values=','.join(['%s'] * len(_columns)))
    print _sql
    execute_commit_sql(_sql, _args)


'''
在修改资产时对输入信息进行检查
True/False, error_msg{}
'''


def validate_update(asset):
    return True, {}


'''
更新资产，操作数据库
返回True/False
'''


def update(asset):
    _column_str = 'sn,ipaddr,hostname,os,admin,business,vendor,model,idc_id,cpu,ram,disk,warranty_date,purchase_date'
    _columns = _column_str.split(',')
    _values = []
    _args = []
    for _column in _columns:
        _values.append('{column}=%s'.format(column=_column))
        _args.append(asset.get(_column, ''))
    _args.append(asset.get('asset_id'))

    _sql = 'UPDATE assets SET {values} WHERE asset_id=%s'.format(values=','.join(_values))
    # print _sql
    execute_commit_sql(_sql, _args)


'''
删除资产，操作数据库
返回True/False
'''


def delete(aid):
    _sql = 'UPDATE assets SET status=1 WHERE asset_id=%s'
    _args = (aid,)
    execute_commit_sql(_sql, _args)


if __name__ == '__main__':
    print get_list()
