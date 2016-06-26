#coding:utf-8
'''log日志取关键内容入库。
'''
from db_act import db_act
import time

start_time=time.time()

file='www_access_20140823.log'
log_content=[]
with open(file,'r') as f:
    for line in f:
        p=line.split()
        src_ip,url_path,stat_code=p[0],p[6],p[8]
        log_content.append((src_ip,url_path,stat_code))

_sql="replace into nginx_log(src_ip,url_path,stat_code)values(%s,%s,%s);"
db_act(_sql,log_content,fetch=False,batch=True)

used_time = time.time() - start_time
print used_time