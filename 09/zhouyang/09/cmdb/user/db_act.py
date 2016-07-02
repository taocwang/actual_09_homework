#/bin/env python
#coding:utf-8
import MySQLdb
import uconf
'''
添加的有问题吧？
数据库中要求为int类型的添加有问题 因为args里面的数据都是str  这个问题咋解决

在哪运行的？
'''
def db_act(sql,args=(),fetch=True,batch=False):
    '''数据库操作。
    fetch决定是返回select结果还是执行增，删，改操作的bool结果;
    batch表示批处理，对args进行遍历for循环执行'''
    rt_list=[]
    db_conn=None
    db_cursor=None
    db_cnt=0
    try:
        db_conn=MySQLdb.connect(host=uconf.db_host,user=uconf.db_user,passwd=uconf.db_passwd,charset=uconf.db_charset,db=uconf.db_db)
        db_conn.autocommit(True)
        db_cursor=db_conn.cursor()
        if batch:
            for arg in args:
                cnt=db_cursor.execute(sql,arg)
                db_cnt += cnt
        else:
            db_cnt=db_cursor.execute(sql,args)
        rt_list=db_cursor.fetchall()
    except BaseException as e:
        print e
    finally:
        if db_cursor:
            db_cursor.close()
        if db_conn:
            db_conn.close()
    if fetch:
        return db_cnt,rt_list
    else:
        return db_cnt != 0
