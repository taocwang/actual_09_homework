#encoding:utf-8
import hashlib

import gconfig

import MySQLdb

import smtplib
from email.mime.text import MIMEText
import datetime


class MySQLConnection(object):
    def __init__(self,host,user,passwd,db,port=3306,charset='utf8'):
        self.__host = host
        self.__port = port
        self.__user = user
        self.__passwd = passwd
        self.__db = db
        self.__charset = charset
        self.__conn = None
        self.__cur = None
        self.__connect()
    def __connect(self):
        try:
            self.__conn = MySQLdb.connect(host=self.__host,port=self.__port,user=self.__user,passwd=self.__passwd,
                                          db=self.__db,charset=self.__charset)
            self.__cur = self.__conn.cursor()
        except BaseException as e:
            print e

    def excute(self,sql,args=()):
        _cnt = 0
        if self.__cur:
            _cnt = self.__cur.execute(sql,args)
        return _cnt

    def fetch(self,sql,args=()):
        _cnt = 0
        _rt_list = []
        if self.__cur:
            _cnt = self.__cur.execute(sql,args)
            _rt_list = self.__cur.fetchall()
        return _cnt,_rt_list


    def commit(self):
        if self.__conn:
            self.__conn.commit()

    def close(self):
        self.commit()
        if self.__cur:
            self.__cur.close()
            self.__cur = None

        if self.__conn:
            self.__conn.close()
            self.__conn = None

    @classmethod
    def excute_sql(cls,sql,args=(),fetch=True):
        _cnt = 0
        _rt_list = []
        _dbconn = MySQLConnection(host=gconfig.mysql_host, port=gconfig.mysql_port, user=gconfig.mysql_user,
                                 passwd=gconfig.mysql_passwd,
                                 db=gconfig.mysql_db, charset=gconfig.mysql_charset)
        if fetch:
            _cnt,_rt_list = _dbconn.fetch(sql,args)

        else:
            _cnt = _dbconn.excute(sql,args)

        _dbconn.close()
        return _cnt,_rt_list

    @classmethod
    def excute_log_sql(cls,sql,loglist):
        sql_count = 0
        _dbconn = MySQLConnection(host=gconfig.mysql_host, port=gconfig.mysql_port, user=gconfig.mysql_user,
                                  passwd=gconfig.mysql_passwd,
                                  db=gconfig.mysql_db, charset=gconfig.mysql_charset)
        for i in range(0, len(loglist)):
            args = (loglist[i][0][0], loglist[i][0][1], loglist[i][0][2], loglist[i][1])
            sql_count += _dbconn.excute(sql, args)
        _dbconn.close()
        return sql_count


def md5_str(value):
    _md5 = hashlib.md5()
    _md5.update(value)
    return _md5.hexdigest()


def sendmail(to_list,title,content):
    _server = smtplib.SMTP(gconfig.smtp_host,gconfig.smtp_port)
    # _server.set_debuglevel(True)    #debug模式
    _server.ehlo()
    _server.login(gconfig.smtp_user,gconfig.smtp_pass)
    _msg = MIMEText(content,'html','utf-8')
    _msg['Subject'] = title
    _msg['To'] = ';'.join(to_list)
    _msg['From'] = '51Reboot告警管理员<%s>' % gconfig.smtp_user
    _msg['Date'] = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    _server.sendmail(gconfig.smtp_user,to_list,_msg.as_string())
    _server.quit()

if __name__ == '__main__':
    # dbconn = MySQLConnection(host=gconfig.mysql_host,port=gconfig.mysql_port, user=gconfig.mysql_user, passwd=gconfig.mysql_passwd,
    #                            db=gconfig.mysql_db, charset=gconfig.mysql_charset)
    # dbconn.close()
    # print md5_str('admin')

    sendmail(['cui6522123@163.com'], '告警邮件', 'cpu内存告警测试邮件')
