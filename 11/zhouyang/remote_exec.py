#!/bin/env python
#-*- coding: utf-8 -*-
import paramiko
import sys
import os
import argparse
import logging

def __help__():
    print """
Desp:Excute a remote command or push/pull a file to/from remote server.
version: 1.0.3
Editer:yaungzhou
Usage: ./remote_exec.py ip username password -c|-f|-fc|-g cmd|file
    -c    excut remote command
    -f    upload local file to remote server path /data/tms2/tmp3
    -fc   upload local file to remote server then exucte it
    -g    get file from remote server and save to local path /data/tms2/tmp3/

"""
#ver1.0 完成基本的远程命令执行和本地script文件push并在远程执行的功能
#ver1.0.1 合并exe_remote_script方法中的chmod和执行脚本文件到一行,节省代码
#ver1.0.2 修改exec_remote_file方法为单纯的uploadfile方法;实现文件上传,远程命令执行的常用ijobs功能.
#ver1.0.3 增加新功能:从remote svr上下载文件到本地/data/tms2/tmp3/ ;完善帮助功能,解释所有功能参数
#ver1.0.4 增加log功能,修正help

class remote_exec(object):
    def __init__(self,ip,port,username,passwd,cmd):
        self.username=username
        self.passwd=passwd
        self.cmd=cmd
        self.ip=ip
        self.port=port

    def ssh2(self):
        try:
            ssh = paramiko.SSHClient()
            ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            ssh.connect(self.ip,self.port,self.username,self.passwd,timeout=5)
            stdin,stdout,stderr = ssh.exec_command(self.cmd)
            out = stdout.readlines()
            for o in out:
                 print o,
            print 'Excute command %s on %s success'%(self.cmd,self.ip)
            ssh.close()
        except Exception:
            print 'Excute command %s on %s failed'%(self.cmd,self.ip)
            sys.exit()

    def uploadfile(self):
        try:
            t = paramiko.Transport((self.ip,self.port))
            t.connect(username=self.username,password=self.passwd)
            sftp = paramiko.SFTPClient.from_transport(t)
            file = self.cmd
            file_name=os.path.basename(file)
            print 'Uploading file %s ...' % file
            sftp.put(file,'/data/tms2/tmp3/%s' % file_name)
            print 'Upload file success'
            t.close()
        except Exception:
            print 'Error:Upload file %s failed' % file
            sys.exit()

    def downloadfile(self):
        try:
            t = paramiko.Transport((self.ip,self.port))
            t.connect(username=self.username,password=self.passwd)
            sftp = paramiko.SFTPClient.from_transport(t)
            file = self.cmd
            file_name = os.path.basename(file)
            print "Download file %s" % file
            sftp.get(file,'/data/tms2/tmp3/%s' % file_name)
            print "Download file %s success" % file
            t.close()
        except Exception:
            print "Error:Download file %s failed" % file
            sys.exit()

if __name__ == "__main__":
    _argparse=argparse.ArgumentParser()
    _argparse.add_argument('-H','--host',help="host name or IP",default='localhost')
    _argparse.add_argument('-P','--port',help="ssh port",type=int)
    _argparse.add_argument('-u','--user',help="username for ssh")
    _argparse.add_argument('-p','--passwd',help="password of username")
    _argparse.add_argument('-C','--cmds',nargs='+',type=str,help="要执行的命令，多个命令之间用|分割",default=[])
    _argparse.add_argument('-U','--upload',nargs='+',type=str,help="要上传的文件,多个文件用|分割",default=[])
    _argparse.add_argument('-D','--download',nargs='+',type=str,help="要下载的文件,多个文件用|分割",default=[])
    _args=_argparse.parse_args()
    ip=_args.host
    port=_args.port
    username=_args.user
    passwd=_args.passwd
    cmds=_args.cmds
    upload_files=_args.upload
    down_files=_args.download



    if cmds:
        p=remote_exec(ip,port,username,passwd,cmds)
        p.ssh2()
    if upload_files:
        p=remote_exec(ip,port,username,passwd,upload_files)
        p.uploadfile()
    if down_files:
        p=remote_exec(ip,port,username,passwd,down_files)
        p.downloadfile()
else:
        __help__()