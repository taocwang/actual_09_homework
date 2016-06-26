#encoding:utf-8
from dbutils import execute_fetch_sql

def get_topn(topn=10):
    _sql = "select ip,url,code,cnt from log order by cnt desc limit %s"
    _count, _rt_list = execute_fetch_sql(_sql,(topn,))
    return _rt_list