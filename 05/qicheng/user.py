import gconf
import json
def GetUser(UserFile):
    return json.load(open(UserFile,'rb'),encoding='utf-8')

def SetUser(UserList,UserFile):
    json.dump(UserList,open(UserFile, 'w'),ensure_ascii=False)
    return True

def validate_user(username,password):
    UserList=GetUser(gconf.UserFile)
    for i in range(0,len(UserList)):
        if username == UserList[i]['username'] and password == UserList[i]['password']:
            return True
    return False

def JudgUser(username):
    UserList=GetUser(gconf.UserFile)
    for i in range(0,len(UserList)):
        if username == UserList[i]['username']:
            return True
    return False
        
def AddUser(username,password,age):
    UserList=GetUser(gconf.UserFile)
    UserList.append({'username':username,'password':password,'age':age})
    Flag=SetUser(UserList, gconf.UserFile)
    if Flag:
        return True
    else:
        return False
def ChangeUser(username,password,age):
    UserList=GetUser(gconf.UserFile)
    for i in range(0,len(UserList)):
        if username == UserList[i]['username']and password == UserList[i]['password']:
            return 'samepassword'
        elif username == UserList[i]['username']:
            UserList[i]['password'],UserList[i]['age']=password,age
            Flag=SetUser(UserList, gconf.UserFile)
            if Flag:
                return True
            else:
                return False
def DelUser(username):
    UserList=GetUser(gconf.UserFile)
    for i in range(0,len(UserList)):
        if username == UserList[i]['username']:
            UserList.pop(i)
            Flag=SetUser(UserList, gconf.UserFile)
            if Flag:
                return True
            else:
                return False
        
