#!/usr/bin/env python
#_*_coding:utf-8_*_

Nginx_Tem = '''
server {{
    listen       {srv_port} {srv};
    server_name  {srv_name};

    access_log  {srv_log}  main;

    location / {{
        root   {srv_root};
        index  index.html index.htm;
        proxy_pass   http://127.0.0.1:{pro_port};
    }}
}}
'''

print Nginx_Tem.format(srv_port=9000, srv='server', srv_name='mysrv', srv_log='/var/log/nginx_access.log', srv_root='/var/www/html', pro_port=9999)

