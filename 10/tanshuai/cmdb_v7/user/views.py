#!/usr/bin/env python
# -*- coding: utf-8 -*-
from flask import render_template, request, redirect, session, flash, url_for
from functools import wraps
from user import app
import json
import time
import sys
from models import User, Asset, Log2db, Service

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
    _username = request.form.get('username', '')
    _password = request.form.get('password', '')
    _user = User(id=None, username=_username, password=_password, age=None)
    if _user.validate_login():
        session['user'] = _user.validate_login()
        return redirect('/users/')
    else:
        return render_template('login.html', username=_username, error=u'用户名或密码错误')

# 登出页面
@app.route('/user/logout/')
def logout():
    session.clear()
    return redirect('/')

# 用户信息显示
@app.route('/users/')
@login_required
def user_list():
    return render_template('users.html', user_list=User.get_list())


# 返回添加用户模版给dialog页面
@app.route('/user/adder/', methods=['POST', 'GET'])
@login_required
def user_create():
    return render_template('user_create.html')

# 添加用户
@app.route('/user/add/', methods=['POST'])
def user_add():
    _username = request.form.get('username', '')
    _password = request.form.get('password', '')
    _age = request.form.get('age', '')
    # 检查用户信息
    _user = User(id=None, username=_username, password=_password, age=_age)
    _is_ok, _error = _user.validate_add()
    _status = None
    _info = None
    if _is_ok:
        if _user.save():
            _status, _info = True, '添加用户成功！'
        else:
            _status, _info = False, '添加用户失败！'
    return json.dumps({'is_ok': _is_ok, 'status': _status, 'info': _info, 'error': _error})

# 返回更新用户模版给dialog页面
@app.route('/user/update/', methods=['POST', 'GET'])
@login_required
def user_update():
    _id = request.args.get('id', '')
    _name = request.args.get('name', '')
    return render_template('user_update.html', uid=_id, username=_name)

# 更新用户
@app.route('/user/upd/', methods=['POST', 'GET'])
def user_upd():
    _id = request.form.get('id', '')
    _mpassword = request.form.get('mpassword', '')
    _age = request.form.get('age', '')
    _user = User(id=_id, username=session['user']['username'], password=_mpassword, age=_age)
    _is_ok, _error = _user.validate_update()
    _status = None
    _info = None
    if _is_ok:
        if _user.update():
            _status, _info = True, '更新用户成功！'
        else:
            _status, _info = False, '更新用户失败！'
    return json.dumps({'is_ok': _is_ok, 'status': _status, 'info': _info, 'error': _error})

# 删除用户
@app.route('/user/delete/')
@login_required
def delete_user():
    uid = request.args.get('uid', '')
    _user = User(id=uid, username=None, password=None, age=None)
    if _user.delete():
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
        _logs = Log2db()
        if _logs.log_execute(log_files=log_files):
            return redirect('/logs/')
        else:
            return '日志写入数据库失败！'
    else:
        topn = request.form.get('topn', 10)
        topn = int(topn) if str(topn).isdigit() else 10
        _logs = Log2db()
        rt_list = _logs.log_fetch(topn=topn)
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
    _service = Service()
    # 添加域名管理信息
    if _url != 'Null':
        if _service.add_service(_url, _username, _password, _func):
            return redirect('/services/')
        else:
            return '添加信息失败！'
    # 查询域名管理信息
    else:
        service_list = _service.get_list()
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
    _service = Service()
    _is_ok = _service.update_service(_url, _username, _password, _func, _id)
    return json.dumps({'is_ok': _is_ok})

# 删除域名管理信息
@app.route('/services/del/')
@login_required
def serviceDel():
    uid = request.args.get('id', '')
    _service = Service()
    if _service.del_service(uid):
        return redirect('/services/')
    else:
        return '域名管理信息删除失败！'


# 资产信息显示
@app.route('/assets/')
@login_required
def asset_list():
    _asset_list = []
    for i in Asset.get_list():
        _rt_list = Asset.get_asset_by_id(i.get('idc_id'))
        i['idc_id'] = _rt_list[0][1]
        _asset_list.append(i)
    return render_template('assets.html', asset_list=_asset_list)

# 返回新建资产模版给dialog页面
@app.route('/asset/create/', methods=['POST', 'GET'])
@login_required
def asset_create():
    # print Asset.get_idc_list()
    return render_template('asset_create.html', idcs=Asset.get_idc_list())

# 添加资产信息
@app.route('/asset/add/', methods=['POST', 'GET'])
@login_required
def asset_add():
    lists = ['sn','ip','hostname','idc_id','purchase_date','warranty','vendor','model','admin','business','os','cpu','ram','disk']
    asset_dict = {}
    for i in lists:
        asset_dict['_'+i] = request.form.get(i, '')
    # 检查资产信息
    _is_ok, _error = Asset.validate_create(asset_dict)
    _status = None
    _info = None
    if _is_ok:
        if Asset.create(asset_dict):
            _status, _info = True, '添加资产成功！'
        else:
            _status, _info = False, '添加资产失败！'
    return json.dumps({'is_ok': _is_ok, 'status': _status, 'info': _info, 'error': _error})


# 返回更新资产模版给dialog页面
@app.route('/asset/update/', methods=['POST', 'GET'])
@login_required
def asset_update():
    _id = request.args.get('id', '')
    _asset_list = []
    for i in Asset.get_list():
        if i.get('id') == int(_id):
            _asset_list.append(i)
    return render_template('asset_update.html', asset_list=_asset_list, idcs=Asset.get_idc_list())

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
    _is_ok, _error = Asset.validate_update(asset_dict)
    _info = None
    _status = None
    if _is_ok:
        if Asset.update(asset_dict, _id):
            _status, _info = True, '更新资产成功！'
        else:
            _status, _info = False, '更新资产失败！'
    return json.dumps({'is_ok': _is_ok, 'status': _status, 'info': _info, 'error': _error})


# 删除资产信息
@app.route('/asset/delete/')
@login_required
def asset_del():
    uid = request.args.get('id', '')
    if Asset.delete(uid):
        return redirect('/assets/')
    else:
        return '资产删除失败！'