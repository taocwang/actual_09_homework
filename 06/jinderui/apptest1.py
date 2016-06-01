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


app = Flask(__name__)
app.secret_key = os.urandom(32)

# 闭包函数，return 内层函数（内层函数是具体的实现）主要是用来判断session是否存在
def login_required(func):
	@wraps(func)
	def wrapper():
		if session.get('user') is None:
			return redirect('/')

		rt = func()      #把传进来的函数重新赋值并return return的时候一定要在if后，否则上面的代码不执行了
		return rt

	return wrapper


#登陆页面 入口
@app.route('/')
def index():
	# user_agent = request.headers.get('User-Agent')
	return render_template('login.html')

# 打开首页，跳转到登陆页面。成功后跳转到user页面。 
#登陆的时候进行了判断，通过外部函数user读取数据库判断用户和密码是否正确。(True就通过，False不通过)

@app.route('/login/',methods=['POST','GET'])
def login():
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


#通过users.html里面的添加按钮，跳转到 adduser页面进行添加用户信息（form表单实现）
@app.route('/adduser/',methods=['GET'])
@login_required
def adduser():
	flash('添加用户成功')
	return render_template('adduser.html') #跳转到adduser.html里面


#通过adduser函数。添加完信息以后获取用户信息跳转到 用户users页面(id是唯一的。可以添加重复账号)
@app.route('/commituser/',methods=['POST'])
def commituser():
	#userid = request.form.get('id')
	username = request.form.get('adduser')
	age = request.form.get('addage')
	password = request.form.get('password')
	
	_is_ok, _error = user.validate_user(username, password, age) 
	if _is_ok:      #user.validate_user(username,password,age):  #外部模块user.validate_user判断用户信息True执行
		user.add_user(username,password,age)
		return redirect('/users/')
	else:												# 检查不通过 提示信息
		return render_template('adduser.html',error=_error,adduser=username,addage=age,password=password)


#删除用户通过get请求获取参数。通过id然后把对应用户删掉
@app.route('/deluser/')
def deluser():
	flash('删除用户成功')
	delid = request.args.get('act')
	
	user.del_user(delid)       #通过user.del_user函数调用sql删掉得到的用户
	return redirect('/users/')

#更新用户先要把用户的信息带过去，通过get到userid然后去user.get_user函数去获取用户信息。id唯一不让其显示
@app.route('/updateuser/')
def updateuser():
	flash('更新用户成功')
	global userid                        #定义了一个全局变量为了让changuser函数获取用户id
	userid = request.args.get('actid') 

     #获取get actname的参数
	_user = user.get_user(userid)

	if _user is None:
		_error = '用户信息不存在'
	else:
		updateuser = _user.get('username')
		updateage = _user.get('age')
		updatepassword = _user.get('password')
	return render_template('updateuser.html',updateuser=updateuser,updateage=updateage,updatepassword=updatepassword)


'''
通过updateuser函数获取原有的用户信息，id,用户名年龄。然后和要改的进行对比，
重新赋值并写入（这个地方id是唯一的）所以说不能修改。更新的时候是通过id判断的，所以id还必须要有。
通过updateuser定义的 全局变量拿到
'''
@app.route('/changeuser/',methods=['POST','GET'])
def changeuser():

	updateuser = request.form.get('user')
	updateage = request.form.get('age')
	updatepassword = request.form.get('password')

	_is_ok, _error = user.validate_user(updateuser,updatepassword,updateage,userid) #获取判断信息这个地方获取的是元组

	if _is_ok:
		user.change_user(userid,updateuser,updateage,updatepassword) #如果是true修改
		return redirect('/users/')
	else:			
		return render_template('updateuser.html',userid=userid,error=_error, updateuser=updateuser, updatepassword=updatepassword, updateage=updateage)


#退出清理sssion
@app.route('/logout/')
def logout():
	session.clear()
	return redirect('/')
	
if __name__ == '__main__':
	app.run(host='0.0.0.0',port=8888,debug=True)