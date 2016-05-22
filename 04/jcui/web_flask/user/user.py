#encoding: utf-8

import json

from config import config

def get_user():
    try:
        handler = open(config.USER_FILE, 'rb')
        cxt = handler.read()
        handler.close()
        print cxt
        return json.loads(cxt)

    except BaseException as e:
        print e
        return []

def validate_login(username,password):
    users = get_user()
    for user in users:
        if user.get('username') == username and user.get('password') == password:
            return True
    return False


def user_add():
    pass


def user_del():
    pass


def user_update():
    pass