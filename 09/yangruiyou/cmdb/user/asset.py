# encoding:utf-8
from dbutils import execute_fetch_sql, execute_commit_sql


def get_list():
    _column = 'asset_id,sn,ipaddr,hostname,os,cpu,ram,disk,idc_id,admin,purchase_date,warranty_date,verdor,model,status'
    _columns = _column.split(',')
    _sql = 'select {column}  from assets where status=0 '.format(column=_column)
    _cnt, _rt_list = execute_fetch_sql(_sql)
    return [dict(zip(_columns, _line)) for _line in _rt_list]


def get_by_id(aid):
    return None


def validate_create():
    return True


def create():
    pass



def update():
    pass


def delete():
    pass


if __name__ == "__main__":
    print get_list()
