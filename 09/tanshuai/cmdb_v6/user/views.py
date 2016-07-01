#!/usr/bin/env python
# -*- coding: utf-8 -*-
from flask import render_template, request, redirect, session, flash, url_for
from functools import wraps
from user import app
import services2db
import log2db
import users
import json
import time
import sys
import asset

reload(sys)
sys.setdefaultencoding('gb18030')

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
    if users.validate_login(username, password):
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
def user_list():
    return render_template('users.html', user_list=users.get_users())


# 返回添加用户模版给dialog页面
@app.route('/user/adder/', methods=['POST', 'GET'])
@login_required
def user_create():
    return render_template('user_create.html')
# 添加用户
@app.route('/user/add/', methods=['POST'])
def user_add():
    params = request.args if request.method == 'GET' else request.form
    username = params.get('username', '')
    password = params.get('password', '')
    age = params.get('age', '')
    # 检查用户信息
    _is_ok, _error = users.validate_add_user(username, password, age)
    _status = None
    if _is_ok:
        if users.add_users(username=username, age=age, password=password):
            _status = '添加用户成功！'
        else:
            _status = '添加用户失败！'
    return json.dumps({'is_ok': _is_ok, 'status': _status, 'error': _error})

# 返回更新用户模版给dialog页面
@app.route('/user/update/', methods=['POST', 'GET'])
@login_required
def user_update():
    _id = request.args.get('id', '')
    _name = request.args.get('name', '')
    # _users = []
    # for i in users.get_users():
    #     if i.get('id') == int(_id):
    #         _users.append(i)
    return render_template('user_update.html', uid=_id, username=_name)

# 更新用户
@app.route('/user/upd/', methods=['POST', 'GET'])
def user_upd():
    _id = request.form.get('id', '')
    _mpassword = request.form.get('mpassword', '')
    _upassword = request.form.get('upassword', '')
    _age = request.form.get('age', '')
    _is_ok, _error = users.validate_update_user(_id, session['user']['username'], _mpassword, _upassword, _age)
    _status = None
    if _is_ok:
        if users.update_users(_id, _upassword, _age):
            _status = '用户更新成功！'
        else:
            _status = '用户更新失败！'
    return json.dumps({'is_ok': _is_ok, 'status': _status, 'error': _error})

# 删除用户
@app.route('/user/delete/')
@login_required
def delete_user():
    uid = request.args.get('uid', '')
    if users.del_users(uid):
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


# 资产信息显示
@app.route('/assets/')
@login_required
def asset_list():
    _asset_list = []
    for i in asset.get_list():
        _rt_list = asset.get_by_id(i.get('idc_id'))
        i['idc_id'] = _rt_list[0][1]
        _asset_list.append(i)
    return render_template('assets.html', asset_list=_asset_list)

# 返回新建资产模版给dialog页面
@app.route('/asset/create/', methods=['POST', 'GET'])
@login_required
def asset_create():
    return render_template('asset_create.html', idcs=asset.get_idc())

# 添加资产信息
@app.route('/asset/add/', methods=['POST', 'GET'])
@login_required
def asset_add():
    lists = ['sn','ip','hostname','idc_id','purchase_date','warranty','vendor','model','admin','business','os','cpu','ram','disk']
    asset_dict = {}
    for i in lists:
        asset_dict['_'+i] = request.form.get(i, '')
    # 检查资产信息
    _is_ok, _error = asset.validate_create(asset_dict)
    status = None
    if _is_ok:
        if asset.create(asset_dict):
            status = '添加资产成功！'
        else:
            status = '添加资产失败！'
    return json.dumps({'is_ok': _is_ok,  'status': status, 'error': _error})

# 删除资产信息
@app.route('/asset/delete/')
@login_required
def asset_del():
    uid = request.args.get('id', '')
    if asset.delete(uid):
        return redirect('/assets/')
    else:
        return '资产删除失败！'


# 返回更新资产模版给dialog页面
@app.route('/asset/update/', methods=['POST', 'GET'])
@login_required
def asset_update():
    _id = request.args.get('id', '')
    _asset_list = []
    for i in asset.get_list():
        if i.get('id') == int(_id):
            _asset_list.append(i)
    return render_template('asset_update.html', asset_list=_asset_list, idcs=asset.get_idc())

# 更新资产信息
@app.route('/asset/upd/', methods=['POST', 'GET'])
@login_required
def asset_upd():
    _id = request.form.get('id', '')
    assets = ['sn','ip','hostname','idc_id','purchase_date','warranty','vendor','model','admin','business','os','cpu','ram','disk']
    asset_dict = {}
    for i in assets:
        asset_dict['_'+i] = request.form.get(i, '')
    # 检查资产信息
    _is_ok, _error = asset.validate_update(asset_dict)
    _status = None
    if _is_ok:
        if asset.update(asset_dict,_id):
            _status = '更新资产成功！'
        else:
            _status = '更新资产失败！'
    return json.dumps({'is_ok': _is_ok,  'status': _status, 'error': _error})