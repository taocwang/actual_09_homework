#encoding:utf-8
import os,sys,json,gconfig,dbutils
json_path = gconfig.file_path +"\user.json"
def get_users():
    _columns=("id","username","password","age")
    _sql='select * from user'
    _count,_rt_list = dbutils.execute_sql(_sql)
    rt =[]
    for _line in _rt_list:
         rt.append(dict(zip(_columns,_line)))
    return  rt
    # _sql='select * from user'
    # _conn=None
    # _cur=None
    # _count=0
    # _rt=[]
    # try:
    #     _conn=MySQLdb.connect(host=gconfig.MYSQL_HOST,port=gconfig.MYSQL_PORT,\
    #                           user=gconfig.MYSQL_USER,passwd=gconfig.MYSQL_PASSWD,\
    #                           db=gconfig.MYSQL_DB,charset=gconfig.MYSQL_CHARSET)
    #     _cur=_conn.cursor()
    #     _count=_cur.execute(_sql)
    #     _rt_list=_cur.fetchall()
    #     for _line in _rt_list:
    #         _rt.append(dict(zip(_columns,_line)))
    # except BaseException as e:
    #     print e
    # finally:
    #     if _cur:
    #         _cur.close()
    #     if _conn:
    #         _conn.close()
    # return _rt
#     try:
#         # print json_path
#         fhandler = open(json_path,"rb")
#         cxt = fhandler.read()
#         fhandler.close()
#         return json.loads(cxt)
#     except BaseException as e:
#         print e
#         return[]
def get_user(uid):
    _users = get_users()
    for _user in _users:
        if _user.get("id")== uid:
            return _user
    return None


def update_user(uid,username,password,age):
    sql="update user SET username=%s,password=%s,age=%s where id = %s"
    args=(username,password,age,uid)
    fetch =False
    dbutils.execute_sql(sql,args,fetch)
    # print username,password,age
    # users= get_users()
    # _idx = -1
    # for _user in users:
    #     _idx=_idx+1
    #     print _user
    #     if _user.get("username")== username:
    #         users[_idx].update({'password' : password, 'age' : age})
    #         save_user(users)

# def save_user(user):
#     fhandler = open(json_path,"wb")
#     fhandler.write(json.dumps(user))
#     fhandler.close
    
def add_user(username,password,age):
    sql='insert into user(username,password,age) values(%s,md5(%s),%s)'
    args=(username,password,age)
    fetch =False
    dbutils.execute_sql(sql,args,fetch)
    # _users = get_users()
    # _users.append({"username":username,"password":password,"age":age})
    # save_user(_users)
    # return "sucess add {}".format(username)

def delete_user(uid):
    sql='delete from user where id=%s'
    args=uid
    fetch =False
    dbutils.execute_sql(sql,args,fetch)
    # _users = get_users()
    # _idx =-1
    # for _user in _users:
    #     _idx=_idx + 1
    #     if _user.get("username")==username:
    #         del _users[_idx]
    #         save_user(_users)
    #         break
    
def validate_login(username,password):
    _sql='select * from user where username =%s and password=md5(%s)'
    _count,_rt_list = dbutils.execute_sql(_sql,(username,password))
    return _count !=0
    # _conn=None
    # _cur=None
    # _count=0
    # try:
    #     print _sql
    #     _conn=MySQLdb.connect(host=gconfig.MYSQL_HOST,port=gconfig.MYSQL_PORT,\
    #                           user=gconfig.MYSQL_USER,passwd=gconfig.MYSQL_PASSWD,\
    #                           db=gconfig.MYSQL_DB,charset=gconfig.MYSQL_CHARSET)
    #     _cur=_conn.cursor()
    #     print _cur
    #     _count=_cur.execute(_sql,(username,password))
    # except BaseException as e:
    #     print e
    # finally:
    #     if _cur:
    #         _cur.close()
    #     if _conn:
    #         _conn.close()
    # return _count !=0
    # _users=get_users()
    # for user in _users:
    #     # print type(user)
    #     if user.get("username")== username and \
    #     user.get("password")== password:
    #         return True
    # return False

def validate_add_user(username,password,age):
    if username.strip()=="":
        return False,"username is empty"
    _users = get_users()
    for user in _users:
        if user.get("username")==username:
            # print username
            return False,"username already exists"
    if len(password) < 6:
        # print password
        return False,"password too short"
    if not str(age).isdigit() or int(age)<0 or int(age)>100:
        # print age
        return False,"age is incorrect"
    return True,"sucess validate"

def validate_update_user(uid,username,password,age):
    if get_user(int(uid)) is None:
        return False,"username does not exist"
    if len(password) < 6:
        return False,"password too short"
    if not str(age).isdigit() or int(age)<0 or int(age)>100:
        return False,"age is incorrect"
    return True,""

# else:
    # handler1 = open(json_path,"ab")        
    # nuser ={"username":username,"password":password,"age":age}
    # my_list=json.loads(handler1.read()).append(nuser)                
    # handler1.close()
    # return False

# def check_username(username):
#     users = get_users()
#     for info in users:
#         if info.get("username")== username:
#             return True
#     return False


def logs_from_db(topn):
    sql='SELECT ip,url,code,cnt FROM nginx_log ORDER BY cnt DESC limit %s'
    args=topn
    _count,_rt_list = dbutils.execute_sql(sql,args)
    return _rt_list

def validate_topn(topn):
    if not topn:
    # if topn is None:
        return False,"请输入TOPN"
    if not str(topn).isdigit():
        return False,"请输入数字"
    return True,""

if __name__ == "__main__":
    # is_ok,error = validate_add_user("abc","kkkkkk",299)
    # print is_ok,error
    # info = add_user("ada","111",26)
    # print info
    # xy=get_user("kk")
    # print xy
    # update_user("kk","123",22)
    x=logs_from_db(2)
    print x
