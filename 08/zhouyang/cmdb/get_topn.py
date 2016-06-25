#coding:utf-8
'''从nginx的日志中找出access前n的信息'''

from db_act import db_act

def get_topn(n=10):
    _sql="select src_ip,url_path,stat_code,count(*) from nginx_log group by src_ip,url_path,stat_code order by count(*) desc limit %s;"
    args=n
    db_cnt,rt_list=db_act(_sql,args)
    return rt_list
