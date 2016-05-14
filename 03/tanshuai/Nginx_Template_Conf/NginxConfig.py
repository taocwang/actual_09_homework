#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 定义模版变量
port = 80
server = 'www.xing008.com'
root_path = '/opt/projects/site/xmpdf'
log_path = '/opt/logs/nginx/xmpdf/www_system'

# 打开Nginx配置模版
open_file = open('nginx.tpl')
nginx_conf = open_file.read().format(port=port, server=server, root_path=root_path, log_path=log_path)
open_file.close()

# 写入Nginx配置文件
create_nginx_conf = open('nginx.conf', 'w+')
create_nginx_conf.write(nginx_conf)
create_nginx_conf.close()


