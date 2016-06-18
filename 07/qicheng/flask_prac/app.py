#!/usr/bin/env python
# -*- coding: utf-8 -*-
from flask import Flask, render_template, request, redirect, session, flash, url_for
from functools import wraps
import log2db
import user
import time
import sys
import os

reload(sys)
sys.setdefaultencoding('gb18030')

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
# 时间装饰器
def time_wrapper(func):
    @wraps(func)
    def wrapper():
        print '计时开始:%s' % func.__name__
        start = time.time()
        rt = func()
        print '计时结束:%s:%s' % (func.__name__,time.time() - start)
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
    return redirect('/')

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
    _is_ok, _error = user.validate_add_user(username, password, age)
    if _is_ok:
        user.add_users(username=username, age=age, password=password)
        flash(u'添加用户信息成功')
        return redirect('/users/')
    else:
        # 跳转到新建页面，回显错误信息
        return render_template('adduser.html', username=username, password=password, error=_error)

# 更新用户
@app.route('/user/find/', methods=['POST', 'GET'])
@login_required
def finds():
    uid = request.args.get('uid', '')
    userinfo = request.args.get('userinfo', '')
    return render_template('updateuser.html', userinfo=userinfo, uid=uid)

@app.route('/user/update/', methods=['POST', 'GET'])
@login_required
def update_user():
    # 获取用户更新信息，username作为唯一标识符，且不能更新
    params = request.args if request.method == 'GET' else request.form
    username = params.get('userinfo', '')
    password = params.get('password', '')
    age = params.get('age', '')
    uid = params.get('uid', '')
    # 更新操作代码块
    _is_ok, _error = user.validate_update_user(username, password, age)
    if _is_ok:
        user.update_users(username=username, password=password, age=age, uid=uid)
        flash(u'更新用户信息成功')
        return redirect('/users/')
    else:
        return render_template('updateuser.html', userinfo=username, uid=uid, error=_error)

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

# 显示日志信息&上传日志并入库
@app.route('/logs/', methods=['POST', 'GET'])
@time_wrapper
@login_required
def logs():
    files = request.files.get('files')
    if files:
        # print files.filename
        files.save('./access.txt')
        log_files = 'access.txt'
        if log2db.log2db(log_files=log_files, fetch=False):
            return redirect('/logs/')
        else:
            return '日志写入数据库失败！'
    else:
        topn = request.form.get('topn', 10)
        topn = int(topn) if str(topn).isdigit() else 10
        rt_list = log2db.log2db(topn=topn)  # 读取数据
        return render_template('logs.html', rt_list=rt_list)

if __name__ == '__main__':
    app.run(port=8088, debug=True)
