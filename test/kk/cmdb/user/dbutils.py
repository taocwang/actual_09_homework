#encoding: utf-8

import MySQLdb

import gconf


def execute_fetch_sql(sql, args=(), fetch=True):
    return execute_sql(sql, args, fetch)

def execute_commit_sql(sql, args=(), fetch=False):
    return execute_sql(sql, args, fetch)


def execute_sql(sql, args=(), fetch=True):
    _conn = None
    _count = 0
    _rt_list = []
    try:
        _conn = MySQLConnect(host=gconf.MYSQL_HOST, port=gconf.MYSQL_PORT, \
                        user=gconf.MYSQL_USER, password=gconf.MYSQL_PASSWD, \
                        db=gconf.MYSQL_DB)

        _count = _conn.execute(sql, args)
        if fetch:
            _count, _rt_list = _conn.fetchall(sql, args)
        else:
            _count = _conn.execute(sql, args)
    except BaseException as e:
        print e
    finally:
        if _conn:
            _conn.close()

    return _count, _rt_list


def bulker_commit_sql(sql, args_list=[]):
    _conn = None
    _count = 0
    _rt_list = []
    try:
        _conn = MySQLConnect(host=gconf.MYSQL_HOST, port=gconf.MYSQL_PORT, \
                        user=gconf.MYSQL_USER, password=gconf.MYSQL_PASSWD, \
                        db=gconf.MYSQL_DB)
        for _args in args_list:
            _count += _count.execute(sql, _args)
    except BaseException as e:
        print e
    finally:
        if _conn:
            _conn.close()

    return _count, _rt_list


class MySQLConnect(object):

    def __init__(self, host, port, user, password, db):
        self.__host = host
        self.__port = port
        self.__user = user
        self.__password = password
        self.__db = db
        self.__connect()

    def __connect(self):
        self.__conn = MySQLdb.connect(host=self.__host, port=self.__port, \
                                    user=self.__user, passwd=self.__password, \
                                    db=self.__db, charset='utf8')
        self.__cursor = _conn.cursor()

    def execute(self, sql, args):
        _count = 0
        try:
            _count = self.__cursor.execute(sql, args)
        except BaseException as e:
            print e
        return _count

    def fetchall(self, sql, args):
        _count = self.execute(sql, args)
        _rt_list = self.__cursor.fetchall()
        return _count, _rt_list

    def close(self):
        self.__conn.commit()
        if self.__cursor:
            self.__cursor.close()
            self.__cursor = None

        if self.__conn:
            self.__conn.close()
