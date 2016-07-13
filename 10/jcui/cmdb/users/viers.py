#encoding:utf-8
import json
import sys
import random
import string

import datetime
from flask import render_template,request,redirect,session, flash ,jsonify
from . import app         #user模块下的变量,在__init__.py  中定义
from modules.modules import User,Assets,Logs,Performs


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
    #类调用--------
    get_session = User.validate_login(username, password)
    if get_session:
        session['username'] = get_session
        return redirect('/user/')
    else:
        return render_template('login.html', username=username, error='用户认证失败')

    #函数调用------
    # if user.validate_login(username, password):
    #     session['username'] = {'username': username}
    #     return redirect('/user/')
    # else:
    #     return render_template('login.html',username=username,error='用户名或密码错误')

'''
a
用户列表
'''
@app.route('/user/')
@User.login_check
def users():
    return render_template('user.html', user_list=User.get_list())

'''
用户添加
'''
@app.route('/user/useradd/',methods=['POST','GET'])
@User.login_check
def users_add():
    params = request.args if request.method == 'GET' else request.form
    if not params:
        return render_template('useradd.html')
    '''
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
    '''
    if User.user_add(params):
        # flash("用户%s添加成功" % username)
        return redirect('/user/')
    else:
        error = '用户名已存在'
    return render_template('useradd.html',error=error)

'''
用户删除
'''
@app.route('/user/userdel/',methods=['POST','GET'])
@User.login_check
def user_del():
    params = request.args if request.method == 'GET' else request.form
    id = params.get('id')
    username = params.get('username')
    if User.user_del(int(id), username):
        # flash("用户删除成功")
        return redirect('/user/')
    return render_template('user.html',error='删除失败')

'''
用户更新
'''
@app.route('/user/userupdate/',methods=['POST','GET'])
@User.login_check
def user_update():
    params = request.args if request.method == 'GET' else request.form
    _is_ok, _error = User.user_update(params)
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
@User.login_check
def nginx_logs():
    params = request.args if request.method == 'GET' else request.form
    if params.get('numbers'):
        top = params.get('numbers')
    else:
        top = 10
    access_list = Logs.log_access(top=int(top))
    return render_template('logstop.html',toplist=access_list,numbers=top)

#触发后将日志导入到mysql中
@app.route('/import_los/')
@User.login_check
def import_logs():
    if Logs.logs_import_sql():
        return 'ok'


@app.route('/upload/',methods=['POST','GET'])
@User.login_check
def files_upload():
    files = request.files.get('files')
    if files:
        filename = ''.join(random.sample(string.ascii_letters + string.digits, 8))
        filepath = '/home/op/test/%s.log' % filename
        files.save(filepath)
        if Logs.logs_import_sql(filepath):
            flash("日志上传成功")
        else:
            flash("日志上传失败")
    else:
        flash("日志上传失败")
    return redirect('/logs/')

@app.route('/user/reset/',methods=['POST','GET'])
@User.login_check
def user_reset():
    params = request.args if request.method == 'GET' else request.form
    id = params.get('id')
    username = params.get('username')
    _is_ok,_error,newpasswd = User.user_reset(id, username)
    return jsonify({'is_ok':_is_ok,'error':_error,'newpass':newpasswd})

'''
dialog 修改密码
'''
@app.route('/user/passwd-change/',methods=['POST'])
@User.login_check
def change_passwd():
    params = request.args if request.method == 'GET' else request.form
    uid = params.get('userid')
    upass = params.get('user-password')
    muser = session['username']['username']
    mpass = params.get('manager-password')
    _is_ok,_error = User.valid_change_passwd(uid, upass, muser, mpass)
    if _is_ok:
        _is_ok,_error = User.change_passwd(uid, upass)
    return jsonify({'is_ok':_is_ok,'error':_error})

@app.route('/user/newuser/',methods=['POST'])
@User.login_check
def newuser():
    params = request.args if request.method == 'GET' else request.form
    _is_ok,_error = User.user_add(params)
    return jsonify({'is_ok':_is_ok,'error':_error})


'''
测试页面
'''
@app.route('/test/',methods=['POST','GET'])
def test():
    params = request.args if request.method == 'GET' else request.form
    return render_template('tt.html')

@app.route('/assets/')
@User.login_check
def assets_list():
    _assets = Assets.get_list()
    for x in _assets:
        x['purchase_date'] = x['purchase_date'].strftime("%Y-%m-%d")
    return render_template('assets.html',assets=_assets)                   #从数据库获取

@app.route('/assets/create/',methods=['POST','GET'])
@User.login_check
def assets_create():
    _idcs = Assets.get_idc_name()
    return render_template('assets_create.html',idcs=_idcs)

@app.route('/assets/add/',methods=['POST','GET'])
@User.login_check
def assets_add():
    params = request.args if request.method == 'GET' else request.form
    _is_ok,_error = Assets.validate_create(params)
    if _is_ok:
        success = '添加成功'
    else:
        success = ''
    return jsonify({'is_ok':_is_ok,'error':_error,'success':success})

@app.route('/assets/modify/',methods=['POST','GET'])
@User.login_check
def assets_modify():
    params = request.args if request.method == 'GET' else request.form
    id = params.get('id')
    result = Assets.get_by_id(id)
    _idcs = Assets.get_idc_name()
    return render_template('assets_modify.html',result=result,idcs=_idcs)

@app.route('/assets/update/',methods=['POST','GET'])
@User.login_check
def assets_update():
    params = request.args if request.method == 'GET' else request.form
    _is_ok,_error = Assets.validate_update(params)
    if _is_ok:
        success = '更新成功'
    else:
        success = ''
    return jsonify({'is_ok':_is_ok,'error':_error,'success':success})

@app.route('/assets/delete/',methods=['POST','GET'])
@User.login_check
def assets_delete():
    params = request.args if request.method == 'GET' else request.form
    id = params.get('id')
    print id
    _is_ok,_error = Assets.delete(int(id))
    if _is_ok:
        return redirect('/assets/')
    return render_template('assets.html')

@app.route('/assets/perform/', methods=['POST', 'GET'])
@User.login_check
def assets_perform():
    params = request.args if request.method == 'GET' else request.form
    id = params.get('id','')
    _asset = Assets.get_by_id(id)
    datetime_list,cpu_list,ram_list = Performs.get_list(_asset.get('ip'))
    # print datetime_list
    # print cpu_list
    # print ram_list
    return render_template('assets_perform.html',datetime_list=json.dumps(datetime_list),cpu_list=json.dumps(cpu_list),ram_list=json.dumps(ram_list))
    # return render_template('assets_perform.html')



'''
登出用户
'''
@app.route('/logout/')
def logout():
    session.clear()
    return redirect('/')

@app.route('/performs/',methods=['POST'])
def performs():
    params =  request.get_json()
    Performs.add(params)
    return json.dumps({'code':200,'text':'success'})


