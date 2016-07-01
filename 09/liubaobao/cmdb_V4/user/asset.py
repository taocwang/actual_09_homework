#!encoding:utf-8
from dbutils import execute_fetch_sql,bulker_commit_sql,execute_commit_sql
import re

'''
获取资产列表
返回一个字典
'''
def get_list():
    _column = 'id,sn,ip,hostname,os,cpu,ram,disk,idc_id,admin,business,purchase_date,warranty,vendor,model'
    _columns = _column.split(',')
    _sql = 'select {column} from assets where status = 0'.format(column=_column)
    _cnt,_rt_list = execute_fetch_sql(_sql)
    dic = [dict(zip(_columns,_line)) for _line in _rt_list]
    for line in dic:
         _idc_id = line.get('idc_id')
         _idc_name = get_idcs_name(line.get('idc_id'))
         line['idc_id'] = [_idc_id,_idc_name]
    return dic


'''
通过id进行查询
返回一个字典
'''
def get_by_id(id):
    _column = 'id,sn,ip,hostname,os,cpu,ram,disk,idc_id,admin,business,purchase_date,warranty,vendor,model'
    _columns = _column.split(',')
    _sql = 'select {column} from assets where status = 0 and id=%s'.format(column=_column)
    args =(id,)
    _cnt,_rt_list = execute_fetch_sql(_sql,args)
    return [dict(zip(_columns,_line)) for _line in _rt_list][0]



'''
检查ip是否符合格式的函数,python正则表达式
返回True/False
'''
def validateIp(ip):
    p = re.compile("^((?:(2[0-4]\d)|(25[0-5])|([01]?\d\d?))\.){3}(?:(2[0-4]\d)|(255[0-5])|([01]?\d\d?))$")
    if len(ip)>6:
        if re.match(p, ip):
            return True
    return False



'''
检查sn编号是否重复
返回True/Fasle和id
'''
def validateSn(sn):
    _sql = "select * from assets where sn = %s"
    _args =(sn,)
    _cnt,_rt_list = execute_fetch_sql(_sql,_args)
    if _cnt:
        return True,_rt_list[0][0]
    return False,''




'''
检查主机名是否重复
返回True/false和id值
'''
def validateHostname(hostname):
    _sql = "select * from assets where hostname = %s"
    _args =(hostname,)
    _cnt,_rt_list = execute_fetch_sql(_sql,_args)
    if _cnt:
        return True,_rt_list[0][0]
    return False,[]



'''
检查添加资产
返回True和Flase和错误列表
'''
def validate_create(_sn,_ip,_hostname,_os,_cpu,_ram,_disk,_idc_id,_admin,_business,_purchase_date,_warranty,_model,_vendor):
    error = []
    if str(_sn).strip() == '':
        error.append('sn编号不能为空')
    else:
        _is_ok,_rt_list = validateSn(_sn)
        if _is_ok:
            error.append('sn编号已经存在')
    if str(_ip).strip() == '':
        error.append('ip地址不能为空')
    else:
        if not validateIp(_ip):
            error.append('ip地址格式不正确')
    if str(_hostname).strip() == '':
        error.append('主机名不能为空')
    else:
        _is_ok, _rt_list = validateHostname(_hostname)
        if _is_ok:
            error.append('主机名已经存在')
    if str(_idc_id).strip() == '':
        error.append('Idc不能为空')
    if str(_os).strip() == '':
        error.append('系统不能为空')
    if str(_admin).strip() == '':
        error.append('业务人不能为空')
    if str(_business).strip() == '':
        error.append('业务不能为空')
    if str(_purchase_date).strip() == '':
        error.append('采购日期不能为空')
    if str(_warranty).strip() == '':
        error.append('保修日期不能为空')
    if str(_model).strip() == '':
        error.append('型号不能为空')
    if str(_vendor).strip() == '':
        error.append('供应商不能为空')
    if len(error) > 0:
        return False,error
    return True,''



'''
添加资产
'''
def create(sql_list=[]):
    #_sql_args = ','.join(sql_list)
    _sql = "insert into assets(sn,ip,hostname,os,cpu,ram,disk,idc_id,admin,business,purchase_date,warranty,model,vendor) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    args = tuple(sql_list)
    execute_commit_sql(_sql,args)




'''
检查更新用户
返回True/false和错误列表
'''
def validate_update(_id,_sn,_ip,_hostname,_os,_cpu,_ram,_disk,_idc_id,_admin,_business,_purchase_date,_warranty,_model,_vendor):
    error = []
    assets = get_by_id(_id)
    if str(_sn).strip() == '':
        error.append('sn编号不能为空')
    else:
        _is_ok,sn_id = validateSn(_sn)
        print sn_id
        print _id
        print _is_ok
        if _is_ok and int(sn_id) != int(_id):
            error.append('sn编号已经存在')
    if str(_ip).strip() == '':
        error.append('ip地址不能为空')
    else:
        if not validateIp(_ip):
            error.append('ip地址格式不正确')
    if str(_hostname).strip() == '':
        error.append('主机名不能为空')
    else:
        _is_ok,hostname_id = validateHostname(_hostname)
        if _is_ok and int(hostname_id) != int(_id):
            error.append('主机名已经存在')
    if str(_idc_id).strip() == '':
        error.append('Idc不能为空')
    if str(_os).strip() == '':
        error.append('系统不能为空')
    if str(_admin).strip() == '':
        error.append('业务人不能为空')
    if str(_business).strip() == '':
        error.append('业务不能为空')
    if str(_purchase_date).strip() == None:
        error.append('采购日期不能为空')
    if str(_warranty).strip() == None:
        error.append('保修日期不能为空')
    if str(_model).strip() == '':
        error.append('型号不能为空')
    if str(_vendor).strip() == '':
        error.append('供应商不能为空')
    if len(error) > 0:
        return False,error
    return True,''



'''
更新资产的操作
'''
def update(sql_list=[]):
    _sql="update assets set sn=%s,ip=%s,hostname=%s,os=%s,cpu=%s,ram=%s,disk=%s,idc_id=%s,admin=%s,business=%s,purchase_date=%s,warranty=%s,model=%s,vendor=%s where id=%s"
    args = tuple(sql_list)
    execute_commit_sql(_sql,args)



'''
获取idcs()
机房的名字
'''
def get_idcs():
    _sql = 'select * from idcs'
    _cnt,_rt_list = execute_fetch_sql(_sql)
    return [ (_line[0],_line[1]) for _line in _rt_list]




def get_idcs_name(idc_id):
    _sql = 'select * from idcs where id = %s'
    args = (idc_id,)
    _cnt,_rt_list = execute_fetch_sql(_sql,args)
    return _rt_list[0][1]



'''
删除资产
返回True和False
'''
def delete(id):
    _sql = "update assets set status = 1 where id =%s"
    args = (id,)
    _cnt,_rt_list = execute_commit_sql(_sql,args)
    if _cnt:
        return True
    return False



if __name__ == '__main__':
    #create(['010','192.168.1.2','server_01','centos',1,100,200,2,'admin','nginx','0000-00-00','0000-00-00','dell','dell'])
    #print get_idcs_name(2)
    # print validateSn('sadsad')
    # print validateHostname('lbb123')
    #print get_by_id(3)
    #update(['022','192.168.1.2','server_01','centos',1,100,200,2,'admin','nginx','0000-00-00','0000-00-00','dell','dell',2])
    print get_list()
    print get_idcs_name(1)