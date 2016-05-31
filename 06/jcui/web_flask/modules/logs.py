#encoding:utf-8
''
from dbutils import excute_nginx_log_write,excute_select_log

'''
对日志进行处理,返回ip,url,code,nums
'''
def log_anslysis(sfile):
    file_dict = {}
    try:
        files = open(sfile, 'r')
        for i in files:
            i = i.split()
            x, y, z = i[0], i[6], i[8]
            file_dict[(x, y, z)] = file_dict.get((x, y, z), 0) + 1
    except BaseException as e:
        print e
        return ''
    finally:
        if files:
            files.close()
    return sorted(file_dict.items(),key=lambda x:x[1],reverse=False)

'''
将日志插入到sql中
'''
def logs_import_sql():
    logs_path = '/home/op/test/www_access_20140823.log'
    log_list = log_anslysis(logs_path)
    _sql = 'insert into access_logs(ip,url,code,nums) values(%s,%s,%s,%s)'
    if excute_nginx_log_write(_sql,log_list):
        return True
    return False

'''
前台调用日志查询展示
'''
def log_access(top=10):
    colloens = ('id', 'ip', 'url', 'code', 'nums')
    _sql = 'select * from access_logs order by nums desc limit %s'
    args = (top,)
    rt = []
    _sql_count, rt_list = excute_select_log(_sql, args)
    for x in rt_list:
        rt.append(dict(zip(colloens,x)))
    return rt








if __name__ == '__main__':
    print logs_import_sql()