#encoding:utf-8

from uservalid import get_user
import gconfig
import json
def useradd(username,password,telephone,mail,usertel,name,adminrole):
    user_list1=get_user()
    for user in user_list1:
        if username == user['username']:
            return False
    useradd_f=open(gconfig.USER_FILE,'rb')
    useradd_info=useradd_f.read()
    useradd_f.close()
    useradd_cxt=json.loads(useradd_info)
    useradd_cxt.append({'username':username,'password':password,'telephone':telephone,'mail':mail,'usertel':usertel,'name':name,'adminrole':adminrole})
    useradd_f=open(gconfig.USER_FILE,'w')
    useradd_f.write(json.dumps(useradd_cxt))
    useradd_f.close()
    return True


