#coding:utf-8
import db_act

def get_list():
    '''返回全部资产信息'''
    comm="id,sn,iner_ip,hostname,os,cpu,ram,dick,idc_id,admin,bak_admin,business,warranty,verdor,model,status"
    _sql="select {0} from t_assets where status=1;".format(comm)
    _args=comm.split(',')
    _cnt,_rt_list=db_act.db_act(_sql)
    return [dict(zip(_args,_line)) for _line in _rt_list]

def get_by_id(mid):
    '''通过主键获取资产信息'''
    comm="id,sn,iner_ip,hostname,os,cpu,ram,dick,idc_id,admin,bak_admin,business,warranty,verdor,model,status"
    _sql="select {0} from t_assets where sn={1};".format(comm,mid)
    _cnt,_rt_list=db_act.db_act(_sql)
    comm2=comm.split(',')
    return dict(zip(comm2,_rt_list[0]))


def validate_create(params):
    '''创建资产时进行检查'''
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

def create(params):
    '''创建资产'''
    _new_info=dict(params)
    _sql="insert into `t_assets` (warranty, ram, verdor, business, admin, iner_ip, hostname, idc_id, sn, model, dick, os, cpu, purchase_date) values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);"
    _args=(_new_info['warranty'][0],int(_new_info['ram'][0]),_new_info['vendor'][0],_new_info['business'][0],_new_info['admin'][0],_new_info['ip'][0],_new_info['hostname'][0],_new_info['idc_id'][0],int(_new_info['sn'][0]),_new_info['model'][0],int(_new_info['disk'][0]),_new_info['os'][0],int(_new_info['cpu'][0]),_new_info['purchase_date'][0])
    print len(_args)
    return db_act.db_act(_sql,_args,fetch=False)



def validate_update(ip):
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



def update(sn,ip,cpu,ram,disk,admin):
    '''更新资产'''
    _sql="update t_assets set iner_ip=%s,cpu=%s,ram=%s,dick=%s,admin=%s where sn=%s;"
    _args=(ip,int(cpu),int(ram),int(disk),admin,int(sn))
    return db_act.db_act(_sql,_args,fetch=False)

def delete(sn):
    '''删除资产'''
    _sql="update t_assets set status=0 where sn=%s;"
    _args=(sn,)
    return db_act.db_act(_sql,_args,fetch=False)

if __name__=='__main__':
    print get_by_id(33331555)