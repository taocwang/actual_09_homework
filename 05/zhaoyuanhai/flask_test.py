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
		#获取POST传过来的参数'')
		parms = request.form
	username = parms.get('username', '')
	password = parms.get('password', '')
	age = parms.get('age', 	'')
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


@app.route('/deluser/', methods=['GET', 'POST'])
def deluser():
	username = request.args.get('username', '')
	user_action.delUser(username)
	return redirect('/users/')


@app.route('/modifyuser/', methods=['POST', 'GET'])
def modify_user():
	username = request.args.get('username', '')
	userlist = user_action.get_user()
	for i in range(0,len(userlist)):
		if userlist[i]['username'] == username:
			result = True
			return render_template('modify.html', content=userlist[i])


@app.route('/upuser/', methods=['GET', 'POST'])
def upuser():
	username = request.form.get('username', '')
	password = request.form.get('password', '')
	age = request.form.get('age', '')
	phone = request.form.get('phone', '')
	email = request.form.get('email', '')
	if username == '' or password == '':
		content = user_action.get_user()
		return render_template('user_list.html', error='username or password can not be empty!', content = content)
	user_action.modifyUser(username, password, age, phone, email)
	return redirect('/users/')






if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9001, debug=True)

'''
功能ok， 继续加油

改进点
1. app中(C)尽量只保持逻辑调用代码，不关注用户信息检查逻辑和操作逻辑，只从浏览器请求中获取(V)，传递给user模块(M)
2. 注意app中函数一定要有返回值，line 76函数，若username是随便填写的，程序会发生什么问题？
3. 用户增、删、改都需要修改user.json文件，是否可以写成一个函数来处理
'''
