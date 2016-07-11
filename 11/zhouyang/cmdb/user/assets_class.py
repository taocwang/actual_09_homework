#!/bin/env python
#encoding:utf-8
from dbutils import MYSQLConnection

class Asset(object):
    def __init__(self,**kwargs):
        self.id=id
        self.sn=sn
        self.iner_ip=iner_ip
        self.hostname=hostname
        self.cpu=cpu

    @classmethod
    def get_list(cls,wheres={}):
        _colum='id,sn,iner_ip,hostname,os,cpu,ram,dick,idc_id,admin,bak_admin,business,warranty,verdor,model,status'
        _args=[]
        _res=[]
        _sql="select {colume} from t_assets where 1=1 and status = 1 ".format(colume=_colum)
        for _key,_value in wheres.items():
            _sql += "AND {key} = %s".format(key=_key)
            _args.append(_value)

        _cnt,_rt_list=MYSQLConnection.excute_sql(_sql,_args)
        for _line in _rt_list:
            _res.append(dict(zip(_colum.split(','),_line)))

        return  _res

    @classmethod
    def get_by_sn(cls,sn):
        _colum={'sn':sn}
        _rt=cls.get_list(_colum)
        return _rt[0] if len(_rt) !=0 else None

    @classmethod
    def validate_create(cls,params):
        _new_info=dict(params)
        errors=[]
        if not _new_info['sn'][0].isdigit():
            errors.append('SN必须为数字')
        if _new_info['ip'][0].count('.') != 3:
            errors.append('不是合法四段式IP')
        if not ''.join(_new_info['ip'][0].split('.')).isdigit():
            errors.append('IP必须为数字')
        if errors:
            return False,errors
        else:
            return True,errors

    @classmethod
    def create(cls,params):
        _new_info=dict(params)
        _sql="insert into `t_assets` (warranty, ram, verdor, business, admin, iner_ip, hostname, idc_id, sn, model, dick, os, cpu, purchase_date) values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);"
        _args=(_new_info['warranty'][0],int(_new_info['ram'][0]),_new_info['vendor'][0],_new_info['business'][0],_new_info['admin'][0],_new_info['ip'][0],_new_info['hostname'][0],_new_info['idc_id'][0],int(_new_info['sn'][0]),_new_info['model'][0],int(_new_info['disk'][0]),_new_info['os'][0],int(_new_info['cpu'][0]),_new_info['purchase_date'][0])
        _cnt,_res=MYSQLConnection.excute_sql(_sql,_args,fetch=False)
        if _cnt == 0:
            return False,'入库失败，请联系管理员'
        return True,'资产添加成功'

    @classmethod
    def validate_update(cls,ip):
        '''修改资产时进行检查'''
        errors=[]
        if ip.count('.') != 3:
            errors.append('不是合法四段式IP')
        if ''.join(ip.split('.')).isdigit():
            errors.append('IP必须为数字')
        if errors:
            return False,errors
        else:
            return True,errors

    @classmethod
    def update(cls,sn,ip,cpu,ram,disk,admin):
        _sql="update t_assets set iner_ip=%s,cpu=%s,ram=%s,dick=%s,admin=%s where sn=%s;"
        _args=(ip,int(cpu),int(ram),int(disk),admin,int(sn))
        _cnt=MYSQLConnection.excute_sql(_sql,_args,fetch=False)
        if _cnt == 0:
            return False,'信息更新失败，请联系管理员'
        return True,'信息修改成功'

    @classmethod
    def asset_del(cls,sn):
        _sql="update t_assets set status=0 where sn=%s;"
        _args=(sn,)
        _cnt=MYSQLConnection.excute_sql(_sql,_args,fetch=False)
        if _cnt == 0:
            return False,'删除资产失败'
        return True,'删除资产%s成功' % sn

class Performs(object):
    @classmethod
    def performs(cls,req):
        _time=req.get('time')
        _ip=req.get('ip')
        _cpu=req.get('cpu')
        _ram=req.get('ram')
        _sql="insert into performs(`time`,`ip`,`cpu`,`ram`) VALUES (%s,%s,%s,%s)"
        print _sql
        _args=(_time,_ip,_cpu,_ram)
        print _args
        _cnt,_res=MYSQLConnection.excute_sql(_sql,_args,fetch=False)
        if _cnt == 0:
            return False,'入库失败'
        return True,''

if __name__ == '__main__':
    print Asset.get_list()