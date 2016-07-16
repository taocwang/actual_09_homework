	#coding:utf8

import paramiko
import getpass

def ssh_command(host,port,username,password,cmd):
	ssh = paramiko.SSHClient()

	ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
	try:
		ssh.connect(host,port,username,password)
		stdin,stdout,stderr = ssh.exec_command(cmd)
		if not stderr.read():
			return stdout.read()
		else:
			return "command:%s error" %(cmd)
	except BaseException as e:
		print e
		return str(e)

	finally:
		ssh.close()




if __name__ == '__main__':
	host = '192.168.192.75'
	port = 22
	username = 'root'
	password = getpass.getpass('input you password: ')
	cmd = 'ifconfiga'
	print ssh_command(host,port,username,password,cmd)


