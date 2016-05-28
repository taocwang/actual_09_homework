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

# 登陆成功后跳转到user页面。 登陆的时候进行了判断，通过外部函数user读取文件判断用户和密码是否正确。
@app.route('/login/',methods=['POST','GET'])
def login():
	params = request.args if request.method == 'GET' else request.form
	username = params.get('user','')
	password = params.get('password','')

	if user.validate_login(username=username,password=password): #判断用户名密码是否正确

		return redirect('/users/')
	else:
		return render_template('login.html',error='用户名或密码错误')

#获取用户信息
@app.route('/users/')
def users():
	user_list = user.get_user()
	return render_template('users.html',user_list=user_list)


#通过users.html里面的添加按钮，跳转到 adduser页面进行添加用户信息
@app.route('/adduser/',methods=['GET'])
def adduser():
	return render_template('adduser.html')  #adduser.html是个form表单。


#通过adduser函数。添加完信息以后获取用户信息跳转到 用户users页面(存在的用户不让重复添加)
@app.route('/commituser/',methods=['POST'])
def commituser():
	adduser = request.form.get('adduser')
	addage = request.form.get('addage')
	addpassword = request.form.get('password')
	user_list = user.get_user()

	for users in user_list:
		if adduser in users['username']:
			return render_template('adduser.html',user='用户名已存在')

	if adduser and addage and addpassword:
		user_list.append({'username':adduser,'age':addage,'password':addpassword})
		user.add_user(json.dumps(user_list))
		return redirect('/users/')
	else:
		return render_template('adduser.html',info='信息不能为空')

#删除用户通过get请求获取参数，进行判断。然后删除，并重新写入到文件。
@app.route('/deluser/')
def deluser():
	deluser = request.args.get('act')
	user_list = user.get_user()

	for users in user_list:
		if users['username'] == deluser:
			del user_list[user_list.index(users)]

	user.add_user(json.dumps(user_list))

	return redirect('/users/')

#更新用户先要把用户的信息带过去，这个地方用了get为了不让密码显示html里面写的是***
@app.route('/updateuser/')
def updateuser():
	updateuser = request.args.get('actname')
	updateage = request.args.get('actage')
	updatepassword = request.args.get('actpassword')
	return render_template('updateuser.html',updateuser=updateuser,updateage=updateage,updatepassword=updatepassword)


'''
通过updateuser函数获取原有的用户信息，用户名年龄。然后和要改的进行对比，发现age被修改了。
重新赋值并写入（这个地方username是唯一的）所以说不能修改用户名
此处没有更新密码，因为密码updateuser函数获取的密码都是***（用了get方式为了不让密码显示html里面写的是***）
如果此处判断密码是否有修改就出问题了（因为我传的是***肯定和之前不一样了）。
如果我不想修改密码呢，所以这个地方没有针对密码进行修改。正常应该写个专门修改密码的函数
'''
@app.route('/changeuser/',methods=['POST'])
def changeuser():
	updateuser = request.form.get('user')
	updateage = request.form.get('age')
	updatepassword = request.form.get('password')

	user_list=user.get_user()

	for users in user_list:
		if users['username'] == updateuser:
			if users['age'] != updateage:
				user_list[user_list.index(users)]['age'] = updateage
				user.add_user(json.dumps(user_list))
				return redirect('/users/')
			else:
				return redirect('/users/')

if __name__ == '__main__':
	app.run(host='0.0.0.0',port=8888,debug=True)


'''
不错，自己代码里面多写注释
改进点
1. app中的代码逻辑越简单越好，只控制逻辑，不控制真实对数据的改写
	将对用户的增删改查，验证等都写在user模块，由user模块提供统一的接口
	如果后续要调整逻辑只需要调整user模块
'''
