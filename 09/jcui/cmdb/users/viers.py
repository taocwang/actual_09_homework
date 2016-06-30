#encoding:utf-8
import json
import os
import sys
import random
import string

import time
from flask import Flask,render_template,request,redirect,session, flash ,jsonify
from . import app         #user模块下的变量,在__init__.py  中定义
from modules import user,logs
from modules import assets


#
reload(sys)
sys.setdefaultencoding('utf8')
#解决字符串默认为ASCII编码的问题,导致输出中文为乱码


@app.route('/')
def index():
    return render_template('login.html')

@app.route('/login/',methods=['POST','GET'])
def login():
    params = request.args if request.method == 'GET' else request.form
    username = params.get('username','')
    password = params.get('password','')
    if user.validate_login(username, password):
        session['username'] = {'username': username}
        return redirect('/user/')
    else:
        return render_template('login.html',username=username,error='用户名或密码错误')

'''
a
用户列表
'''
@app.route('/user/')
@user.login_check
def users():
    return render_template('user.html', user_list=user.get_user())

'''
用户添加
'''
@app.route('/user/useradd/',methods=['POST','GET'])
@user.login_check
def users_add():
    params = request.args if request.method == 'GET' else request.form
    if not params:
        return render_template('useradd.html')
    username = params.get('username')
    password = params.get('password')
    gender = params.get('gender')
    hobby = params.getlist('hobby')
    department = params.get('department')
    filename = request.files.get('files')
    if filename:
        print filename.filename
        filename.save('/tmp/aa.txt')
    age = params.get('age')
    telphone = params.get('telphone')
    email = params.get('email')
    if user.user_add(params):
        flash("用户%s添加成功" % username)
        return redirect('/user/')
    else:
        error = '用户名已存在'
    return render_template('useradd.html',error=error,username=username,password=password,age=age,telphone=telphone,email=email)

'''
用户删除
'''
@app.route('/user/userdel/',methods=['POST','GET'])
@user.login_check
def user_del():
    params = request.args if request.method == 'GET' else request.form
    id = params.get('id')
    username = params.get('username')
    if user.user_del(int(id), username):
        flash("用户删除成功")
        return redirect('/user/')
    return render_template('user.html',error='删除失败')

'''
用户更新
'''
@app.route('/user/userupdate/',methods=['POST','GET'])
@user.login_check
def user_update():
    params = request.args if request.method == 'GET' else request.form
    _is_ok, _error = user.user_update(params)
    return jsonify({'is_ok': _is_ok, 'error': _error})

# @app.route('/user/userupdate/',methods=['POST','GET'])
# @user.login_check
# def user_update():
#     params = request.args if request.method == 'GET' else request.form
#     id = params.get('id')
#     if request.method == 'GET':
#         users = user.get_alone_user(int(id))
#         username = users.get('username')
#         age = users.get('age')
#         telphone = users.get('telphone')
#         email = users.get('email')
#         return render_template('userupdate.html', id=id,username=username, age=age, telphone=telphone, email=email)
#     if user.user_update(params):
#         flash("用户更新成功")
#         return redirect('/user/')
#     return render_template('userupdate.html',error='更新失败')

#加载日志的页面
@app.route('/logs/')
@user.login_check
def nginx_logs():
    params = request.args if request.method == 'GET' else request.form
    if params.get('numbers'):
        top = params.get('numbers')
    else:
        top = 10
    access_list = logs.log_access(top=int(top))
    return render_template('logstop.html',toplist=access_list,numbers=top)

#触发后将日志导入到mysql中
@app.route('/import_los/')
@user.login_check
def import_logs():
    if logs.logs_import_sql():
        return 'ok'


@app.route('/upload/',methods=['POST','GET'])
@user.login_check
def files_upload():
    files = request.files.get('files')
    if files:
        filename = ''.join(random.sample(string.ascii_letters + string.digits, 8))
        filepath = '/home/op/test/%s.log' % filename
        files.save(filepath)
        if logs.logs_import_sql(filepath):
            flash("日志上传成功")
        else:
            flash("日志上传失败")
    else:
        flash("日志上传失败")
    return redirect('/logs/')

@app.route('/user/reset/',methods=['POST','GET'])
@user.login_check
def user_reset():
    params = request.args if request.method == 'GET' else request.form
    id = params.get('id')
    username = params.get('username')
    _is_ok,_error,newpasswd = user.user_reset(id, username)
    return jsonify({'is_ok':_is_ok,'error':_error,'newpass':newpasswd})
#test
# @app.route('/test/',methods=['POST','GET'])
# def test():
#     print request.form
#     print request.args
#     print request.files
#     # print request.header
#     return render_template('user.html',user_list=user.get_user())

'''
dialog 修改密码
'''
@app.route('/user/passwd-change/',methods=['POST'])
@user.login_check
def change_passwd():
    params = request.args if request.method == 'GET' else request.form
    uid = params.get('userid')
    upass = params.get('user-password')
    muser = session['username']['username']
    mpass = params.get('manager-password')
    _is_ok,_error = user.valid_change_passwd(uid, upass, muser, mpass)
    if _is_ok:
        _is_ok,_error = user.change_passwd(uid, upass)
    return jsonify({'is_ok':_is_ok,'error':_error})

@app.route('/user/newuser/',methods=['POST'])
def newuser():
    params = request.args if request.method == 'GET' else request.form
    _is_ok,_error = user.user_add(params)
    return jsonify({'is_ok':_is_ok,'error':_error})


'''
测试页面
'''
@app.route('/test/',methods=['POST','GET'])
def test():
    params = request.args if request.method == 'GET' else request.form
    return render_template('tt.html')

@app.route('/assets/')
def assets_list():
    _assets = assets.get_list()
    return render_template('assets.html',assets=_assets)

@app.route('/assets/create/',methods=['POST','GET'])
def assets_create():
    _idcs = assets.get_idc_name()
    return render_template('assets_create.html',idcs=_idcs)

@app.route('/assets/add/',methods=['POST','GET'])
def assets_add():
    params = request.args if request.method == 'GET' else request.form
    _is_ok,_error = assets.validate_create(params)
    if _is_ok:
        success = '添加成功'
    else:
        success = ''
    return jsonify({'is_ok':_is_ok,'error':_error,'success':success})

@app.route('/assets/modify/',methods=['POST','GET'])
def assets_modify():
    params = request.args if request.method == 'GET' else request.form
    id = params.get('id')
    result = assets.get_by_id(id)
    print json.dumps(result)

    return render_template('assets_create.html',result=result)

@app.route('/assets/get_data/',methods=['POST','GET'])
def get_data():
    params = request.args if request.method == 'GET' else request.form
    id = params.get('id')
    result = assets.get_by_id(id)
    return jsonify(result=result)


@app.route('/assets/update/',methods=['POST','GET'])
def assets_update():
    pass


'''
登出用户
'''
@app.route('/logout/')
def logout():
    session.clear()
    return redirect('/')


