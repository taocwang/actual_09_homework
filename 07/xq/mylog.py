#!/usr/bin/env python
# coding=utf-8
from dbutils import execute_sql
#定义函数获取排名前N的日志
def get_sum(path):
    k={}
    l=[]
    n=[]
#打开日志文件并把对应字段加入列表
    with open(path) as f:
        for line in f:
            l.append((line.split()[0] + " " + line.split()[6] + " " + line.split()[8]))
#统计列表中元素个数，并排序
    for i in l:
        k[i]=k.setdefault(i,0)+1
    kk=sorted(k.items(),key=lambda x: -x[1])
    count= len(kk)

#将数据元素构造成字典，并加入列表[{},{}]
    for j in range(count):
        d={}
        d['ip'] = kk[j][0].split()[0]
        d['url'] = kk[j][0].split()[1]
        d['code'] = kk[j][0].split()[2]
        d['cnt'] = kk[j][1]
        n.append(d)
    return n
if __name__ ==  '__main__':
    n=get_sum('www_access_20140823.log')
    for i in n:
        _sql = 'insert into logs(ip, url, code,cnt) values(%s, %s, %s,%s);'
        _args = (i['ip'],i['url'],i['code'],int(i['cnt']))
        execute_sql(_sql, _args,fetch=False)
