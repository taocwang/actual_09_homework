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
import asset

app = Flask(__name__)
#app.secret_key = os.urandom(32)
app.secret_key = '123'

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
			_is_ok = True
			return json.dumps({"is_ok":_is_ok})
		else:
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
			_is_ok = True
			return json.dumps({'is_ok':_is_ok})
		else:
			_is_ok = False
			return json.dumps({'is_ok':_is_ok, 'error':'用户信息不存在'})
	else:	
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
		else:
			_is_ok = False
			return json.dumps({'is_ok':_is_ok,'error':'更改用户信息失败'})
	else:
		_is_ok = False
		return json.dumps({'is_ok':_is_ok, 'error':'用户信息填写不完整'})

@app.route('/upload_logs/', methods=['get','post'])	
@login_required
def upload_logs():
	upload_logs = request.files.get('upload_logs')
	if upload_logs:
		filename=upload_logs.filename + "." + time.strftime("%Y%m%d%H%M%S", time.localtime())
		logs_filename = gconf.LOG_PATH + filename
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

@app.route('/assets/')
@login_required
def assets():	
	assets = asset.get_list()
	return render_template('assets.html', assets=assets)	

@app.route('/asset/create/', methods=['POST','GET'])	
@login_required
def create_asset():
	idcs = asset.idcs_list()
	return render_template('asset_create.html', idcs=idcs)

@app.route('/asset/add/', methods=['POST'])	
@login_required
def add_asset():
	asset_info=request.form
	_is_ok,_errors = asset.validate(asset_info)
	if _is_ok:
		if asset.create(asset_info):
			_is_ok=True
		else:
			_is_ok=False
			_errors = {"add":"添加不成功"}
	return json.dumps({"is_ok":_is_ok, "success":"添加成功", "errors":_errors, "asset_info":asset_info})

@app.route('/asset/edit/', methods=['POST','GET'])	
@login_required
def edit_asset():
	asset_id = request.form.get("asset_id")
	print '资产ID', asset_id
	idcs = asset.idcs_list()
	_asset = asset.get_list(asset_id)
	print '打印资产',_asset
	return render_template('asset_update.html', idcs=idcs, asset=_asset[0])
	
@app.route('/asset/update/', methods=['POST'])	
@login_required	
def update_asset():
	asset_info=request.form
	print '更新资产',asset_info
	repeat=False
	_is_ok,_errors = asset.validate(asset_info,repeat)
	if _is_ok:
		if asset.update(asset_info):
			_is_ok=True
		else:
			_is_ok=False
			_errors = {"update":"更新不成功"}
	return json.dumps({"is_ok":_is_ok, "success":"更新成功", "errors":_errors, "asset_info":asset_info})
	
@app.route('/asset/del/', methods=['POST','GET'])	
@login_required
def del_asset():
	asset_id = request.form.get("asset_id")
	return render_template('asset_delete.html', asset_id=asset_id)
	
@app.route('/asset/drop/', methods=['POST'])	
@login_required	
def drop_asset():
	asset_id = request.form.get("id")
	if asset_id:
		print 'ok删除资产',asset_id
		_is_ok = asset.drop(asset_id)
		errors = {"drop":"删除不成功"}
		success = "删除成功"
	else:
		_is_ok = False
		errors = {"drop":"ID为空,删除不成功"}
	return json.dumps({"is_ok":_is_ok, "success":success, "errors":errors, "asset_info":{'id':asset_id}})	
	
if __name__ == '__main__':
	app.run(host='0.0.0.0', port=80,debug=True)
