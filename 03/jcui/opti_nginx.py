#encoding: utf-8
#用于根据nginx的模板文件生成相应的配置文件

nginx_template = 'nginx.tmp'

files = open(nginx_template,'r')
tmp = files.read()
files.close()

new_tmp = tmp .format(port=80,server='127.0.0.1',servername='www.baidu.com',access_log='/var/log/nginx/access.log',home='/usr/local/nginx/html',proxy_port=9001)
files = open('nginx.conf','w')
files.write(new_tmp)
files.close()