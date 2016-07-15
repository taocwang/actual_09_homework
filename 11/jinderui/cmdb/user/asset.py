#encoding: utf-8
import sys
reload(sys)
sys.setdefaultencoding('utf-8')


from dbutils import MySQLConnection
'''
返回所有资产信息
[{'sn':'','id':''}]
'''

class Asset(object):
	"""docstring for asset"""

	#返回资产信息 没有删除的(status=0)
	@classmethod
	def get_list(cls):
		_column = 'id,sn,ip,hostname,os,cpu,ram,disk,idc_id,admin,business,purchase_date,warranty,vendor,model'
		_columns = _column.split(',')
		_sql = 'select {column} from assets where status=0'.format(column=_column)
		_cnt,_rt_list = MySQLConnection.execute_sql(_sql)

		return [dict(zip(_columns,_line)) for _line in _rt_list]

	#返回资产信息。删除和不删除的都返回(status 是0和1的都返回)
	@classmethod
	def get_list2(cls):
		_column = 'id,sn,ip,hostname,os,cpu,ram,disk,idc_id,admin,business,purchase_date,warranty,vendor,model'
		_columns = _column.split(',')
		_sql = 'select {column} from assets'.format(column=_column)
		_cnt,_rt_list = MySQLConnection.execute_sql(_sql)

		return [dict(zip(_columns,_line)) for _line in _rt_list]


	@classmethod
	def get_idcs_list(cls):
		_sql = 'select id,name from idcs where status=0'
		_cnt,_rt_list = MySQLConnection.execute_sql(_sql)
		return dict(_rt_list)  #返回的是一个字典

	@classmethod
	def get_by_id(cls,id):
		_column = 'id,sn,ip,hostname,os,cpu,ram,disk,idc_id,admin,business,purchase_date,warranty,vendor,model'
		_columns = _column.split(',')
		_sql = 'select {column} from assets where status=0 and id=%s'.format(column=_column)
		_args = (id,)
		_cnt,_rt_list = MySQLConnection.execute_sql(_sql,_args)

		return dict(zip(_columns, _rt_list[0]))




	'''
	创建资产时对输入信息进行检查
	'''
	@classmethod
	def validate_create(cls,sn,warranty,cpu,ram,disk,ip):
		assets_list=cls.get_list2()  #判断所有资产信息，删除和不删除的都有
		for asset in assets_list:
			if asset['sn'] == sn:
				return False,u'sn存在不能重复'

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
	@classmethod
	def create(cls,sn, warranty,cpu,ram,disk,ip,idc_id):
		_sql = 'insert into assets(sn,warranty,cpu,ram,disk,ip,idc_id) values(%s,%s,%s,%s,%s,%s,%s)'
		_args = (sn, warranty, cpu,ram,disk,ip,idc_id)
		MySQLConnection.execute_sql(_sql,_args,fetch=False)

	'''
	更新资产时对输入信息进行检查
	'''
	@classmethod
	def validate_update(cls,sn, warranty, cpu,ram,disk):
		if not str(warranty).isdigit() or int(warranty) <= 0 or int(warranty) > 10:
			return False,u'报修时间不正确,需要是数字且0-10范围内'
		return True, {}

	'''
	更新资产信息
	'''
	@classmethod
	def update(cls,warranty,cpu,ram,disk,idc_id,ip,id):
		_sql = 'update assets set warranty=%s,cpu=%s,ram=%s,disk=%s,idc_id=%s,ip=%s where id =%s'
		print _sql
		_args = (warranty,cpu,ram,disk,idc_id,ip,id)
		print _args
		MySQLConnection.execute_sql(_sql,_args,fetch=False)

	'''
	删除资产信息
	'''
	@classmethod
	def delete(cls,id):
		_sql = 'update assets set status=1  where id =%s'
		_args = (id,)
		MySQLConnection.execute_sql(_sql,_args,fetch=False)

if __name__ == '__main__':
	print Asset.get_by_id(5)




