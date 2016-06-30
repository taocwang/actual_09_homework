# encoding: utf-8
'''
返回所有资产信息
【{'sn': '', 'id': '', 'hostname':'', 'ip': '', ...},{},{}】
'''
from dbutils import execute_fetch_sql, execute_commit_sql

def get_list():
    _column = 'id,sn,ip,hostname,os,purchase_date,warranty,vendor,model,idc_id,admin,business,cpu,mem,disk'
    _columns = _column.split(',')
    _sql = 'select {column} from assets where status=0'.format(column=_column)
    print _sql
    _cnt, _rt_list = execute_fetch_sql(_sql)
    return [dict(zip(_columns, _line)) for _line in _rt_list]



'''
通过主键返回资产信息
返回None/{}
'''
def get_by_id(aid):
    _column = 'id,sn,ip,hostname,os,purchase_date,warranty,vendor,model,idc_id,admin,business,cpu,mem,disk'
    _columns = _column.split(',')
    _sql = 'select * from assets where sn=%s'
    _cnt, _rt_list = execute_fetch_sql(_sql, (aid,))
    return _cnt, dict(zip(_columns,_rt_list[0]))


'''
在创建资产时对信息进行检查
返回None
'''
def validate_create(sn, ip, hostname, os, purchase_date, warranty, vendor, model, idc_id, admin, business, cpu, mem, disk):
    _cnt, _rt_list=get_by_id(sn)
    error = {'error':[]}
    rt = True
    if _cnt:
        error['error'].append('SN号已存在')
        rt = False
        return Flase, error
    iplist = ip.split(',')
    for i in iplist:
        if 0<i<255 and i != '':
            pass
        else:
            rt = False
            error['error'].append('ip地址不符合规范')
    if hostname == '' or os == '' or admin == '':
        rt = False
        error['error'].append('ip或主机或操作系统或使用人不能为空')
    if warranty.isdigit() and idc_id.isdigit() and cpu.isdigit() and mem.isdigit() and disk.isdigit():
        pass
    else:
        rt = False
        error['error'].append('保修时长或机房ID或cpu或内存或磁盘不是整数')
    return rt, error


'''
创建资产,更新数据库
返回True/False
'''
def create(sn, ip, hostname, os, purchase_date, warranty, vendor, model, idcs, admin, business, cpu, mem, disk):
    _sql = 'insert into assets(sn, ip, hostname, os, purchase_date, warranty, vendor, model, idc_id, admin, business, cpu, mem, disk) values(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)'
    args = (sn, ip, hostname, os, purchase_date, warranty, vendor, model, idcs, admin, business, cpu, mem, disk)
    execute_commit_sql(_sql, args)
    return True


'''
在修改资产时对信息进行检查
返回True/False, error_msg{}
'''
def validate_update(ip, hostname, os, purchase_date, warranty, vendor, model, idc_id, admin, business, cpu, mem, disk):
    error = {'error': []}
    rt = True
    iplist = ip.split('.')
    print iplist
    for i in iplist:
        if 0 < int(i) < 255 and i != '':
            pass
        else:
            rt = False
            error['error'].append('ip地址不符合规范')
    if ip == '' or hostname == '' or os == '' or admin == '':
        rt = False
        error['error'].append('操作系统或使用人不能为空')
    if warranty.isdigit() and idc_id.isdigit() and cpu.isdigit() and mem.isdigit() and disk.isdigit():
        pass
    else:
        rt = False
        error['error'].append('保修时长或机房ID或cpu或内存或磁盘不是整数')
    return rt, error


'''
更新资产,更新数据库
返回True/False
'''
def update(ip, hostname, os, purchase_date, warranty, vendor, model, idc_id, admin, business, cpu, mem, disk, sn):
    _sql = 'update assets set ip=%s, hostname=%s, os=%s, purchase_date=%s, warranty=%s, vendor=%s, model=%s, idc_id=%s, admin=%s, business=%s, cpu=%s, mem=%s, disk=%s where sn=%s'
    args = (ip, hostname, os, purchase_date, warranty, vendor, model, idc_id, admin, business, cpu, mem, disk, sn)
    execute_commit_sql(_sql, args)
    return True

'''
删除资产,更新数据库
返回True/False
'''
def delete(aid):
    _sql = 'update assets set status=1 where sn=%s'
    args = (aid,)
    _cnt, _rt_list = execute_commit_sql(_sql, args)
    return _cnt, _rt_list


if __name__ == '__main__':
    print get_list()