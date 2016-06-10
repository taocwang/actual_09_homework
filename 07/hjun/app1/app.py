#encoding: UTF-8
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

import os
import time
from functools import wraps
from flask import Flask
from flask import render_template
from flask import request
from flask import redirect
from flask import session
from flask import flash

import gconf
import user
import logscount

app = Flask(__name__)
app.secret_key = os.urandom(32)

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
	return render_template('login.html')

@app.route('/login/', methods=['get','post'])	
def login():
	params = request.args if request.method == 'GET' else request.form
	username = params.get('username', '')
	password = params.get('password', '')
	if user.validate_login(username, password):
		session['user'] = {'username': username}
		return redirect('/logs/')
	else:
		return render_template('login.html', username=username, error='username or password is error')

@app.route('/logout/')
def logout():
	session.clear()
	print session
	return redirect('/')
		
@app.route('/logs/')
@login_required
def logs():
	cut = request.args.get('cut')
	cut = int(cut) if str(cut).isdigit() else 10
	rt_list = logscount.logscount(cut=cut)
	return render_template('logs.html', rt_list=rt_list, logs_info="请选择文件 ")

@app.route('/useradd/index/', methods=['get','post'])	
@login_required	
def useradd_index():
	return render_template('useradd.html')	
	
@app.route('/useradd/', methods=['get','post'])	
@login_required	
def useradd():
	params = request.args if request.method == 'GET' else request.form
	username = request.form.get('username', '')
	password = request.form.get('password', '')
	age = request.form.get('age', '')
	gender = request.form.get('gender', '男')
	email = request.form.get('email', '')
	img = request.files.get('img')
	if user.user_add(username, password, age, gender, email):
		flash('恭喜您,添加用户:"%s" 成功' % username)
		return redirect('/users/')
	else:
		return render_template('useradd.html', useradd_info='username or password or age is error')
	
@app.route('/userdel/index/', methods=['get','post'])	
@login_required	
def userdel_index():
	params = request.args if request.method =='GET' else request.form
	user_id = params.get('user_id', '')
	if user_id:
		if user.user_del(user_id):
			flash('删除用户成功')
			return redirect('/users/')
		else:
			return render_template('users.html', user_list=user.get_users(), user_info='抱歉,删除用户失败')
	else:	
		return render_template('userdel.html', user_info='错误,用户信息不存在')	

@app.route('/useredit/index/', methods=['get','post'])
@login_required
def useredit_index():
	params = request.args if request.method =='GET' else request.form
	user_id = params.get('user_id', '')
	user_info = user.get_user(user_id)
	if user_info:
		username = user_info['username']
		password = user_info[ 'password' ]
		age = user_info[ 'age' ]
		gender = user_info[ 'gender' ]
		email = user_info[ 'email' ]
		return render_template('useredit.html', user_id=user_id, username=username, password=password, age=age, gender=gender, email=email)
	else:
		return render_template('useredit.html', useredit_info='更新用户失败,用户信息不存在')	
	
@app.route('/useredit/', methods=['get','post'])	
@login_required
def useredit():
	params = request.args if request.method == 'GET' else request.form
	user_id = request.form.get('user_id', '')
	age = request.form.get('age', '')
	password = request.form.get('password', '')
	gender = request.form.get('gender', '')
	email = request.form.get('email', '')
	username = request.form.get('username', '')
	
	if user_id:
		if user.user_edit(age=age, user_id=user_id, password=password, gender=gender, email=email):
			flash('恭喜您 用户[%s] 信息更改成功' % username )
			return redirect('/users/')
		else:
			return render_template('useredit.html', useredit_info='抱歉,更新用户信息失败')	
	else:
		return render_template('useredit.html', useredit_info='错误,用户信息不存在')

@app.route('/upload_logs/', methods=['get','post'])	
@login_required
def upload_logs():
	upload_logs = request.files.get('upload_logs')
	if upload_logs:
		filename=upload_logs.filename + "." + time.strftime("%Y%m%d%H%M%S", time.localtime())
		logs_filename = gconf.LOG_PATH + filename
		#return logs_filename
		upload_logs.save(logs_filename)
		logscount.load_data_logs(logs_filename)
		flash('恭喜您文件[%s] 处理成功' % upload_logs.filename )
		return redirect('/logs/')
	else:
		return redirect('/logs/')
@app.route('/users/')
@login_required
def users():	
	return render_template('users.html', user_list=user.get_users())		
			
if __name__ == '__main__':
	app.run(host='0.0.0.0', port=80,debug=True)
