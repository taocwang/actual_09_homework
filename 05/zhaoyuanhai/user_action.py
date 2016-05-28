#!/usr/bin/env python
#-*- coding:utf-8 -*-
import json, gconfig
from flask import request
def get_user():
	try:
		f = open(gconfig.USER_FILE, 'rb')
		content = f.read()	
		f.close()
		return json.loads(content)
		#return content
	except BaseException as e:
		print e
		return []
def validate_login(username, password):

	users = get_user()
	for user in users:
		if user.get('username') == username and user.get('password') == password:
			return True
	return False


def user_list(number):
	users = get_user()
	userlist = sorted(users, key=lambda x:x['username'])
	if len(userlist) > number:
		return userlist[:number]
	else:
		return userlist
def add_user(username, password, age, phone, email):
	userinfo = {'username': username, 'password': password, 'age': age, 'phone': phone, 'email': email}
	userlist.append(userinfo)
	f = open(gconfig.USER_FILE, 'wb')
	f.write(json.dumps(userlist))
	f.close()

def delUser(username):
	users = get_user()
	for i in range(0, len(users)):
		if users[i]['username'] == username:
			users.pop(i)
	f = open(gconfig.USER_FILE, 'wb')
	f.write(json.dumps(users))
	f.close()

def modifyUser(username, password, age, phone, email):
	users = get_user()
	for i in range(0,len(users)):
		if users[i]['username'] == username:
			users[i].update({'password': password, 'age': age, 'phone': phone, 'email': email})


if __name__ == '__main__':
	print get_user()