#encoding:utf-8
import uservalid
import gconfig
import json
def userdel(username):
    user_list_e = uservalid.get_user()
    print user_list_e
    for user in user_list_e:
      for i in user.items():
          if username in i:
              dic_index = user_list_e.index(user)
              user_list_e.pop(dic_index)
              user_list_f = open(gconfig.USER_FILE,'w')
              data = json.dumps(user_list_e)
              user_list_f.write(data)
              user_list_f.close()
              return True
    return False
