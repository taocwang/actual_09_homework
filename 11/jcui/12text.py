#encoding:utf-8


''
'''
发送邮件

import smtplib

_server_conn = smtplib.SMTP(server,port)
_server_conn.ehlo()
_server_conn.starttls()    启用ssl时需配置该选项
_server_conn.sendmail('from','to','msg')
_server_conn.quit()

msg 依赖另外的包

from email.mime.text import MIMEText



psutil

sudo pip install psutil

获取服务器信息的第三方库

爬虫:

    requests
        发起url请求,获取结果
    pyquery
        解析html
    拼写url requests发起请求
    PyQuery(text)
    class 选择器
    标签选择器
    find

    找到标签后干嘛?
    1. attr attrib.get('attrname')
    2. value .value
    3. text .text


'''

import smtplib
from email.mime.text import MIMEText
import datetime
from pyquery import PyQuery as pyq
import requests


def sendmail(to_list,title,content):
    smtp_host = 'smtp.tom.com'
    smtp_port = 25
    smtp_user = 'wolfccies@tom.com'
    smtp_pass = 'wolfccies'

    _server = smtplib.SMTP(smtp_host,smtp_port)
    _server.set_debuglevel(True)
    _server.ehlo()
    _server.login(smtp_user,smtp_pass)
    _msg = MIMEText(content,'html','utf-8')
    _msg['Subject'] = title
    _msg['To'] = ';'.join(to_list)
    _msg['From'] = '51Reboot告警管理员<%s>' % smtp_user
    _msg['Date'] = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    _server.sendmail(smtp_user,to_list,_msg.as_string())
    _server.quit()


def re_url(ip):
    _response = requests.get('http://ip.chinaz.com/ip=%s' % ip)
    _response.encoding = 'utf-8'
    return _response

def get_area(ip):
    jq = pyq(re_url(ip).text)
    rt = jq('.IcpMain02').find('.bor-b1s') .find('span')[-1].text
    print rt

def re_url2(ip):
    _response = requests.get('http://ip138.com/ips138.asp?ip=%s' % ip)
    _response.encoding = 'gbk'
    return _response

def get_area2(ip):
    jq = pyq(re_url2(ip).text)
    rt = jq('.ul1').find('li')[0].text
    print rt
    print type(rt)


if __name__ == '__main__':
    # sendmail(['cui6522123@163.com'],'告警邮件','cpu内存告警测试邮件')
    ip = '221.179.216.54'
    # get_area(ip)
    get_area2(ip)



'''
作业:
1.查看flask中获取参数值
2.根据accesslog,统计code分布图
3.画服务器cpu,内存使用率的仪表盘
4.机房的增删改查
5.爬虫抓取

'''