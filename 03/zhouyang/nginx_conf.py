#!/bin/env python
#coding:utf8

file ='nginx.conf_default'
handler=open(file,'r')
content=handler.read()
handler.close()

content=content.format(server_port=8060,server_name='www.qqq.com',root_path='/usr/local/nginx/htdocs')

new_file='nginx.conf'
handle=open(new_file,'w')
handle.write(content)
handle.close()
