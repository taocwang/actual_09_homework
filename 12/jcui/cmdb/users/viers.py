#encoding:utf-8
import json
import sys
import random
import string

import datetime
from flask import render_template,request,redirect,session, flash ,jsonify
from . import app         #user模块下的变量,在__init__.py  中定义
from modules.modules import User,Assets,Logs,Performs
from modules import gconfig

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
    code_list = Logs.log_code_list()
    return render_template('logstop.html',toplist=access_list,numbers=top,code_list=json.dumps(code_list))

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
    cpu_end = {}
    ram_end = {}
    if datetime_list:
        cpu_end['y'] = cpu_list[-1]
        ram_end['y'] = ram_list[-1]
    return render_template('assets_perform.html',datetime_list=json.dumps(datetime_list),cpu_list=json.dumps(cpu_list),ram_list=json.dumps(ram_list),cpu_end=json.dumps(cpu_end),
                           ram_end=json.dumps(ram_end),id=id)

@app.route('/assets/perform/monitor/', methods=['POST', 'GET'])
@User.login_check
def assets_perform_monitor():
    params = request.args if request.method == 'GET' else request.form
    id = params.get('id')
    _asset = Assets.get_by_id(id)
    datetime_list, cpu_list, ram_list = Performs.get_list(_asset.get('ip'))
    datetime_end = {}
    cpu_end = {}
    ram_end = {}
    datetime_end['y'] = datetime_list[-1]
    cpu_end['y'] = cpu_list[-1]
    ram_end['y'] = ram_list[-1]
    return jsonify(datetime_end,cpu_end,ram_end)




@app.route('/assets/conssh/',methods=['POST','GET'])
@User.login_check
def assets__conssh():
    params = request.args if request.method == 'GET' else request.form
    id = params.get('id')
    result = Assets.get_by_id(id)
    return render_template('assets_conssh.html',result=result)

@app.route('/assets/concmd/',methods=['POST','GET'])
@User.login_check
def assets__concmd():
    params = request.args if request.method == 'GET' else request.form
    _is_ok,_result = User.validate_mpass(params)
    if _is_ok:
        error = ''
        _data = []
        nums = 1
        for x in _result:
            if x[0] :
                _data += (nums,x[0])
            else:
                _data += (nums, x[1])
            nums +=1
    elif _result:
        error = _result
        _data = ''
    else:
        error = '执行失败'
        _data = ''
    return jsonify({'is_ok':_is_ok,'error':error,'data_result':_data})

@app.route('/assets/performs/endstat/')
@User.login_check
def performs_cpu():
    params = request.args if request.method == 'GET' else request.form
    type_name = params.get('name')
    id = params.get('id')
    _asset = Assets.get_by_id(id)
    datetime_list, cpu_list, ram_list = Performs.get_list(_asset.get('ip'))
    if datetime_list:
        if type_name == 'cpu':
            end_cpu = cpu_list[-1]
            return jsonify({'y': end_cpu})
        elif type_name == 'ram':
            end_ram = ram_list[-1]
            return jsonify({'y': end_ram})
    return jsonify({'y':0})


#图表展示
@app.route('/charts/')
@User.login_check
def charts():
    status_legend,status_data = Logs.log2_code_list()

    time_status_legend,time_status_date,time_status_data = Logs.log2_time_status()

    _map_geocoord,_map_markline,_map_markpoint = Logs.log2_map()

    return render_template('charts.html',status_legend=json.dumps(status_legend),status_data=json.dumps(status_data),
                           time_legend=json.dumps(time_status_legend),time_date=json.dumps(time_status_date),
                           time_data=json.dumps(time_status_data),map_geocoord=json.dumps(_map_geocoord),
                           map_markline=json.dumps(_map_markline),map_markpoint=json.dumps(_map_markpoint))



'''
登出用户
'''
@app.route('/logout/')
def logout():
    session.clear()
    return redirect('/')

@app.route('/performs/',methods=['POST'])
def performs():
    app_key = request.headers.get('App-Key')
    app_secret = request.headers.get('App-Secret')
    if app_key != gconfig.app_key and app_secret != gconfig.app_secret:
        return json.dumps({'code':400,'text':'error app_key'})
    params =  request.get_json()
    Performs.add(params)
    return json.dumps({'code':200,'text':'success'})


