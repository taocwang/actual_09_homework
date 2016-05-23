#coding:utf-8
import uconf
import json
def adduser(username,password,age):
    with open(uconf.user_conf,'r') as userinfo:
        users = json.loads(userinfo.read())
        newuser={'username':username,'password':password,'age':age}
        for user in users:
            if user.get('name') == username:
                return False
        users.append(newuser)
        newusers=json.dumps(users)
        with open(uconf.user_conf,'r+') as userinfo:
            userinfo.write(newusers)
            return True

if __name__ == '__main__':
    adduser('test','test_p',17)