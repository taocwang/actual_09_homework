#encoding: utf-8
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

import json
import gconf
import MySQLdb
from dbutils import execute_sql

def get_list(asset_id=None):
	rt = []
	columns=("id","sn","ip","hostname","os","cpu","ram","disk","idc_id","admin","business","purchase_date","warranty","vendor","model","status","idc_name")
	if asset_id:
		sql = 'SELECT a.id,a.sn,a.ip,a.hostname,a.os,a.cpu,a.ram,a.disk,a.idc_id,a.admin,a.business,a.purchase_date,a.warranty,a.vendor,a.model,a.status, b.`name` idc_name from assets a, idcs b WHERE a.id=%s and a.idc_id=b.id'
		args = (asset_id,)
	else:
		sql = 'SELECT a.id,a.sn,a.ip,a.hostname,a.os,a.cpu,a.ram,a.disk,a.idc_id,a.admin,a.business,a.purchase_date,a.warranty,a.vendor,a.model,a.status, b.`name` idc_name from assets a, idcs b WHERE a.status=0 and a.idc_id=b.id'	
		args = ()
	count, rt_list = execute_sql(sql,args)
	for line in rt_list:
		rt.append(dict(zip(columns, line)))
	rt[0]['purchase_date']=str(rt[0]['purchase_date'])	
	return rt

def idcs_list():
	sql = 'select id,name from idcs where status=0'
	count, rt_list = execute_sql(sql)
	return rt_list

def validate(asset_info,repeat=True):
	errors = {}
	for value in asset_info:
		if asset_info[value] == "":
			errors[value] = "%s为空" % value
	if errors != {}:
		return False, errors			
	if not asset_info["cpu"].isdigit():
		errors["cpu"] = "cpu核数只能写整数,请重新填写"
	if not asset_info["disk"].isdigit():
		errors["disk"] = "硬盘大小只能写整数,请重新填写"
	if not asset_info["ram"].isdigit():
		errors["ram"] = "内存大小只能写整数,请重新填写"
	if not asset_info["warranty"].isdigit():
		errors["warranty"] = "保修时间只能写整数,请重新填写"
	if errors != {}:
		return False, errors
	if repeat:	
		sql = 'select sn from assets where sn=%s'
		args =(asset_info['sn'],)
		count, rt_list = execute_sql(sql,args)
		if count != 0:
			errors['sn'] = "sn编码重复,请重新输入"
	if errors != {}:
		return False, errors
	else:
		return True, {}
	
def create(asset_info):
	sql = 'insert into assets (sn,ip,hostname,os,cpu,ram,disk,idc_id,admin,business,purchase_date,warranty,vendor,model) values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'
	args = (asset_info.get('sn'),asset_info.get('ip'),asset_info.get('hostname'),asset_info.get('os'),asset_info.get('cpu'),asset_info.get('ram'),asset_info.get('disk'),asset_info.get('idc_id'),asset_info.get('admin'),asset_info.get('business'),asset_info.get('purchase_date'),asset_info.get('warranty'),asset_info.get('vendor'),asset_info.get('model'))
	fetch = False
	count, rt_list = execute_sql(sql, args, fetch)
	return count != 0		

def update(asset_info):
	sql = 'update assets set ip=%s,hostname=%s,os=%s,cpu=%s,ram=%s,disk=%s,idc_id=%s,admin=%s,business=%s,purchase_date=%s,warranty=%s,vendor=%s,model=%s where id=%s'
	args = (asset_info.get('ip'),asset_info.get('hostname'),asset_info.get('os'),asset_info.get('cpu'),asset_info.get('ram'),asset_info.get('disk'),asset_info.get('idc_id'),asset_info.get('admin'),asset_info.get('business'),asset_info.get('purchase_date'),asset_info.get('warranty'),asset_info.get('vendor'),asset_info.get('model'),asset_info.get('id'))
	fetch = False
	count, rt_list = execute_sql(sql, args, fetch)
	return count != 0	
	
def drop(asset_id):
	sql = 'update assets set status=1 where id=%s'
	args = (asset_id,)
	fetch = False
	count, rt_list = execute_sql(sql, args, fetch)
	return count != 0
	
if __name__ == "__main__":
	a={"admin":"hjun", "business":"test","cpu":64,"disk":3072,"hostname":"test01","idc_id":1,"ip":"192.168.1.2","model":"R730","os":"centos6","purchase_date":'2016-06-29',"ram":512,"sn":"12345670","vendor":"dell","warranty":3}
	print create(a)