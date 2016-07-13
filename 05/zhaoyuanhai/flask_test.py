#!/usr/bin/env python
#-*- coding:utf-8 -*-
from flask import Flask, render_template, session, flash
from flask import request, redirect
import user_action, gconfig, json, os, sys
from functools import wraps

app = Flask(__name__)
app.secret_key = os.urandom(32)

reload(sys)
sys.setdefaultencoding('utf-8')
def login_required(func):
	@wraps(func)
	def wrapper(*args, **kwargs):
		if session.get('user') is None:
			return redirect('/')
		rt = func(*args, **kwargs)
		return rt
	return wrapper


@app.route('/')
def index():
    return render_template('user_login.html')

@app.route('/users/')
@login_required
def re_userlist():
	#return number
	# if session.get('user') is None:   判断用户是否登陆
	# 	return redirect('/')
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
		session['user'] = {'username' : username}
		flash('登陆成功')
		return redirect('/users/')
	else:
		#登陆失败，返回错误信息回页面
		return render_template('user_login.html', username=username, error="username or password error!!")


@app.route('/adduser/', methods=['POST', 'GET'])
@login_required
def add_user():
	# if session.get('user') is None:
	# 	return redirect('/')
	return render_template('adduser.html')


@app.route('/wuser/', methods=['POST', 'GET'])
@login_required
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
			flash('user has regedited!!')
			return render_template('adduser.html')
	if  username == '' or  password == '':
		flash('username or password cant be empty!!')
		return render_template('adduser.html')
	else:
		user_action.add_user(username, password, age, phone, email)
		result = user_action.user_list(10)
		flash('user add sucessful!')
		return render_template('user_list.html', title='top 10 user', content=result)


@app.route('/deluser/', methods=['GET', 'POST'])
@login_required
def deluser():
	# if session.get('user') is None:
	# 	return redirect('/')
	username = request.args.get('username', '')
	user_action.delUser(username)
	flash('用户{username}删除成功'.format(username=username))
	return redirect('/users/')


@app.route('/modifyuser/', methods=['POST', 'GET'])
@login_required
def modify_user():
	# if session.get('user') is None:
	# 	return redirect('/')
	username = request.args.get('username', '')
	userlist = user_action.get_user()
	for i in range(0,len(userlist)):
		if userlist[i]['username'] == username:
			flash('修改用户%s' %username)
			return render_template('modify.html', content=userlist[i])


@app.route('/upuser/', methods=['GET', 'POST'])
@login_required
def upuser():
	username = request.form.get('username', '')
	password = request.form.get('password', '')
	age = request.form.get('age', '')
	phone = request.form.get('phone', '')
	email = request.form.get('email', '')
	if username == '' or password == '':
		content = user_action.get_user()
		flash('username or password can not be empty!')
		return render_template('user_list.html', content = content)
	user_action.modifyUser(username, password, age, phone, email)
	flash('用户{username}修改成功'.format(username=username))
	return redirect('/users/')

@app.route('/logout/')
def logout():
	session.clear()
	#del session['user']
	return redirect('/')




if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9001, debug=True)

'''
功能ok， 继续加油

改进点
1. app中(C)尽量只保持逻辑调用代码，不关注用户信息检查逻辑和操作逻辑，只从浏览器请求中获取(V)，传递给user模块(M)
2. 注意app中函数一定要有返回值，line 76函数，若username是随便填写的，程序会发生什么问题？
3. 用户增、删、改都需要修改user.json文件，是否可以写成一个函数来处理
'''
