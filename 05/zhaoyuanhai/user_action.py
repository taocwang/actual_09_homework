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

def file_read(file):
	try:
		f = open(file, 'r')
		content = f.read()
		f.close()
		return content
	except Exception, e:
		print e
		return e

def file_write(file, content):
	try:
		f = open(file, 'wb')
		f.write(content)
		f.close()
		return 'sucess'
	except Exception, e:
		print e
		return False


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
	userlist = get_user()
	userinfo = {'username': username, 'password': password, 'age': age, 'phone': phone, 'email': email}
	userlist.append(userinfo)
	result = file_write(gconfig.USER_FILE, json.dumps(userlist))
	return result
	# f = open(gconfig.USER_FILE, 'wb')
	# f.write(json.dumps(userlist))
	# f.close()

def delUser(username):
	users = get_user()
	for i in range(0, len(users)):
		if users[i]['username'] == username:
			users.pop(i)
			break
	result = file_write(gconfig.USER_FILE, json.dumps(users))
	return result

def modifyUser(username, password, age, phone, email):
	users = get_user()
	for i in range(0,len(users)):
		if users[i]['username'] == username:
			users[i].update({'password': password, 'age': age, 'phone': phone, 'email': email})

	result = file_write(gconfig.USER_FILE, json.dumps(users))
	return result

if __name__ == '__main__':
	delUser('user2')