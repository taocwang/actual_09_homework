#encoding: utf-8
import sys
reload(sys)
sys.setdefaultencoding('utf-8')                     #设置命令行为utf-8

import os
import json
import time
from functools import wraps
from . import app
from flask import Flask                             #从flask包导入Flask类
from flask import render_template                   #从flask包导入render_template函数
from flask import request                           #从flask包导入request对象
from flask import redirect                          #从flask包导入redirect函数
from flask import url_for
from flask import session
from flask import flash
import assets
import userdb as user
#import user                                         #导入user模块
#import loganalysis
import loganalysisdb as loganalysis
import log2db


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
    print user.validate_login(username, password)
    if user.validate_login(username, password):
        session['user'] = {'username' : username}
        return redirect('/users/')                  #跳转到url /users/
    else:
        #登录失败
        return render_template('login.html', username=username, error='用户名或密码错误')


'''用户列表显示
'''
@app.route('/users/') #将url path=/users/的get请求交由users函数处理
@login_required
def users():
    #获取所有用户的信息
    print session
    if session.get('user') is None:
        return redirect('/')

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
    passwordrep = request.form.get('passwordrep', '')
    age = request.form.get('age', '')
    phone = request.form.get('phone', '')
    email = request.form.get('email','')
    img = request.files.get('img')
    if img:
        print img.filename
        img.save('/tmp/kk.txt')

    print request.form


    #检查用户信息
    _is_ok, _error = user.validate_add_user(username, password, age, phone, email)
    if _is_ok:
        user.add_user(username, password, age, phone, email)      #检查ok，添加用户信息
        return json.dumps({'is_ok': _is_ok, 'error':_error})                 #跳转到用户列表url_for
    else:
        #跳转到用户新建页面，回显错误信息&用户信息
        return json.dumps({'is_ok': _is_ok, 'error':_error})


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
    _phone = ''
    _email = ''
    print _user
    if _user is None:
        _error = '用户信息不存在'
    else:
        _uid = _user.get('id')
        _username = _user.get('username')
        _password = _user.get('password')
        _age = _user.get('age')
        _phone = _user.get('phone')
        _email = _user.get('email')

    return render_template('user_modify.html', error=_error, user=_user)

'''保存修改用户数据
'''
@app.route('/user/update/', methods=['POST'])           #将url path=/user/update/的post请求交由update_user函数处理
@login_required
def update_user():
    uid = request.form.get('userid', '')
    username = request.form.get('username', '')
    password = request.form.get('password', '')
    age = request.form.get('age', '')
    phone = request.form.get('phone', '')
    email = request.form.get('email', '')
    print uid,username
    #检查用户信息
    _is_ok, _error = user.validate_update_user(uid,username,password, age, phone, email)
    if _is_ok:
        user.update_user(uid, password, age, phone, email)
        return json.dumps({'is_ok': _is_ok, 'error':_error})
    else:
        return json.dumps({'is_ok': _is_ok, 'error':_error})


@app.route('/user/delete/')
@login_required
def delete_user():
    uid = request.args.get('userid', '')
    user.delete_user(uid)
    return  redirect('/users/')


@app.route('/logs/')
@login_required
def logs():
    topn = request.args.get('topn', 10)
    topn = int(topn) if str(topn).isdigit() else 10

    rt_list = loganalysis.get_topn(topn=topn)
    return render_template('logs.html', rt_list=rt_list, title='topn log')


@app.route('/user/changepass/')
@login_required
def change_pass():
    uid = request.args.get('userid', '')
    _user = user.get_user(uid)
    return render_template('change_password.html', user=_user)

@app.route('/user/change-passwd/', methods=['post'])
@login_required
def change_user_password():
    uid = request.form.get('userid')
    mpasswd = request.form.get('mgr-passwd')
    npasswd = request.form.get('user-passwd')
    _is_ok, _error = user.validate_change_user_password(uid, npasswd, session['user']['username'], mpasswd)
    if _is_ok:
        user.change_user_password(uid, npasswd)
    return json.dumps({'is_ok': _is_ok, 'error':_error})




@app.route('/logout/')
@login_required
def logout():
    session.clear()
    print session
    return redirect('/')


@app.route('/uploadlogs/', methods=['POST'])
@login_required
def uploadlogs():
    _file = request.files.get('logfile')
    if _file:
        _filepath = 'temp/%s' % time.time()
        _file.save(_filepath)
        log2db.log2db(_filepath)
    return redirect('/logs/')

@app.route('/test/', methods=['POST', 'GET'])
def test():
    print request.args
    print request.form
    print request.files
    print request.headers
    return render_template('test.html')

'''资产列表显示
'''

@app.route('/assets/', methods=['POST','GET'])
@login_required
def assets_list():
    # 获取所有资产的信息
    _assets = assets.get_list()
    return render_template('assets.html', assets=_assets)

@app.route('/assets/add/', methods=['POST','GET'])
@login_required
def add_assets():
    idcs =  [('1', '北京-亦庄'), ('2', '北京-酒仙桥'), ('3', '北京-西单'), ('4', '北京-东单')]
    return render_template('assets_create.html',idcs=idcs)

@app.route('/assets/create/', methods=['POST', 'GET'])
@login_required
def assets_create():
    pa = request.form.get
    sn = pa('sn')
    ip = pa('ip')
    hostname = pa('hostname')
    os = pa('os')
    purchase_date = pa('purchase_date')
    warranty = pa('warranty')
    vendor = pa('vendor')
    model = pa('model')
    idc_id = pa('idc')
    admin = pa('admin')
    business = pa('business')
    cpu = pa('cpu')
    mem = pa('mem')
    disk = pa('disk')


    _is_ok, _error = assets.validate_create(sn, ip, hostname, os, purchase_date, warranty, vendor, model, idc_id, admin, business, cpu, mem, disk)
    if _is_ok:
        assets.create(sn, ip, hostname, os, purchase_date, warranty, vendor, model, idc_id, admin, business, cpu, mem, disk)
        return json.dumps({'is_ok':'创建成功'})
    else:
        return json.dumps({'error': "\n".join(_error['error'])})

        # if __name__ == '__main__':
#     app.run(host='0.0.0.0', port=9001, debug=True)


@app.route('/assets/modify/', methods=['POST', 'GET'])
@login_required
def assets_modify():
    sn = request.args.get('sn')
    _cnt, _assets = assets.get_by_id(sn)
    idcs = [('1', '北京-亦庄'), ('2', '北京-酒仙桥'), ('3', '北京-西单'), ('4', '北京-东单')]
    return render_template('assets_modify.html', assets=_assets, idcs=idcs)

@app.route('/assets/update/', methods=['POST','GET'])
@login_required
def assets_update():
    pa = request.form.get
    sn = pa('sn')
    ip = pa('ip')
    hostname = pa('hostname')
    os = pa('os')
    purchase_date = pa('purchase_date')
    warranty = pa('warranty')
    vendor = pa('vendor')
    model = pa('model')
    idc_id = pa('idc')
    admin = pa('admin')
    business = pa('business')
    cpu = pa('cpu')
    mem = pa('mem')
    disk = pa('disk')
    _is_ok, _error = assets.validate_update(ip, hostname, os, purchase_date, warranty, vendor, model, idc_id, admin, business, cpu, mem,
                      disk)
    if _is_ok:
        assets.update(ip, hostname, os, purchase_date, warranty, vendor, model, idc_id, admin, business, cpu, mem,
                      disk, sn)
        return json.dumps({'is_ok': '修改成功'})
    else:
        return json.dumps({'error': "\n".join(_error['error'])})


@app.route('/assets/delete/', methods=['POST','GET'])
@login_required
def assets_delete():
    aid = request.args.get('sn','')
    print aid
    _is_ok, _rt_list = assets.delete(aid)
    if _is_ok:
        return redirect('/assets/')
    else:
        return json.dumps({'error': '删除失败'})
