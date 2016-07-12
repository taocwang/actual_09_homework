#coding:utf-8
import paramiko
ssh = paramiko.SSHClient()

ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

ssh.connect("192.168.0.101",22,"root", "321100")

stdin, stdout, stderr = ssh.exec_command("pwd")

print stdout.readlines()

ssh.close()