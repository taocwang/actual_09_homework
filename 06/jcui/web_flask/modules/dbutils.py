#encoding:utf-8


from gconfig import gconfig
import MySQLdb


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
            args = (loglist[i][1], loglist[i][0][0], loglist[i][0][1], loglist[i][0][2])
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