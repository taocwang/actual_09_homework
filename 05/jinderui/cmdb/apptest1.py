#encoding: utf-8
import sys,os
reload(sys)
sys.setdefaultencoding( "utf-8" )
from flask import Flask
from flask import request
from flask import redirect
from flask import render_template
import json
import user


app = Flask(__name__)

#登陆页面 入口
@app.route('/')
def index():
	# user_agent = request.headers.get('User-Agent')
	return render_template('login.html')

# 打开首页，跳转到登陆页面。成功后跳转到user页面。 
#登陆的时候进行了判断，通过外部函数user读取文件判断用户和密码是否正确。(True就通过，False不通过)
@app.route('/login/',methods=['POST','GET'])
def login():
	params = request.args if request.method == 'GET' else request.form
	username = params.get('user','')
	password = params.get('password','')

	if user.validate_login(username=username,password=password): #判断用户名密码是否正确
		return redirect('/users/')
	else:
		return render_template('login.html',error='用户名或密码错误') #不正确提示信息通过渲染模板实现把error的值传到login.html里面

#获取用户信息
@app.route('/users/')
def users():
	user_list = user.get_users()
	return render_template('users.html',user_list=user_list) #渲染模板 通过for打印所有用户在users.html里面实现


#通过users.html里面的添加按钮，跳转到 adduser页面进行添加用户信息（form表单实现）
@app.route('/adduser/',methods=['GET'])
def adduser():
	return render_template('adduser.html') #跳转到adduser.html里面


#通过adduser函数。添加完信息以后获取用户信息跳转到 用户users页面(存在的用户不让重复添加)
@app.route('/commituser/',methods=['POST'])
def commituser():
	adduser = request.form.get('adduser')
	addage = request.form.get('addage')
	addpassword = request.form.get('password')

	if user.validate_user(adduser,addage,addpassword):  #外部模块user.validate_user判断用户信息True执行
		user.add_user(adduser,addage,addpassword)
		return redirect('/users/')
	else:												# 检查不通过 提示信息
		return render_template('adduser.html',user='信息不正确')


#删除用户通过get请求获取参数。然后把对应用户删掉
@app.route('/deluser/')
def deluser():
	deluser = request.args.get('act')
	
	user.del_user(deluser)       #通过user.del_user函数删掉得到的用户
	return redirect('/users/')

#更新用户先要把用户的信息带过去，这个地方用了get为了不让密码显示html里面写的是***
@app.route('/updateuser/')
def updateuser():
	username = request.args.get('actname')          #获取get actname的参数
	_user = user.get_user(username)					#
	if _user is None:
		_error = '用户信息不存在'
	else:
		updateuser = _user.get('username')
		updateage = _user.get('age')
		updatepassword = _user.get('password')
	return render_template('updateuser.html',updateuser=updateuser,updateage=updateage,updatepassword=updatepassword)


'''
通过updateuser函数获取原有的用户信息，用户名年龄。然后和要改的进行对比，发现age被修改了。
重新赋值并写入（这个地方username是唯一的）所以说不能修改用户名
'''
@app.route('/changeuser/',methods=['POST'])
def changeuser():
	updateuser = request.form.get('user')
	updateage = request.form.get('age')
	updatepassword = request.form.get('password')

	user.change_user(updateuser,updateage,updatepassword)
	return redirect('/users/')
	user_list=user.get_users()
	
if __name__ == '__main__':
	app.run(host='0.0.0.0',port=8888,debug=True)