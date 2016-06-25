#encoding: utf-8
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

import os
from flask import Flask             #导入Flask类
from flask import render_template   #导入模板加载函数
from flask import request           #导入请求对象
from flask import redirect          #导入跳转函数
from flask import session
from flask import flash

import json

from functools import wraps

import userdb as user
#import user                         #导入user模块

app = Flask(__name__)               #创建Flask对象

#app.secret_key = os.urandom(32)
app.secret_key = 'sadsadasdsa'

def login_required(func):
    @wraps(func)
    def wrapper(*args,**kwargs):
        if session.get('user') is None:
            return redirect('/')
        rt = func(*args,**kwargs)
        return rt
    return wrapper



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
        session['user'] = {'username' : username}          #登录成功，放session
        return redirect('/users/')
    else:
        return render_template('login.html', username=username, error='用户名或密码错误')

'''退出登录'''
@app.route('/logout/')
def logout():
    session.clear()
    print session
    return redirect('/')

'''
显示用户列表
'''
@app.route('/users/')
def users():
    print session
    if session.get('user') is None:            #每次请求检查session
        return redirect('/')

    users = user.get_users()
    return render_template('users.html', users=users)

'''
用户添加
'''
#@app.route('/user/add/', methods=['POST'])
@app.route('/user/create-user/', methods=['POST'])
@login_required
def create_user():
    username = request.form.get('user-username', '')
    password = request.form.get('user-password', '')
    age = request.form.get('user-userage', '')

    _is_ok, _error = user.validate_add_user(username, password, age)    #检查用户信息

    if _is_ok:
        user.add_user(username, password, age)                          #添加用户信息
    return json.dumps({'is_ok': _is_ok, "error": _error})

'''
删除用户
'''
@app.route('/user/delete-user/', methods=['POST'])
@login_required
def delete_user():
    uid = request.form.get('userid', '')
    print uid
    _is_ok, _error = user.validate_delete_user(uid)    #检查用户信息

    if _is_ok:
        user.delete_user(uid)                          #删除用户
    return json.dumps({'is_ok': _is_ok, "error": _error})

'''
更新用户密码
'''
@app.route('/user/charge-password/', methods=['POST'])
@login_required
def charge_user_password():
    uid = request.form.get('userid', '')
    manager_password = request.form.get('password-manager-password', '')
    user_password = request.form.get('password-user-password', '')

    _is_ok, _error = user.validate_charge_user_password(uid,user_password,session['user']['username'],manager_password)

    if _is_ok:
        user.charge_user_password(uid,user_password)
    return json.dumps({'is_ok':_is_ok,"error":_error})

'''
更新用户年龄
'''
@app.route('/user/modify-age/', methods=['POST'])
@login_required
def charge_user_age():
    uid = request.form.get('userid', '')
    user_age = request.form.get('user-age', '')

    _is_ok, _error = user.validate_update_user_age(uid,user_age)

    if _is_ok:
        user.update_user( user_age, uid)
    return json.dumps({'is_ok':_is_ok,"error":_error})


'''日志页面'''
@app.route('/logs/',methods=['POST','GET'])
@login_required
def logs():
    if request.method == 'POST':
        _file = request.files['re_file']
        _file.save('www_access_20140823.log')
    topn = request.args.get('topn')
    topn = int(topn) if str(topn).isdigit() else 10
    rt_list = user.accesslog(topn=topn)
    print rt_list

    return render_template('logs.html', rt_list=rt_list, title='access_log')

'''添加日志页面'''
@app.route('/upload_log/',methods=['POST','GET'])
@login_required
def upload_log():
    return render_template('upload_log.html')

@app.route('/test/', methods=['POST', 'GET'])
def test():
    return render_template('test.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=8080, debug=True) #启动app
