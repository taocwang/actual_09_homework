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

from functools import wraps

import userdb as user
import r2
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
显示用户添加表单
'''
@app.route('/user/create/')
@login_required
def create_user():
    return render_template('user_create.html')

'''
用户添加
'''
@app.route('/user/add/', methods=['POST'])
@login_required
def add_user():
    username = request.form.get('username', '')
    password = request.form.get('password', '')
    age = request.form.get('age', '')
    gender = request.form.get('gender','1')
    hobby = request.form.getlist('hobby')
    img = request.files.get('img')
    if img:
        print img.filename
        img.save('./test.img')
    print request.form
    print gender
    print hobby

    _is_ok, _error = user.validate_add_user(username, password, age)    #检查用户信息

    if _is_ok:
        user.add_user(username, password, age)                          #添加用户信息
        flash('添加用户信息成功')
        return redirect('/users/')                                      #跳转到用户列表
    else:
        return render_template('user_create.html', username=username, password=password, age=age, error=_error)


'''
显示修改用户表单
'''
@app.route('/user/modify/')
@login_required
def modify_user():
    id = request.args.get('id', '')
    _user = user.get_user_id(id)
    _user = _user[0]
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

    return render_template('user_modify.html', error=_error, username=_username, password=_password, age=_age, id=id)


'''
更新用户信息
'''
@app.route('/user/update/', methods=['POST'])
@login_required
def update_user():
    username = request.form.get('username', '')
    password = request.form.get('password', '')
    age = request.form.get('age', '')
    id = request.form.get('id','')
    _is_ok, _error = user.validate_update_user(username, password, age,id)

    if _is_ok:
        user.update_user(username, password, age, id)
        flash('更新用户信息成功')
        return redirect('/users/')
    else:
        return render_template('user_modify.html', error=_error, username=username, password=password, age=age, id=id)

'''
删除用户
'''
@app.route('/user/delete/')
@login_required
def delete_user():
    #username = request.args.get('username', '')
    id = request.args.get('id', '')
    #user.delete_user(username)
    user.delete_user(id)
    flash('删除用户信息成功')
    return redirect('/users/')


'''日志页面'''
@app.route('/logs/',methods=['POST','GET'])
@login_required
def logs():
    if request.method == 'POST':
        _file = request.files['re_file']
        _file.save('www_access_20140823.log')
    topn = request.args.get('topn')
    topn = int(topn) if str(topn).isdigit() else 10
    logfile = './www_access_20140823.log'
    rt_list = r2.get_topn(topn=topn,logfile = logfile)
    print rt_list

    return render_template('logs.html', rt_list=rt_list, title='access_log')

'''添加日志页面'''
@app.route('/upload_log/',methods=['POST','GET'])
@login_required
def upload_log():
    return render_template('upload_log.html')

@app.route('/test/', methods=['POST', 'GET'])
def test():
    print request.args
    print request.form
    print request.files
    print request.headers
    return render_template('test.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=8080, debug=True) #启动app
