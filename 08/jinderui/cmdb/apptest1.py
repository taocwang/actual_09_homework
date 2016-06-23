#encoding: utf-8
import sys,os
reload(sys)
sys.setdefaultencoding( "utf-8" )
from flask import Flask
from flask import request
from flask import redirect
from flask import render_template
from flask import session
from flask import flash
from functools import wraps
import json
import userdb as user
import logan


app = Flask(__name__)
# app.secret_key = os.urandom(32)
app.secret_key = "jinnery"

# 闭包函数，return 内层函数（内层函数是具体的实现）主要是用来判断session是否存在
def login_required(func):
	@wraps(func)
	def wrapper():
		if session.get('user') is None:
			return redirect('/')

		rt = func()      #把传进来的函数重新赋值并return return的时候一定要在if后，否则上面的代码不执行了
		return rt

	return wrapper	#返回函数，而不是函数调用


#登陆页面 入口
@app.route('/')
def index():
	# user_agent = request.headers.get('User-Agent')
	return render_template('login.html')

# 打开首页，跳转到登陆页面。成功后跳转到user页面。 
#登陆的时候进行了判断，通过外部函数user读取数据库判断用户和密码是否正确。(True就通过，False不通过)

@app.route('/login/',methods=['POST','GET'])
def login():
	flash('欢迎')
	params = request.args if request.method == 'GET' else request.form
	username = params.get('user','')
	password = params.get('password','')

	if user.validate_login(username=username,password=password): #判断用户名密码是否正确
		session['user'] = username  #添加用户session信息，防止不登陆访问其他页面

		return redirect('/users/')
	else:
		return render_template('login.html',error='用户名或密码错误') #不正确提示信息通过渲染模板实现把error的值传到login.html里面

#获取用户信息
@app.route('/users/')
@login_required            #通过调用闭包函数检查session信息。没有session跳转到登陆页面
def users():
	user_list = user.get_users()

	return render_template('users.html',user_list=user_list) #渲染模板 通过for打印所有用户在users.html里面实现


@app.route('/commituser/',methods=['POST'])
def commituser():
	#userid = request.form.get('id')
	username = request.form.get('adduser')
	age = request.form.get('addage')
	password = request.form.get('password')

	_is_ok, _error = user.validate_add_user(username, password, age) 
	if _is_ok:      #外部模块user.validate_user判断用户信息True执行
		user.add_user(username,password,age)
	return json.dumps({'is_ok':_is_ok,'error':_error})



#删除用户通过get请求获取参数。通过id然后把对应用户删掉
@app.route('/deluser/',methods=['POST'])
def deluser():
	flash('删除用户成功')
	delid = request.form.get('userid')
	
	user.del_user(delid)       #通过user.del_user函数调用sql删掉得到的用户
	return redirect('/users/')

@app.route('/changeuser/',methods=['POST','GET'])
@login_required
def changeuser():

	userid = request.form.get('userid')
	updateage = request.form.get('age')
	#获取判断信息这个地方获取的是元组
	_is_ok, _error = user.validate_user(updateage)

	#如果是true修改
	if _is_ok:
		user.change_user(userid,updateage)
	return json.dumps({'is_ok':_is_ok,'error':_error})

#退出清理sssion
@app.route('/logout/')
def logout():
	session.clear()
	return redirect('/')

#文件上传
@app.route('/upfile/')
def upfile():
	return render_template('upfile.html')

#日志展示
@app.route('/logs/',methods=['POST','GET'])
def logs():
	_upfile = request.files.get('upfile')
	print _upfile
	if _upfile:
		print _upfile
		_upfile.save('/tmp/logs')
		logan.execute_commit_sql('/tmp/logs')
	topn = request.args.get('topn',10)	#通过get请求获取topn。没有默认是10 
	_rt_list = logan.fetch_accesslog(topn) 	#从数据库获取指定数据

	return render_template('logs.html',rt_list=_rt_list)  #模板渲染展示界面

#对前端js post请求过来的数据进行判断。并返回数据让js进行相应处理
@app.route('/changepassword/',methods=['POST'])
def changepassword():
	userid = request.form.get('userid')
	print userid
	manager_password = request.form.get('manager-password')
	user_password = request.form.get('user-password')
	_is_ok,_error = user.validate_charge_user_password(userid,user_password,session['user'],manager_password)
	if _is_ok:
		user.charge_user_password(userid,user_password)
	return json.dumps({'is_ok':_is_ok,'error':_error})


if __name__ == '__main__':
	app.run(host='0.0.0.0',port=8888,debug=True)