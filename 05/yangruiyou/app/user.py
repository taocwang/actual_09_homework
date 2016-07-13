# coding:utf-8
import json
import gconf


def get_users():
    try:
        handler = open(gconf.USER_FILE, 'rb')
        cxt = handler.read()
        handler.close()
        return json.loads(cxt)
    except BaseException as e:
        print e
        return []


# print get_users()

def validate_login(username, password):
    users = get_users()
    # print users
    for user in users:
        if user.get('username') == username and user.get('password') == password:
            return True
    return False


#print validate_login('kk', '123456')


def check_username(username):
    users = get_users()
    for user in users:
        if user.get('username') == username:
            return True

    return False


#print check_username('you')


def new_users(username, password, age):
    if check_username(username):
        return False
    else:
        if username != '' and password != '' and age != '':
            users = get_users()
            users.append({'username': username, 'password': password, 'age': age})
            cxt = json.dumps(users)
            # print cxt

            handler = open(gconf.USER_FILE, 'w')
            handler.write(cxt)
            # handler.close
            return True
        else:
            return False


#print new_users('you', 'you', 30)


def delete_username(username):
    if check_username(username):
        users = get_users()
        for index in range(0, len(users)):
            if users[index].get('username') == username:
                del (users[i])
                cxt = json.dumps(users)
                handler = open(gconf.USER_FILE, 'w+')
                handler.write(cxt)
                handler.close()

    return True
