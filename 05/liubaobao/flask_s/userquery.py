#encoding:utf-8
import uservalid
import json
import gconfig


def userquery(username):
    user_list_s = uservalid.get_user()
    for user in user_list_s:
        if username in user.get('username'):
            return True
    return False


def userquery_get(username):
    user_list_x = uservalid.get_user()
    for user in user_list_x:
        if username in user.get('username'):
                user_dict_t = user
                return user_dict_t
    return []
