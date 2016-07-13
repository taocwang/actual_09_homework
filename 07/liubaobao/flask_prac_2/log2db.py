#!encoding:utf-8


import dbutils


def log2db(logfile):
    fhandler = open(logfile,'r')
    rt_dict ={}

    Flag =True

    while Flag:
        line = fhandler.readline()
        if line == '':
            break
        nodes = line.split()
        ip, url, code = nodes[0], nodes[6], nodes[8]
        key =(ip,url,code)
        if key not in rt_dict:
            rt_dict[key]=1
        else:
            rt_dict[key] += 1
    fhandler.close()
    rt_list = []
    count = 0
    for _key,_cnt in rt_dict.items():
        count += 1
        rt_list.append(_key + (_cnt,))
        if count == 100:
            break
    _sql = 'insert into log(ip,url,code,count) values(%s,%s,%s,%s)'
    dbutils.bulker_commit_sql(_sql,rt_list)


