#encoding: UTF-8

from flask import Flask
from flask import render_template
from flask import request
from flask import redirect
import user
import logscount
app = Flask(__name__)


@app.route('/')
def index():
	return render_template('login.html')

@app.route('/login/', methods=['get','post'])
def login():
	params = request.args if request.method == 'GET' else request.form
	username = params.get('username', '')
	password = params.get('password', '')
	if user.validate_login(username, password):
		return redirect('/logs/')
	else:
		return render_template('login.html', username=username, error='username or password is error')

@app.route('/logs/')
def logs():
	cut = request.args.get('cut')
	cut = int(cut) if str(cut).isdigit() else 10
	rt_list = logscount.logscount(path='www_access_20140823.log',cut=cut)
	return render_template('logs.html',rt_list=rt_list, title='topn 10g')

@app.route('/useradd/index/', methods=['get','post'])
def useradd_index():
	return render_template('useradd.html')

@app.route('/useradd/', methods=['get','post'])
def useradd():
	params = request.args if request.method == 'GET' else request.form
	username = request.form.get('username', '')
	password = request.form.get('password', '')
	age = request.form.get('age', '')
	if user.user_add(username, password, age):
		return redirect('/users/')
		#return render_template('users.html', user_list=user.get_users(), user_info='Add User [%s] Success') % username
	else:
		return render_template('useradd.html', useradd_info='username or password or age is error')

@app.route('/userdel/index/', methods=['get','post'])
def userdel_index():
<<<<<<< HEAD
	params = request.args if request.method =='GET' else request.form
	username = params.get('username', '')
	if username:
		if user.user_del(username):
			return redirect('/users/')
			#return render_template('users.html', user_list=user.get_users(), user_info='User [%s] successfully deleted') % username
		else:
			return render_template('users.html', user_list=user.get_users(), user_info='error, Remove user [%s] failed') % username
	else:	
		return render_template('userdel.html')	
	
@app.route('/userdel/', methods=['get','post'])		
def userdel():
	params = request.args if request.method == 'GET' else request.form
	username = params.get('username', '')	
=======
	return render_template('userdel.html')

@app.route('/userdel/', methods=['get','post'])
def userdel():
	params = request.args if request.method == 'GET' else request.form
	username = request.form.get('username', '')
>>>>>>> 63c34a46c3795b80b84dac5a6bbcc8b6f7827b4d
	if user.user_del(username):
		return redirect('/users/')
		#return render_template('users.html', user_list=user.get_users(), user_info='User [%s] successfully deleted') % username
	else:
		return render_template('userdel.html', userdel_info='error, no user')

@app.route('/useredit/index/', methods=['get','post'])
def useredit_index():
<<<<<<< HEAD
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
=======
	return render_template('useredit.html')

@app.route('/useredit/', methods=['get','post'])
>>>>>>> 63c34a46c3795b80b84dac5a6bbcc8b6f7827b4d
def useredit():
	params = request.args if request.method == 'GET' else request.form
	username = request.form.get('username', '')
	password = request.form.get('password', '')
	age = request.form.get('age', '')
	if user.user_edit(username, password, age):
<<<<<<< HEAD
		return redirect('/users/')
		#return render_template('users.html', user_list=user.get_users(), user_info='New users [%s] more successful') % username
=======
		return render_template('useredit.html', useredit_info='New users [%s] more successful') % username
>>>>>>> 63c34a46c3795b80b84dac5a6bbcc8b6f7827b4d
	else:
		return render_template('useredit.html', useredit_info='username error')

@app.route('/users/')
def users():
	return render_template('users.html', user_list=user.get_users())

if __name__ == '__main__':
	app.run(host='0.0.0.0', port=80,debug=True)


'''
ok，功能没有问题
改进
1. 用户在编辑时，可以将编辑的用户信息回显到编辑页面
2. 可以对用户输入进行严格检查
比如用户名不能为空，用户名&密码的长度必须在某个范围内容，age必须是在某个范围内的数字等等
任何用户输入的是不可信的
3. 用户信息存储文件的代码，增、删、改都有，是否能提取成一个函数（一段代码copy 1次，再copy第二次第三次就需要考虑是否写成函数了）

继续加油哦
'''
