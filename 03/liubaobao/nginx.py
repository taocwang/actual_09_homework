#!/usr/bin/env python
#coding:utf-8
port = 8555
server = 'default'
servername = 'cmdb'
access_log = '/var/log/cmdb.log'
home = '/home/lbb/www'

tpl = open('nginx.tp','r')
nginx = tpl.read().format(port='8888',server='default',servername='cmdb',access_log='/var/log/cmdb.log',home='/workspace/web/01',proxy_port=9999)
tpl.close()

handler = open('cmdb.conf','w')
handler.write(nginx)
handler.close()