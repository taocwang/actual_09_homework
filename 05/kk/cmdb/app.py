#encoding: utf-8
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

from flask import Flask             #导入Flask类
from flask import render_template   #导入模板加载函数
from flask import request           #导入请求对象
from flask import redirect          #导入跳转函数

import user                         #导入user模块

app = Flask(__name__)               #创建Flask对象


'''
接收path=/的url, 加载登录页面
'''
@app.route('/')                     #绑定处理url path = /的函数为index
def index():
    return render_template('login.html')

'''
接收path=/login/的url, 进行用户密码的验证
'''
@app.route('/login/', methods=['POST'])               #绑定处理url path = /login/的函数为login
def login():
    username = request.form.get('username', '')
    password = request.form.get('password', '')
    if user.validate_login(username, password):
        return redirect('/users/')
    else:
        return render_template('login.html', username=username, error='用户名或密码错误')

'''
显示用户列表
'''
@app.route('/users/')
def users():
    users = user.get_users()
    return render_template('users.html', users=users)


'''
显示用户添加表单
'''
@app.route('/user/create/')
def create_user():
    return render_template('user_create.html')

'''
用户添加
'''
@app.route('/user/add/', methods=['POST'])
def add_user():
    username = request.form.get('username', '')
    password = request.form.get('password', '')
    age = request.form.get('age', '')

    _is_ok, _error = user.validate_add_user(username, password, age)    #检查用户信息

    if _is_ok:
        user.add_user(username, password, age)                          #添加用户信息
        return redirect('/users/')                                      #跳转到用户列表
    else:
        return render_template('user_create.html', username=username, password=password, age=age, error=_error)


'''
删除用户
'''
@app.route('/user/delete/')
def delete_user():
    username = request.args.get('username', '')
    user.delete_user(username)
    return redirect('/users/')


'''
显示修改用户表单
'''
@app.route('/user/modify/')
def modify_user():
    username = request.args.get('username', '')
    _user = user.get_user(username)
    _error = ''
    _username = ''
    _password = ''
    _age = ''
    if _user is None:
        _error = '用户信息不存在'
    else:
        _username = _user.get('username')
        _password = _user.get('password')
        _age = _user.get('age')

    return render_template('user_modify.html', error=_error, username=_username, password=_password, age=_age)

'''
更新用户信息
'''
@app.route('/user/update/', methods=['POSt'])
def update_user():
    username = request.form.get('username', '')
    password = request.form.get('password', '')
    age = request.form.get('age', '')

    _is_ok, _error = user.validate_update_user(username, password, age)

    if _is_ok:
        user.update_user(username, password, age)
        return redirect('/users/')
    else:
        return render_template('user_modify.html', error=_error, username=username, password=password, age=age)


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True) #启动app
