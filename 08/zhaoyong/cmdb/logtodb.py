#encoding: utf-8

import dbutils

def logtodb(logfile):
    fhandler = open(logfile,'r')
    rt_dict = {}
    _sql = 'insert into accesslog(count, ip, url, code) values (%s, %s, %s, %s)'
    while True:
        line = fhandler.readline()
        if line == '':
            break
        nodes = line.split()
        ip , url ,code = nodes[0],nodes[6],nodes[8]
        key = (ip,url,code)
        if key not in rt_dict:
            rt_dict[key] = 1
        else:
            rt_dict[key] += 1
        #rt_list.append((nodes[6],nodes[0],nodes[8]))

    fhandler.close()
    # 排序
    rt_list = rt_dict.items()
    # [(key,value),(key,value)]

    for j in range(0, 10):
        for i in range(0, len(rt_list) - 1):
            if rt_list[i][1] > rt_list[i + 1][1]:
                temp = rt_list[i]
                rt_list[i] = rt_list[i + 1]
                rt_list[i + 1] = temp

    db_list = []
    for node in rt_list[-1:-11:-1]:
        db_list.append((node[1],node[0][0],node[0][1],node[0][2]))
        print db_list
        dbutils.bulker_commit_sql(_sql, db_list)

if __name__ == '__main__':
    logfile = '../../05/www_access_20140823.log'
    logtodb(logfile)
