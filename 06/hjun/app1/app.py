#encoding: UTF-8

import os
from functools import wraps
from flask import Flask
from flask import render_template
from flask import request
from flask import redirect
from flask import session
from flask import flash
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
	#return rt_list[0][0]
	return render_template('logs.html',rt_list=rt_list, title='topn 10g')

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
	if user.user_add(username, password, age):
		flash('New users [%s] more successful' % username)
		return redirect('/users/')
		#return render_template('users.html', user_list=user.get_users(), user_info='Add User [%s] Success') % username
	else:
		return render_template('useradd.html', useradd_info='username or password or age is error')
	
@app.route('/userdel/index/', methods=['get','post'])	
@login_required	
def userdel_index():
	params = request.args if request.method =='GET' else request.form
	username = params.get('username', '')
	if username:
		if user.user_del(username):
			flash('User [%s] successfully deleted' % username)
			return redirect('/users/')
			#return render_template('users.html', user_list=user.get_users(), user_info='User [%s] successfully deleted') % username
		else:
			return render_template('users.html', user_list=user.get_users(), user_info='error, Remove user [%s] failed') % username
	else:	
		return render_template('userdel.html')	
	
@app.route('/userdel/', methods=['get','post'])		
@login_required	
def userdel():
	params = request.args if request.method == 'GET' else request.form
	username = params.get('username', '')	
	if user.user_del(username):
		flash('User [%s] successfully deleted' % username)
		return redirect('/users/')
		#return render_template('users.html', user_list=user.get_users(), user_info='User [%s] successfully deleted') % username
	else:
		return render_template('userdel.html', userdel_info='error, no user')

@app.route('/useredit/index/', methods=['get','post'])
@login_required
def useredit_index():
	params = request.args if request.method =='GET' else request.form
	username = params.get('username', '')
	if username:
		user_info = user.get_user(username)
		if user_info:
			username = user_info.get('username')
			password = user_info.get('password')
			age = user_info.get('age')
			return render_template('useredit.html', username=username, password=password, age=age)
		else:
			return render_template('useredit.html', useredit_info='username error')
	else:
		return render_template('useredit.html')	
	
@app.route('/useredit/', methods=['get','post'])	
@login_required
def useredit():
	params = request.args if request.method == 'GET' else request.form
	username = request.form.get('username', '')
	password = request.form.get('password', '')
	age = request.form.get('age', '')	
	if user.user_edit(username, password, age):
		flash('New users [%s]  more successful' % username )
		return redirect('/users/')
		#return render_template('users.html', user_list=user.get_users(), user_info='New users [%s] more successful') % username
	else:
		return render_template('useredit.html', useredit_info='username error')		
		
@app.route('/users/')
@login_required
def users():	
	return render_template('users.html', user_list=user.get_users())		
			
if __name__ == '__main__':
	app.run(host='0.0.0.0', port=80,debug=True)
	#print logs()
