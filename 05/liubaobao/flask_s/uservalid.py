#encoding:utf-8
import json
import gconfig

def get_user():
    try:
        user_file=open(gconfig.USER_FILE,'rb')
        user_info=user_file.read()
        user_file.close()
        user_ext = json.loads(user_info)
        return user_ext
    except:
        return []

def uservalid(username,password):
    user_list=get_user()
    print user_list
    for user in user_list:
        print user
        if username == user.get('username') and password == user.get('password'):
            print username,password
            return True
    return False
uservalid('lbb','123')
