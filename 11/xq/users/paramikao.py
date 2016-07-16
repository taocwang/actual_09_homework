#!/usr/bin/env python
# coding=utf-8

import paramiko

myhost_list = [
'172.20.150.74']

def Myssh(hostname,port,user,password,cmd):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(hostname,port,user, password)
    stdin, stdout, stderr = ssh.exec_command(cmd)
    for line in stdout.readlines():
        print line,
    ssh.close()
L=len(myhost_list)
while L:
    for  ip in myhost_list:
        print '-' *40 + ip +'-' *40
        Myssh(ip,21860,'root','1meWsgvYeSjMA0pecBMg','ls -al /home/dev/BuildTags')
        L-=1
