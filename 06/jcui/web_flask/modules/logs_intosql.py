#encoding:utf-8


from receive_logs import log_anslysis
from dbutils import excute_nginx_log_write

#插入sql
def logs_import_sql():
    logs_path = '/home/op/test/www_access_20140823.log'
    log_list = log_anslysis(logs_path)
    _sql = 'insert into access_logs(ip,url,code,nums) values(%s,%s,%s,%s)'
    if excute_nginx_log_write(_sql,log_list):
        return True
    return False

if __name__ == '__main__':
    print logs_import_sql()