#!/usr/bin/env python
# -*- coding: utf-8 -*-
from flask import Flask, render_template, request, redirect, session, flash, url_for
from functools import wraps
import services2db
import log2db
import user
import json
import time
import sys
import os

reload(sys)
sys.setdefaultencoding('gb18030')

# flask框架定义
app = Flask(__name__)
# session_key定义
# app.secret_key = os.urandom(32)
app.secret_key = '\xabv\xb2\x00\xb8\xd3\xde\xac\x84=\xf8*\xaa\xad\xf5%\x83\xd0\x08P]pG\x18\xa9:\xf8pm\x8f\x18\xb1'

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
    username = params.get('username', '')
    password = params.get('password', '')
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
@app.route('/user/adder/', methods=['POST'])
def add_user():
    params = request.args if request.method == 'GET' else request.form
    username = params.get('username', '')
    password = params.get('password', '')
    age = params.get('age', '')
    # 检查用户信息
    _is_ok, _error = user.validate_add_user(username, password, age)
    if _is_ok:
        user.add_users(username=username, age=age, password=password)
    return json.dumps({'is_ok': _is_ok, 'error': _error})

# 更新用户
@app.route('/user/update/', methods=['POST'])
def update_user():
    uid = request.form.get('userid', '')
    userinfo_password = request.form.get('userinfo-password', '')
    manages_password = request.form.get('manager-password', '')
    userinfo_age = request.form.get('userinfo-age', '')
    _is_ok, _error = user.validate_update_user(uid, session['user']['username'], manages_password, userinfo_password, userinfo_age)
    if _is_ok:
        user.update_users(uid, userinfo_password, userinfo_age)
    return json.dumps({'is_ok': _is_ok, 'error': _error})


# 删除用户
@app.route('/user/delete/')
@login_required
def delete_user():
    uid = request.args.get('uid', '')
    if user.del_users(uid):
        return redirect('/users/')
    else:
        return '用户删除失败'

# 显示日志信息
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


# 显示域名管理信息
@app.route('/services/', methods=['POST', 'GET'])
@login_required
def service_manage():
    params = request.args if request.method == 'GET' else request.form
    _url = params.get('url', 'Null')
    _username = params.get('username', 'Null')
    _password = params.get('password', 'Null')
    _func = params.get('func', 'Null')
    # 添加域名管理信息
    if _url != 'Null':
        if services2db.add_service(_url, _username, _password, _func):
            return redirect('/services/')
        else:
            return '添加信息失败！'
    # 查询域名管理信息
    else:
        service_list = services2db.get_service()
        return render_template('services.html', service_list=service_list)

# 更新域名管理信息
@app.route('/services/update/', methods=['POST'])
def update_service():
    params = request.args if request.method == 'GET' else request.form
    _id = params.get('id', '')
    _url = params.get('url', '')
    _username = params.get('username', '')
    _password = params.get('password', '')
    _func = params.get('func', '')
    _is_ok = services2db.update_service(_url, _username, _password, _func, _id)
    return json.dumps({'is_ok': _is_ok})

# 删除域名管理信息
@app.route('/services/del/')
@login_required
def serviceDel():
    uid = request.args.get('id', '')
    if services2db.servicedel(uid):
        return redirect('/services/')
    else:
        return '域名管理信息删除失败！'


if __name__ == '__main__':
    app.run(port=8088, debug=True)
