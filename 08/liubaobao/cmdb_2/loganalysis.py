#encoding:utf-8

from dbutils import execute_commit_sql,bulker_commit_sql

def loganalysis(logfile):
    execute_commit_sql('delete from accesslog;')
    fhandler = open(logfile, 'rb')
    rt = {}
    while True:
        line = fhandler.readline()
        if line == "":
            break
        nodes = line.split()
        ip,url,code = nodes[0],nodes[6],nodes[8]
        key = (ip,url,code)
        if key not in rt:
            rt[key] = 1
        else:
            rt[key] += 1
    rt_list = rt.items()
    rt_data = []
    for line in rt_list:
        lines = line[0]+(line[1],)
        rt_data.append(lines)
    _sql = "insert into accesslog(ip,url,code,cnt) VALUES (%s,%s,%s,%s)"
    bulker_commit_sql(_sql, rt_data)


if __name__ == '__main__':
    logfile = 'access.log'
    loganalysis(logfile)


