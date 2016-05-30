#encoding:utf-8
import os,sys,json,gconfig
json_path = gconfig.file_path +"\user.json"
def get_users():
    try:
        # print json_path
        fhandler = open(json_path,"rb")        
        cxt = fhandler.read()
        fhandler.close()
        return json.loads(cxt)
    except BaseException as e:
        print e
        return[]

def get_user(username):
    _users = get_users()
    for _user in _users:
        if _user.get("username")== username:
            return _user
    return None

def update_user(username,password,age):
    print username,password,age
    users= get_users()
    _idx = -1
    for _user in users:
        _idx=_idx+1
        print _user
        if _user.get("username")== username:
            users[_idx].update({'password' : password, 'age' : age})
            save_user(users)

def save_user(user):
    fhandler = open(json_path,"wb")
    fhandler.write(json.dumps(user))
    fhandler.close
    
def add_user(username,password,age):
    _users = get_users()
    _users.append({"username":username,"password":password,"age":age})
    save_user(_users)
    return "sucess add {}".format(username)

def delete_user(username):
    _users = get_users()
    _idx =-1
    for _user in _users:
        _idx=_idx + 1
        if _user.get("username")==username:
            del _users[_idx]
            save_user(_users)
            break
    
def validate_login(username,password):
    _users=get_users()
    for user in _users:
        # print type(user)
        if user.get("username")== username and \
        user.get("password")== password:
            return True               
    return False

def validate_add_user(username,password,age):
    if username.strip()=="":
        return False,"username is empty"
    _users = get_users()
    for user in _users:
        if user.get("username")==username:
            # print username
            return False,"username already exists"
    if len(password) < 6:
        # print password
        return False,"password too short"
    if not str(age).isdigit() or int(age)<0 or int(age)>100:
        # print age
        return False,"age is incorrect"
    return True,"sucess validate"

def validate_update_user(username,password,age):
    if get_user(username) is None:
        return False,"username does not exist"
    if len(password) < 6:
        return False,"password too short"
    if not str(age).isdigit() or int(age)<0 or int(age)>100:
        return False,"age is incorrect"
    return True,""

# else:
    # handler1 = open(json_path,"ab")        
    # nuser ={"username":username,"password":password,"age":age}
    # my_list=json.loads(handler1.read()).append(nuser)                
    # handler1.close()
    # return False

# def check_username(username):
#     users = get_users()
#     for info in users:
#         if info.get("username")== username:
#             return True
#     return False

if __name__ == "__main__":
    is_ok,error = validate_add_user("abc","kkkkkk",299)
    print is_ok,error
    # info = add_user("ada","111",26)
    # print info
    # xy=get_user("kk")
    # print xy
    update_user("kk","123",22)