#encoding:utf-8

import paramiko
import getpass

def ssh_excute(host,username,password,cmd=[],port=22):
    _rt_list = []
    #创建连接对象
    ssh = paramiko.SSHClient()
    #设置客户端登陆验证方式
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    #设置连接服务器信息
    ssh.connect(host, 22, username,password)

    for _cmd in cmd:
        # 操作
        stdin, stdout, stderr = ssh.exec_command(_cmd)
        #获取反馈信息
        _rt_list.append([_cmd,stdout.readlines(),stderr.readlines()])
    #关闭
    ssh.close()
    # 返回结果
    return _rt_list

def sftp_excute(host,username,password,sfile,dfile,port=22):

    t = paramiko.Transport((host, port))

    t.connect(username=username, password=password)

    sftp = paramiko.SFTPClient.from_transport(t)

    remotepath = dfile

    localpath = sfile

    sftp.put(localpath, remotepath)

    t.close()

if __name__ == '__main__':
    host = '182.61.42.4'
    port = 22
    user = 'root'
    password = '1qaz@WSX'
    sfile = '/home/jcui/files/aa.py'
    dfile = '/tmp/jcui.py'
    sftp_excute(host, user, password, sfile, dfile)
    print ssh_excute(host,user,password,cmd=['rm -rf /tmp/aa.py','nohup python /tmp/jcui.py >/tmp/jcui.log 2>&1 &','cat /tmp/jcui.log'])
