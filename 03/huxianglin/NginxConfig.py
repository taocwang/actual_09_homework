#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
通过使用字符串处理中的format函数，传递参数到nginx模版中，生成nginx配置文件
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
'''
def NginxConfig(FileName,ItemDict):
    NginxConfigTemplate='''
server {{
    listen       {port} {server};
    server_name  {servername};

    access_log  {access_log}  main;

    location / {{
        root   {home};
        index  index.html index.htm;
        proxy_pass   http://127.0.0.1:{proxy_port};
    }}
}}
'''.format(port=ItemDict['port'],server=ItemDict['server'],servername=ItemDict['servername'],access_log=ItemDict['access_log'],home=ItemDict['home'],proxy_port=ItemDict['proxy_port'])
    Flag=WritFile(FileName, NginxConfigTemplate)
    if Flag:
        print 'nginx配置文件已成功保存到文件%s' %(FileName)
    else:
        print 'nginx配置文件保存失败！！！'

def WritFile(FileName,NginxConfigTemplate):
    f=open(FileName,'w')
    try:
        f.write(NginxConfigTemplate)
        f.close()
        return True
    except Exception,e:
        print 'File %s Save Failed!!!' %(FileName),e
        f.close()
        return False

if __name__ == "__main__":
    ItemDict={
             'port':9999,
             'server':'default_server',
             'servername':'_',
             'access_log':'/tmp/cmdb.access.log',
             'home':'/home/woniu/07/11/user',
             'proxy_port':9990
             }
    NginxConfig('nginx.conf',ItemDict)


'''
功能ok，继续加油
'''
