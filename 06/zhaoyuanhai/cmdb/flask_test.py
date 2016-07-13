#!/usr/bin/env python
#-*- coding:utf-8 -*-
from flask import Flask, render_template, session, flash
from flask import request, redirect
import gconfig, json, os, sys
import user_action
from functools import wraps
import user_action, user_action
import loganalysis

app = Flask(__name__)
app.secret_key = 'jdlaksjdflsfjd;'

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


@app.route('/logs/')
@login_required
def logs_detail():
	number = request.args.get('number', 10)
	result = loganalysis.logTop(number)
	title = 'accesslog detail top {number}'.format(number=number)
	return render_template('accesslog_detail.html', title=title, content=result)


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
	age = parms.get('age', 	10)
	phone = parms.get('phone', '')
	email = parms.get('email', '')
	if  username.strip() == '' or  password == '':
		flash('username or password cant be empty!!')
		return render_template('adduser.html')
	result = user_action.add_user(username, password, age, phone, email)
	if result:
		flash('{username}创建成功'.format(username=username))
		return redirect('/users/')
	else:
		flash('{username}已存在'.format(username=username))
		return redirect('/adduser/')



@app.route('/deluser/', methods=['GET', 'POST'])
@login_required
def deluser():
	# if session.get('user') is None:
	# 	return redirect('/')
	uid = request.args.get('uid', '')
	result = user_action.delUser(uid)
	if result:
		flash('用户ID{uid}删除成功'.format(uid=uid))
		return redirect('/users/')
	else:
		flash('id{uid}删除失败'.format(uid=uid))
		return redirect('/users/')


@app.route('/modifyuser/', methods=['POST', 'GET'])
@login_required
def modify_user():
	# if session.get('user') is None:
	# 	return redirect('/')
	uid = request.args.get('uid', '')
	_content = user_action.modifyUser(uid)
	print _content
	if _content:
		return render_template('modify.html', content=_content)
	else:
		flash('用户不存在')
		return redirect('/users/')


@app.route('/upuser/', methods=['GET', 'POST'])
@login_required
def upuser():
	uid = request.form.get('uid', '')
	username = request.form.get('username', '')
	password = request.form.get('password', '')
	age = request.form.get('age', 10)
	phone = request.form.get('phone', '')
	email = request.form.get('email', '')
	if password == '':
		content = user_action.get_user()
		flash('password can not be empty!')
		return render_template('user_list.html', content = content)
	user_action.upToDb(uid,username, password, age, phone, email)
	flash('ID{uid}修改成功'.format(uid=uid))
	return redirect('/users/')

@app.route('/logout/')
def logout():
	session.clear()
	#del session['user']
	return redirect('/')



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9002, debug=True)
