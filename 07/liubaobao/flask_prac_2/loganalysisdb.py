#!encoding:utf-8
from dbutils import execute_sql

def get_topn(topn=10):
    _sql = 'select ip, url, code, count from log order by count desc limit %s'
    args = (topn,)
    _count,_rt_list = execute_sql(_sql,args,fetch=True)
    return _rt_list


