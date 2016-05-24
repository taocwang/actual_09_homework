#encoding: utf-8

import json
import gconf

def get_users():
	try:
		handler = open(gconf.USER_FILE, 'rb')
		cxt = handler.read()
		handler.close()
		return json.loads(cxt)
	except:
		return []

def validate_login(username, password):
	users = get_users()
	for user in users:
		if user.get('username') == username and user.get('password') == password:
			return True
	return False		

def validate_user(username):
	users = get_users()
	for user in users:
		if user.get('username') == username:
			return True
	return False
	
def user_add(username,password,age):
	if validate_user(username):
		return False
	else:
		if username != '' and password != '' and age != '':
			users = get_users()
			users.append({"username":username,"password":password,"age":age})
			cxt = json.dumps(users)
			handler = open(gconf.USER_FILE, 'w')
			handler.write(cxt)
			return True
		else:
			return False
		
def user_del(username):
	if validate_user(username):
		users = get_users()
		for i in range(0, len(users)):
			if users[i].get('username') == username:
				del(users[i])
				cxt = json.dumps(users)		
				handler = open(gconf.USER_FILE, 'w')
				handler.write(cxt)
				handler.close()
				return True	
	else:
		return False
			
def user_edit(username, password, age):
	if validate_user(username):
		users = get_users()
		for i in range(0,len(users)):
			if users[i].get('username') == username:
				users[i] = {"username":username, "password":password, "age":age}
		cxt = json.dumps(users)
		handler = open(gconf.USER_FILE, 'w')
		handler.write(cxt)
		handler.close()
		return True
	else:
		return False
		
if __name__ == '__main__':
	print user_edit(username,password,age)