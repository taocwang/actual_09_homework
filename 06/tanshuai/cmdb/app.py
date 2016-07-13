#!/usr/bin/env python
# -*- coding: utf-8 -*-
from flask import Flask, render_template, request, redirect, session, flash
from functools import wraps
import log2db
import user
import os

# flask框架定义
app = Flask(__name__)
# session_key定义
app.secret_key = os.urandom(32)

# 登录验证装饰器（登录页面加入验证会死循环）
def login_required(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        if session.get('user') is None:
            return redirect('/')
        rt = func(*args, **kwargs)
        return rt
    return wrapper

# 根目录
@app.route('/')
def index():
    if session:
        return redirect('/users/')
    else:
        return render_template('login.html')

# 登录页面
@app.route('/login/', methods=['POST', 'GET'])
def login():
    params = request.args if request.method == 'GET' else request.form
    username = params.get('username')
    password = params.get('password')
    if user.validate_login(username, password):
        print '登录成功'
        session['user'] = {'username': username}
        return redirect('/users/')
    else:
        return render_template('login.html', username=username, error=u'用户名或密码错误')

# 登出页面
@app.route('/user/logout/')
def logout():
    session.clear()
    return redirect('/users')

# 用户信息显示
@app.route('/users/')
@login_required
def users():
    return render_template('users.html', user_list=user.get_users())

# 添加用户
@app.route('/user/create/')
@login_required
def create():
    return render_template('adduser.html')

@app.route('/user/add', methods=['POST', 'GET'])
@login_required
def addUser():
    params = request.args if request.method == 'GET' else request.form
    username = params.get('username', '')
    password = params.get('password', '')
    age = params.get('age', '')
    # 检查用户信息
    if user.validate_find(username):
        return render_template('adduser.html', error=u'用户名存在，请重新输入')
    elif not username or not password or not age:
        return render_template('adduser.html', error=u'(用户名、年龄、密码)不能为空，请重新输入')
    else:
        if user.add_users(username=username, age=age, password=password):
            flash(u'添加用户信息成功')
            return redirect('/users/')
        else:
            return '用户添加失败！'

# 更新用户
@app.route('/user/find/', methods=['GET'])
@login_required
def finds():
    uid = request.args.get('uid', '')
    userinfo = request.args.get('userinfo', '')
    return render_template('updateUser.html', userinfo=userinfo, uid=uid)

@app.route('/user/update/', methods=['POST', 'GET'])
@login_required
def update():
    # 获取用户更新信息，username作为唯一标识符，且不能更新
    params = request.args if request.method == 'GET' else request.form
    username = params.get('username', '')
    password = params.get('password', '')
    age = params.get('age', '')
    uid = request.args.get('uid', '')
    userinfo = request.args.get('userinfo', '')
    # 更新操作代码块
    if user.validate_find(username):
        return render_template('updateUser.html', userinfo=userinfo, uid=uid, error=u'用户名存在，请重新输入')
    elif not username or not password or not age:
        return render_template('updateUser.html', userinfo=userinfo, uid=uid, error=u'(用户名、密码、年龄)不能为空，请重新输入')
    elif user.update_users(username=username, password=password, age=age, uid=uid):
        flash(u'更新用户信息成功')
        return redirect('/users/')
    else:
        return "用户更新失败！"

# 删除用户
@app.route('/user/delete/')
@login_required
def deleteUser():
    uid = request.args.get('uid', '')
    if user.del_users(uid):
        flash(u'删除用户信息成功')
        return redirect('/users/')
    else:
        return '用户删除失败'

# 显示日志信息
@app.route('/logs/')
@login_required
def logs():
    log_files = 'access.txt'
    topn = request.args.get('topn', 10)
    topn = int(topn) if str(topn).isdigit() else 10
    rt_list = log2db.log2db(log_files=log_files, topn=topn)  # 读取数据
    return render_template('logs.html', rt_list=rt_list, title='Top N')

if __name__ == '__main__':
    app.run(port=8088, debug=True)
