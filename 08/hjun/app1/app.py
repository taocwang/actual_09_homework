#encoding: UTF-8
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

import os
import time
import json
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
	
@app.route('/useradd/', methods=['post'])	
@login_required	
def useradd():
	params = request.args if request.method == 'GET' else request.form
	username = request.form.get('useradd_username', '')
	password = request.form.get('useradd_password', '')
	age = request.form.get('useradd_age', '')
	gender = request.form.get('useradd_gender', '男')
	email = request.form.get('useradd_email', '')
	if username and len(password) >= 6 and age and gender and email:
		if user.user_add(username, password, age, gender, email):
			flash('恭喜您,添加用户:"%s" 成功' % username)
			# return redirect('/users/')
			_is_ok = True
			return json.dumps({"is_ok":_is_ok})
		else:
			# return render_template('useradd.html', useradd_info='username or password or age is error')
			_is_ok = False
			return json.dumps({"is_ok":_is_ok, "error":"用户已经存在"})
	else:
		_is_ok = False
		return json.dumps({'is_ok':_is_ok, 'error':'用户信息不完整,密码必须大于6位'})
	
@app.route('/userdel/', methods=['post'])	
@login_required	
def userdel():
	user_id = request.form.get('user_id', '')
	if user_id:
		if user.user_del(user_id):
			flash('删除用户成功')
			# return redirect('/users/')
			_is_ok = True
			return json.dumps({'is_ok':_is_ok})
		else:
			# return render_template('users.html', user_list=user.get_users(), user_info='抱歉,删除用户失败')
			_is_ok = False
			return json.dumps({'is_ok':_is_ok, 'error':'用户信息不存在'})
	else:	
		# return render_template('userdel.html', user_info='错误,用户信息不存在')	
		_is_ok = False
		return json.dumps({'is_ok':_is_ok, 'error':'用户ID为空'})
	
@app.route('/useredit/', methods=['post'])	
@login_required
def useredit():
	user_id = request.form.get('user_id', '')
	useredit_age = request.form.get('useredit_age', '')
	useredit_gender = request.form.get('useredit_gender', '')
	useredit_email = request.form.get('useredit_email', '')
	
	if user_id and useredit_age and useredit_gender and useredit_email:
		if user.user_edit(age=useredit_age, user_id=user_id, gender=useredit_gender, email=useredit_email):
			flash('恭喜您,用户信息更改成功')
			_is_ok = True
			return json.dumps({'is_ok':_is_ok})
			#return redirect('/users/')
		else:
			#return render_template('useredit.html', useredit_info='抱歉,更新用户信息失败')	
			_is_ok = False
			return json.dumps({'is_ok':_is_ok,'error':'更改用户信息失败'})
	else:
		#return render_template('useredit.html', useredit_info='错误,用户信息不存在')
		_is_ok = False
		return json.dumps({'is_ok':_is_ok, 'error':'用户信息填写不完整'})

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
	
@app.route('/updateuserpassword/', methods=['POST'])
@login_required
def charge_user_password():
	user_id = request.form.get('userid')
	manager_password = request.form.get('manager_password')
	user_password = request.form.get('user_password')
	print user_id, user_password
	_is_ok, _error = user.validate_charge_user_password(user_id, user_password, session['user']['username'], manager_password)
	if _is_ok:
		user.charge_user_password(user_id, user_password)
	return json.dumps({'is_ok':_is_ok, "error":_error})	
			
if __name__ == '__main__':
	app.run(host='0.0.0.0', port=80,debug=True)
