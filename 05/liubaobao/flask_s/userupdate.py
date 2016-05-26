#encoding:utf-8
import uservalid
import gconfig
import json

def userupdate(username,password):
    user_list_v = uservalid.get_user()
    print user_list_v
    for user in user_list_v:
        if username in user.get('username'):
            user['password'] = password
            user_list_h = open(gconfig.USER_FILE,'w')
            data = json.dumps(user_list_v)
            user_list_h.write(data)
            user_list_h.close()
            return True
    return False

