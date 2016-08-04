#!/bin/env python
#coding:utf-8
import MySQLdb
import uconf

class MYSQLConnection(object):
    def __init__(self,host,username,passwd,db,port=3306,charset='utf8'):
        self.__host=host
        self.__username=username
        self.__port=port
        self.__password=passwd
        self.__db=db
        self.__char=charset
        self.__conn=None
        self.__cursor=None
        self.__connect()

    def __connect(self):
        try:
            self.__conn=MySQLdb.connect(host=self.__host,port=self.__port,\
                        user=self.__username,passwd=self.__password,\
                        db=self.__db,charset=self.__char)
            self.__cursor=self.__conn.cursor()
        except BaseException as e:
            #import traceback
            #print traceback.format_exc()   这两行是调试错误的好东西
            print e

    def close(self):
        self.commit()
        if self.__cursor:
            self.__cursor.close()
            self.__cursor=None

        if self.__conn:
            self.__conn.close()
            self.__conn=None

    def commit(self):
        if self.__conn:
            self.__conn.commit()

    def excute(self,sql,args):
        if self.__cursor:
            cnt=self.__cursor.execute(sql,args)
            return cnt

    def fetch(self,sql,args):
        if self.__cursor:
            cnt=self.excute(sql,args)
            rt_list=self.__cursor.fetchall()
            return cnt,rt_list

    @classmethod
    def excute_sql(cls,sql,args=(),fetch=True):
        _cnt=0
        _rt_list=[]
        _conn=MYSQLConnection(host=uconf.db_host,username=uconf.db_user,passwd=uconf.db_passwd,charset=uconf.db_charset,db=uconf.db_db)
        if fetch:
            _cnt,_rt_list=_conn.fetch(sql,args)
        else:
            _cnt=_conn.excute(sql,args)
        _conn.close()
        return _cnt,_rt_list

if __name__ == "__main__":
    _args=('zy22','123123')
    _sql="select username,password from user where username=%s and password=md5(%s);"
    print MYSQLConnection.excute_sql(_sql,_args)