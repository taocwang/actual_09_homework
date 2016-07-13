#encoding:utf-8
import gconfig,MySQLdb

def execute_sql(sql,args=(),fetch=True):
    _conn=None
    _cur=None
    _count=0
    _rt_list=[]
    try:
        _conn=MySQLdb.connect(host=gconfig.MYSQL_HOST,port=gconfig.MYSQL_PORT,\
                              user=gconfig.MYSQL_USER,passwd=gconfig.MYSQL_PASSWD,\
                              db=gconfig.MYSQL_DB,charset=gconfig.MYSQL_CHARSET)
        _cur=_conn.cursor()
        _count=_cur.execute(sql,args)
        if fetch:
            _rt_list=_cur.fetchall()
        else:
            _conn.commit()
    except BaseException as e:
        print e
    finally:
        if _cur:
            _cur.close()
        if _conn:
            _conn.close()
    return _count,_rt_list


# def execute_fetch_sql(sql,args=()):
#     _conn=None
#     _cur=None
#     _count=0
#     _rt_list=[]
#     try:
#         _conn=MySQLdb.connect(host=gconfig.MYSQL_HOST,port=gconfig.MYSQL_PORT,\
#                               user=gconfig.MYSQL_USER,passwd=gconfig.MYSQL_PASSWD,\
#                               db=gconfig.MYSQL_DB,charset=gconfig.MYSQL_CHARSET)
#         _cur=_conn.cursor()
#         _count=_cur.execute(sql,args)
#         _rt_list=_cur.fetchall()
#         print _count
#     except BaseException as e:
#         print e
#     finally:
#         if _cur:
#             _cur.close()
#         if _conn:
#             _conn.close()
#     return _count,_rt_list
#
# def execute_commit_sql(sql,args=()):
#     _conn=None
#     _cur=None
#     _count=0
#     try:
#         _conn=MySQLdb.connect(host=gconfig.MYSQL_HOST,port=gconfig.MYSQL_PORT,\
#                               user=gconfig.MYSQL_USER,passwd=gconfig.MYSQL_PASSWD,\
#                               db=gconfig.MYSQL_DB,charset=gconfig.MYSQL_CHARSET)
#         _cur=_conn.cursor()
#         _count=_cur.execute(sql,args)
#         _conn.commit()
#     except BaseException as e:
#         print e
#     finally:
#         if _cur:
#             _cur.close()
#         if _conn:
#             _conn.close()
#     return _count
#
