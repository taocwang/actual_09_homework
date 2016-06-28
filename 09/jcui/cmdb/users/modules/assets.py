#encoding:utf-8
from dbutils import excute_fetch_sql,excute_commit_sql


''
'''
返回所有资产信息
[{'sn':'','id':''}]

'''
def get_list():
    _column = 'id,sn,ip,hostname,os,cpu,ram,disk,idc_id,admin,business,purchase_date,warranty,vendor,model,status'
    _columns = _column.split(',')
    _sql = 'select {column} from assets where status=0'.format(column=_column)
    _cnt,_rt_list = excute_fetch_sql(_sql)
    rt_list = [dict(zip(_columns,i)) for i in _rt_list]
    return [dict(zip(_columns,i)) for i in _rt_list]

'''
通过主键返回资产信息
None/{}
'''
def get_by_id(aid):
    return None

'''
创建资产时对输入信息检查
True/False,error_msg{}
'''
def validate_create(params):
    collent =  params.keys()
    _sql = 'select * from assets where %s = %s and status = 0'
    result = {}
    for i in collent:
        if params[i] == '':
            result[i] = '%s 不能为空' % i
    #检查SN的唯一
    sn = params.get('sn')
    if len(sn) >= 6:
        _args = ('sn',sn)
        _cnt,rt_list = excute_fetch_sql(_sql,_args)
        if _cnt != 0:
            result['sn'] = 'SN编码已存在'
    result['sn'] = 'SN编码太短'

    #检查IP的唯一
    ip = params.get('ip')
    if ip_check(ip):
        _args = ('ip',ip)
        _cnt, rt_list = excute_fetch_sql(_sql, _args)
        if _cnt != 0:
            result['ip'] = 'IP地址已存在'
    result['ip'] = 'IP地址不合法'

    #检查主机名的唯一
    hostname = params.get('hostname')
    _args = ('hostname', hostname)
    _cnt, rt_list = excute_fetch_sql(_sql, _args)
    if _cnt != 0:
        result['hostname'] = '主机名已存在'

    if result:
        create(params)
    return False,result.values()

'''
创建资产,操作数据库
返回True/False
'''

def create(params):
    collent = tuple(params.keys())
    _sql = 'insert into '
    print collent
    return False,'入库失败'

'''
修改资产时对输入信息检查
True/False,error_msg{}
'''
def validate_update():
    return True,{}

'''
修改资产,操作数据库
返回True/False
'''
def update():
    pass

'''
删除资产,操作数据库
True/False
'''
def delete():
    pass


def ip_check(ip):
    q = ip.split('.')
    return len(q) == 4 and len(filter(lambda x: x >= 0 and x <= 255, \
        map(int, filter(lambda x: x.isdigit(), q)))) == 4

if __name__ == '__main__':
   print ip_check('123.123.123.123')