#encoding: utf-8
import sys
reload(sys)
sys.setdefaultencoding('utf-8')                     #设置命令行为utf-8

import os
import time
import json
from functools import wraps

from flask import Flask                             #从flask包导入Flask类
from flask import render_template                   #从flask包导入render_template函数
from flask import request                           #从flask包导入request对象
from flask import redirect                          #从flask包导入redirect函数
from flask import url_for
from flask import session
from flask import flash

from user import app                                # user模块下的app变量(Flask对象)

import userdb as user
import loganalysisdb as loganalysis
import log2db
import asset

def login_required(func):

    @wraps(func)
    def wrapper(*args, **kwargs):
        if session.get('user') is None:
            return redirect('/')

        rt = func(*args, **kwargs)
        return rt

    return wrapper


'''打开用户登录页面
'''
@app.route('/')                                     #将url path=/的请求交由index函数处理
def index():
    return render_template('login.html')            #加载login.html模板，并返回页面内容


'''用户登录信息检查
'''
@app.route('/login/', methods=["POST"])             #将url path=/login/的post请求交由login函数处理
def login():
    username = request.form.get('username', '')     #接收用户提交的数据
    password = request.form.get('password', '')

    #需要验证用户名密码是否正确
    print username, password
    if user.validate_login(username, password):
        session['user'] = {'username' : username}
        return redirect('/users/')                  #跳转到url /users/
    else:
        #登录失败
        return render_template('login.html', username=username, error='用户名或密码错误')


'''用户列表显示
'''
@app.route('/users/')                               #将url path=/users/的get请求交由users函数处理
@login_required
def users():
    #获取所有用户的信息
    _users = user.get_users()
    return render_template('users.html', users=_users, username=session.get('user').get('username'), msg=request.args.get('msg', ''))            #加载渲染users.html模板

'''跳转到新建用户信息输入的页面
'''
@app.route('/user/create/')                         #将url path=/user/create/的get请求交由create_user处理
@login_required
def create_user():
    return render_template('user_create.html')      #加载渲染user_create.html


'''存储新建用户的信息
'''
@app.route('/user/add/', methods=['POST'])          #将url path=/user/add的post请求交由add_user处理
@login_required
def add_user():
    username = request.form.get('username', '')
    password = request.form.get('password', '')
    age = request.form.get('age', '')

    #检查用户信息
    _is_ok, _error = user.validate_add_user(username, password, age)
    if _is_ok:
        user.add_user(username, password, age)      #检查ok，添加用户信息
    return json.dumps({'is_ok':_is_ok, "error":_error})

    '''
    if _is_ok:
        user.add_user(username, password, age)      #检查ok，添加用户信息
        return redirect(url_for('users', msg='新建成功'))                  #跳转到用户列表url_for
    else:
        #跳转到用户新建页面，回显错误信息&用户信息
        return render_template('user_create.html', \
                                error=_error, username=username, \
                                password=password, age=age)
    '''

'''打开用户信息修改页面
'''
@app.route('/user/modify/')                          #将url path=/user/modify/的歌特请求交由modify_user函数处理
@login_required
def modify_user():
    uid = request.args.get('id', '')
    _user = user.get_user(uid)
    _error = ''
    _uid = ''
    _username = ''
    _password = ''
    _age = ''
    if _user is None:
        _error = '用户信息不存在'
    else:
        _uid = _user.get('id')
        _username = _user.get('username')
        _password = _user.get('password')
        _age = _user.get('age')

    return render_template('user_modify.html', error=_error, password=_password, age=_age, username=_username, uid=_uid)

'''保存修改用户数据
'''
@app.route('/user/update/', methods=['POST'])           #将url path=/user/update/的post请求交由update_user函数处理
@login_required
def update_user():
    uid = request.form.get('id', '')
    username = request.form.get('username', '')
    password = request.form.get('password', '')
    age = request.form.get('age', '')

    #检查用户信息
    _is_ok, _error = user.validate_update_user(uid, username, password, age)

    if _is_ok:
        user.update_user(uid, username, password, age)
    return json.dumps({'is_ok':_is_ok, "error":_error})

    '''
    if _is_ok:
        user.update_user(uid, username, password, age)
        flash('修改用户信息成功')
        return redirect('/users/')
    else:
        return render_template('user_modify.html', error=_error, username=username, password=password, age=age, uid=uid)
    '''

@app.route('/user/delete/')
@login_required
def delete_user():
    uid = request.args.get('id', '')
    user.delete_user(uid)
    flash('删除用户信息成功')
    return redirect('/users/')


@app.route('/logs/')
@login_required
def logs():
    topn = request.args.get('topn', 10)
    topn = int(topn) if str(topn).isdigit() else 10

    rt_list = loganalysis.get_topn(topn=topn)
    return render_template('logs.html', rt_list=rt_list, title='topn log')

@app.route('/logout/')
@login_required
def logout():
    session.clear()
    print session
    return redirect('/')

@app.route('/uploadlogs/', methods=['POST'])
def uploadlogs():
    _file = request.files.get('logfile')
    if _file:
        _filepath = 'temp/%s' % time.time()
        _file.save(_filepath)
        log2db.log2db(_filepath)
    return redirect('/logs/')


@app.route('/user/charge-password/', methods=['POST'])
@login_required
def charge_user_password():
    uid = request.form.get('userid')
    manager_password = request.form.get('manager-password')
    user_password = request.form.get('user-password')
    _is_ok, _error = user.validate_charge_user_password(uid, user_password, \
                                    session['user']['username'], manager_password)
    if _is_ok:
        user.charge_user_password(uid, user_password)

    return json.dumps({'is_ok':_is_ok, "error":_error})

'''资产列表显示
'''
@app.route('/assets/')
@login_required
def assets():
    _assets = asset.get_list()
    return render_template('assets.html', assets=_assets)

@app.route('/asset/create/', methods=['POST', 'GET'])
@login_required
def create_asset():
    return render_template('asset_create.html', idcs=asset.get_idc_list())

@app.route('/asset/add/', methods=['POST'])
def add_asset():
    _is_ok, _errors = asset.validate_create(request.form)
    if _is_ok:
        asset.create(request.form)
    return json.dumps({'is_ok' : _is_ok, 'errors' : _errors, 'success' : '添加成功'})


@app.route('/asset/modify/')
@login_required
def modify_asset():
    _id = request.args.get('id', '')
    _asset = asset.get_by_id(_id)
    return render_template('asset_modify.html', asset=_asset, idcs=asset.get_idc_list())


@app.route('/asset/update/', methods=['POST'])
@login_required
def update_asset():
    _is_ok, _errors = asset.validate_update(request.form)
    if _is_ok:
        asset.update(request.form)
    return json.dumps({'is_ok' : _is_ok, 'errors' : _errors, 'success' : '更新成功'})


@app.route('/asset/delete/')
@login_required
def delete_asset():
    _id = request.args.get('id', '')
    asset.delete(_id)
    return redirect('/assets/')


@app.route('/test/', methods=['POST', 'GET'])
def test():
    print request.args
    print request.form
    print request.files
    print request.headers
    return render_template('test.html')
