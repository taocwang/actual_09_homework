#coding:utf-8
import paramiko
import getpass

def ssh_execute(hostname,username,password,cmds=[],port=22):
    rt_list=[]

    #创建远程ssh对象
    ssh=paramiko.SSHClient()
    #设定ssh连接方式
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    #连接服务器
    ssh.connect(hostname,port,username,password)

    for cmd in cmds:
        stdin,stdout,stderr=ssh.exec_command(cmd)
        rt_list.append([cmd,stdout,stderr])

    ssh.close()

    return rt_list

def upload(hostname,username,password,files=[],port=22):
    t=paramiko.Transport((hostname,port))
    t.connect(username,password)
    sftp=paramiko.SFTPClient.from_transport(t)
    for _local,_remote in files:
        sftp.put(_local,_remote)
    t.close()


if __name__=="__main__":
    host='192.168.0.101'
    username='root'
    files=['log.txt','/tmp/zz']
    #password=getpass.getpass('请输入密码:')
    password='321100'
    '''for cmd,stdout,stderr in ssh_execute(hostname=host,username=username,password=password,cmds=['pwd','id']):
        print cmd,stdout,stderr'''

    upload(hostname=host,username=username,password=password,files=files,port=22)

