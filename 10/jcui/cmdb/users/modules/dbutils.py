#encoding:utf-8


import gconfig

import MySQLdb


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
        # _cnt = self.excute(sql,args)
        # _rt_list = self.__cur.fetchall()
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



def excute_fetch_sql(sql,args=()):
    return excute_sql(sql,args)

def excute_commit_sql(sql,args=()):
    return excute_sql(sql, args,fetch=False)

def excute_update_sql(sql,args=()):
    return excute_sql(sql, args, fetch=False)

def excute_delete_sql(sql,args=()):
    return excute_sql(sql, args, fetch=False)

def excute_select_log(sql,args=()):
    return excute_sql(sql, args)

def excute_sql(sql,args=(),fetch=True):
    conn = None
    curs = None
    sql_count = 0
    rt_list = []
    try:
        conn = MySQLdb.connect(host=gconfig.mysql_host, user=gconfig.mysql_user, passwd=gconfig.mysql_passwd,
                               db=gconfig.mysql_db, charset=gconfig.mysql_charset)
        curs = conn.cursor()
        sql_count = curs.execute(sql, args)
        if fetch:
            rt_list = curs.fetchall()
        else:
            conn.commit()
    except BaseException as e:
        print e
    finally:
        if curs:
            curs.close()
        if conn:
            conn.close()
    return sql_count, rt_list

def excute_nginx_log_write(sql,loglist):
    conn = None
    curs = None
    sql_count = 0
    try:
        conn = MySQLdb.connect(host=gconfig.mysql_host, user=gconfig.mysql_user, passwd=gconfig.mysql_passwd,
                               db=gconfig.mysql_db, charset=gconfig.mysql_charset)
        curs = conn.cursor()
        for i in range(0, len(loglist)):
            args = (loglist[i][0][0], loglist[i][0][1], loglist[i][0][2],loglist[i][1])
            sql_count += curs.execute(sql, args)
        if sql_count:
            conn.commit()
    except BaseException as e:
        print e
        return False
    finally:
        if curs:
            curs.close()
        if conn:
            conn.close()
    return sql_count

if __name__ == '__main__':
    dbconn = MySQLConnection(host=gconfig.mysql_host,port=gconfig.mysql_port, user=gconfig.mysql_user, passwd=gconfig.mysql_passwd,
                               db=gconfig.mysql_db, charset=gconfig.mysql_charset)
    dbconn.close()
