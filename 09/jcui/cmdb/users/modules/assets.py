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
def validate_create():
    return True,{}

'''
创建资产,操作数据库
返回True/False
'''

def create():
    pass

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


if __name__ == '__main__':
   print get_list()