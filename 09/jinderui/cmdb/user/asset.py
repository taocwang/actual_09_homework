#encoding:utf-8
from dbutils import execute_fetch_sql,execute_commit_sql,execute_del_sql,execute_update_sql

'''
返回所有资产信息
[{'sn':'','id':''}]
'''
def get_list():
	_column = 'id,sn,ip,hostname,os,cpu,ram,disk,idc_id,admin,business,purchase_date,warranty,vendor,model'
	_columns = _column.split(',')
	_sql = 'select {column} from assets where status=0'.format(column=_column)
	_cnt,_rt_list = execute_fetch_sql(_sql)
	return [dict(zip(_columns,_line)) for _line in _rt_list]

def get_idcs_list():

	_columns = ('id','name')
	_sql = 'select id,name from idcs where status=0'
	_cnt,_rt_list = execute_fetch_sql(_sql)
	a = [dict(zip(_columns,_line)) for _line in _rt_list]
	print a
	return [dict(zip(_columns,_line)) for _line in _rt_list]


'''
通过主键返回资产信息
'''
def get_by_id(aid):
	return None

'''
创建资产时对输入信息进行检查
'''
def validate_create(sn,warranty,cpu,ram,disk,ip):
	assets_list=get_list()
	for asset in assets_list:
		if asset['sn'] == sn:
			return False,u'sn存在不能重复'
	print ip
	if ip == '' or ip.isalpha():
		return False,u'ip not null and not str'


	testip = ip.split('.')
	if len(testip) == 4 :
		if int(testip[0]) >255 or int(testip[1]) > 255 or int(testip[2]) > 255 or int(testip[3]) >255:
			return False,u'ip failed'
	else:
		return False,u'ip 4'

	if not str(warranty).isdigit() or int(warranty) <= 0 or int(warranty) > 10:
		return False,u'报修时间不正确,需要是数字且0-10范围内'
	return True,{}

'''
创建资产信息
'''
def create(sn, warranty,cpu,ram,disk,ip,idc_id):
	_sql = 'insert into assets(sn,warranty,cpu,ram,disk,ip,idc_id) values(%s,%s,%s,%s,%s,%s,%s)'
	_args = (sn, warranty, cpu,ram,disk,ip,idc_id)
	execute_commit_sql(_sql,_args)

'''
更新资产时对输入信息进行检查
'''
def validate_update(sn, warranty, cpu,ram,disk):
	if not str(warranty).isdigit() or int(warranty) <= 0 or int(warranty) > 10:
		return False,u'报修时间不正确,需要是数字且0-10范围内'
	return True, {}

'''
更新资产信息
'''

def update(warranty,cpu,ram,disk,sn):
	_sql = 'update assets set warranty=%s,cpu=%s,ram=%s,disk=%s where sn =%s'
	_args = (warranty,cpu,ram,disk,sn)
	execute_update_sql(_sql,_args)

'''
删除资产信息
'''
def delete(sn):
	_sql = 'delete from assets where sn =%s'
	print _sql
	_args = (sn,)
	execute_del_sql(_sql,_args)

if __name__ == '__main__':
	print get_idcs_list()