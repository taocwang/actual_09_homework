#encoding:utf-8
import dbutils

def log2db(logfile):
    dbutils.execute_commit_sql('DELETE FROM accesslog;')
    fhandler = open(logfile, 'r')

    rt_dict = {}
    # 统计

    while True:
        line = fhandler.readline()
        if line == '':
            break

        nodes = line.split()
        ip, url, code = nodes[0], nodes[6], nodes[8]
        key = (ip, url, code)
        if key not in rt_dict:
            rt_dict[key] = 1
        else:
            rt_dict[key] = rt_dict[key] + 1
    fhandler.close()
    rt_list = []

    for _key, _cnt in rt_dict.items():
        rt_list.append(_key + (_cnt, ))

    _sql = 'insert into accesslog(ip, url, code, cnt) values (%s, %s, %s, %s)'
    dbutils.bulker_commit_sql(_sql, rt_list)


if __name__ == '__main__':
    logfile = '/Users/yang/Downloads/www_access_20140823.log'
    log2db(logfile)
