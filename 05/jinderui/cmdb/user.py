#encoding: utf-8
import json

#查询所有用户信息
def get_users():
	with open('userportal.txt','rb') as f:
		cxt = f.read()
		return json.loads(cxt)

#检查 用户名密码是否正确。正确返回True 不正确返回False
def validate_login(username,password):
	users = get_users()

	for user in users:
		if user.get('username') == username and user.get('password') == password:
			return True

	return False

#检查用户信息，如果不满足就返回False。也就是检查不通过
def validate_user(username,age,password):
	if username.strip() == '':
		return False, u'用户名不能为空'

	user_list = get_users()
	for users in user_list:
		if username in users['username']:
			return False
	
	if len(password) < 6:
		return False
	if not str(age).isdigit() or int(age) <= 0 or int(age) > 100:
		return False
	return True

#将信息保存到文件
def save_user(user_list):
	with open('userportal.txt','wb') as wf:
		wf.write(json.dumps(user_list))

#添加用户，调用save_uer并写入到文件
def add_user(adduser,addage,addpassword):
	user_list = get_users()
	if adduser and addage and addpassword:
		user_list.append({'username':adduser,'age':addage,'password':addpassword})

	save_user(user_list)


#删除用户，调用save_uer并重新写入到文件
def del_user(deluser):
	user_list = get_users()
	for users in user_list:
		if users['username'] == deluser:
			del user_list[user_list.index(users)]
	save_user(user_list)

#更新用户，调用save_uer并重新写入到文件
def change_user(updateuser,updateage,updatepassword):
	user_list = get_users()
	for users in user_list:
		if users['username'] == updateuser:
			if users['age'] != updateage:
				user_list[user_list.index(users)]['age'] = updateage
			if users['password'] != updatepassword:
				user_list[user_list.index(users)]['password'] = updatepassword
	save_user(user_list)

#获取指定用户的信息
def get_user(username):
    _users = get_users()
    for _user in _users:
        if _user.get('username') == username:
            return _user   #在for里面return的。所以每次返回的只是判断正确的用户信息（是一个字典）
    return None