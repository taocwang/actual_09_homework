#!/usr/bin/env python
#-*- coding: UTF=8 -*-

rh = open('nginx.rdp','r')
rf = rh.read()
rh.close()

wh = open('cmdb.conf','w')
wf = wh.write(rf.format (port=8080,server='',servername='hjun.in',access_log='hjun.in.log',home='/opt/webapps/cmdb',proxy_port='8080'))
wh.close()

rh = open('cmdb.conf','r')
for i in rh:
	print i
rh.close()
