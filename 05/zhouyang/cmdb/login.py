#coding:utf-8
import json
import uconf

def get_users(file):
    with open(file,'r') as user_info:
        try:
            return json.loads(user_info.read())
        except:
            return []

def check_user(username,password):
    users=get_users(uconf.user_conf)
    for user in users:
        if user.get('username') == username and user.get('password')==password:
            return True
        else:
            return False

