#encoding:utf-8
import os
import sys

from flask import Flask,render_template,request,redirect,session,url_for,flash
from flask.ext.bootstrap import Bootstrap
from flask.ext.moment import Moment

from logs import cretae_log
from modules import user
from datetime import datetime

#
reload(sys)
sys.setdefaultencoding('utf8')
#解决字符串默认为ASCII编码的问题,导致输出中文为乱码

app = Flask(__name__)
app.secret_key = os.urandom(32)
# app.secret_key = 'asdasd2342tdasfdasfasdasds'

@app.route('/')
def index():
    return render_template('login.html')

@app.route('/login/',methods=['POST','GET'])
def login():
    params = request.args if request.method == 'GET' else request.form
    username = params.get('username','')
    password = params.get('password','')
    if user.validate_login(username, password):
        session['username'] = {'username': username}
        return redirect('/user/')
    else:
        return render_template('login.html',username=username,error='用户名或密码错误')

'''
用户列表
'''
@app.route('/user/')
@user.login_check
def users():
    return render_template('users.html', user_list=user.get_user())

'''
用户添加
'''
@app.route('/user/useradd/',methods=['POST','GET'])
@user.login_check
def users_add():
    params = request.args if request.method == 'GET' else request.form
    if not params:
        return render_template('user_add.html')
    username = params.get('username')
    password = params.get('password')
    age = params.get('age')
    telphone = params.get('telphone')
    email = params.get('email')
    if user.user_add(params):
        flash("用户%s添加成功" % username)
        return redirect('/user/')
    return render_template('user_add.html',error='用户名已存在',username=username,password=password,age=age,telphone=telphone,email=email)

'''
用户删除
'''
@app.route('/user/userdel/',methods=['POST','GET'])
@user.login_check
def user_del():
    params = request.args if request.method == 'GET' else request.form
    id = params.get('id')
    if user.user_del(int(id)):
        flash("用户删除成功")
        return redirect('/user/')
    return render_template('users.html',error='删除失败')

'''
用户更新
'''
@app.route('/user/userupdate/',methods=['POST','GET'])
@user.login_check
def user_update():
    params = request.args if request.method == 'GET' else request.form
    id = params.get('id')
    if id:
        users = user.get_alone_user(int(id))
        username = users.get('username')
        age = users.get('age')
        telphone = users.get('telphone')
        email = users.get('email')
        return render_template('user_update.html', username=username, age=age, telphone=telphone, email=email)
    if user.user_update(params):
        flash("用户更新成功")
        return redirect('/user/')
    return render_template('user_update.html',error='更新失败')

'''
登出用户
'''
@app.route('/logout/')
def logout():
    session.clear()
    return redirect('/')

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=9000,debug=True)

