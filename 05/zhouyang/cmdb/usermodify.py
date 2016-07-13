#coding:utf-8
import uconf
import json

def usermodify(username,password,age):
    with open(uconf.user_conf,'r') as content:
        user_list=json.loads(content.read())
        i = 0
        for userinfo in user_list:
            if userinfo['username'] == username:
                user_list[i]['age']=age
                user_list[i]['password']=password
                break
            i += 1
    with open(uconf.user_conf,'w') as newcontent:
        newcontent.write(json.dumps(user_list))
    return 1

if __name__ == '__main__':
    usermodify('kk',123,22)


