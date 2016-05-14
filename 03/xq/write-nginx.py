#!/usr/bin/env python
# coding=utf-8

port = 9999
server = 'default'
servername = 'cmdb'
access_log = '/var/log/cmdb.log'
proxy_port = 8888
root ='/var/www/script/'

with open('nginx.tpl') as f:
    nginx_conf=f.read().format(port=port,server=server,servername=servername,access_log=access_log,proxy_port=proxy_port,home=root)

with open('cmdb.conf','w') as f1:
    f1.write(nginx_conf)
