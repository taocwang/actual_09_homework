#!/usr/bin/env python
#-*- coding:utf-8 -*-
from flask import Flask, render_template
from flask import request, redirect
import user_action, gconfig, json

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('user_login.html')

@app.route('/users/')
def re_userlist():
	#return number
	number = request.args.get('number', 10)
	result = user_action.user_list(number)
	title = 'user top{number}'.format(number=number)
	return render_template('user_list.html',title=title, content=result)

@app.route('/login/', methods=['POST', 'GET'])
def login():
	if request.method == 'GET':
		#获取POST传过来的参数
		parms = request.args
	else:
		#获取POST传过来的参数
		parms = request.form
	username = parms.get('username', '')
	password = parms.get('password', '')
	#return '%s:%s'%(username,password)
	if user_action.validate_login(username, password):
		return redirect('/users/')
	else:
		#登陆失败，返回错误信息回页面
		return render_template('user_login.html', username=username, error="username or password error!!")

@app.route('/adduser/', methods=['POST', 'GET'])
def add_user():
	return render_template('adduser.html')

@app.route('/wuser/', methods=['POST', 'GET'])
def writeuser():
	if request.method == 'GET':
		#获取POST传过来的参数
		parms = request.args
	else:
		#获取POST传过来的参数
		parms = request.form
	username = parms.get('username', '')
	password = parms.get('password', '')
	age = parms.get('age', '')
	phone = parms.get('phone', '')
	email = parms.get('email', '')
	userlist = user_action.get_user()
	for i in userlist:
		if username == i['username']:
			return render_template('adduser.html', error='user has regedited!!')
	if  username == '' or  password == '':
		return render_template('adduser.html', error='username or password cant be empty!!')
	else:
		user_action.add_user(username, password, age, phone, email)
		result = user_action.user_list(10)
		return render_template('user_list.html', title='top 10 user', sucessinfo = 'user add sucessful!', content=result)
@app.route('/delusr/', methods=['GET', 'POST'])
def deluser():
	username = request.args.get('username', '')
	user_action.delUser('username')
	return redirect('/users')

@app.route('/modify/', methods=['POST', 'GET'])
def modify_user():
	username = request.args.get('username', '')
	userlist = user_action.get_user()
	if username in userlist
	for i in range(0,len(userlist)):
		if userlist[i]['username'] == username:
			return render_template('modify.html', result=user_list[i])
		


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9001, debug=True)