#encoding:utf-8


''
'''
发送邮件

import smtplib

_server_conn = smtplib.SMTP(server,port)
_server_conn.ehlo()
_server_conn.starttls()    启用ssl时需配置该选项
_server_conn.sendmail('from','to','msg')
_server_conn.close()


'''
