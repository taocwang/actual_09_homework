#encoding:utf-8
import dbutils

def log2db(logfile):

    fhandler = open(logfile, 'r')

    rt_list = []
    # 统计
    _sql = 'insert into accesslog(url, ip, code) values (%s, %s, %s)'
    while True:
        line = fhandler.readline()
        if line == '':
            break

        nodes = line.split()
        rt_list.append((nodes[0], nodes[6], nodes[8]))
        

    fhandler.close()

    dbutils.bulker_commit_sql(_sql, rt_list)


if __name__ == '__main__':
    logfile = '/home/share/www_access_20140823.log'

    log2db(logfile)
