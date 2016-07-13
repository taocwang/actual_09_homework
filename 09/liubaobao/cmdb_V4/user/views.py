#encoding:utf-8

from flask import Flask                                     #导入flask框架
from flask import request                                   #导入request的函数
from flask import redirect                                  #导入redirect函数
from flask import session                                   #导入session会话
from flask import render_template                           #导入调用模板函数
from functools import wraps
from flask import url_for
from flask import flash
from loganalysisdb import get_topn
import json
import os
import sys
reload(sys)
sys.setdefaultencoding('utf-8')                             #设定默认字符集,免得报错
import  userdb as user                                      #导入userdb重新命名为user
import time
from loganalysis import loganalysis

from user import app
import asset


def login_required(func):                                   #装饰器检查session登录的session
    @wraps(func)
    def wrapper(*args, **kwargs):
        if session.get('user') is None:
            return redirect('/')
        rt = func(*args, **kwargs)
        return rt
    return wrapper




'''
用户登录首页
'''
@app.route('/')
def index():
    return render_template('login.html')




'''
用户登录信息检查
'''
@app.route('/login/',methods=['POST'])
def login():
    username = request.form.get('username')                 #从表单中提取数据
    password = request.form.get('password')
    _error = "用户名或者密码不正确"
    if user.validate_login(username,password):
        session['user'] = {'username':username}             #登录成功的时候放入session的一个字典
        return redirect('/users/')
    else:
        return render_template('login.html',error=_error)





'''
用户列表页
'''
@app.route('/users/')
@login_required
def users():
    users = user.get_users()
    return render_template('users.html',users=users,msg=request.args.get('msg',''))




'''
创建用户页面
'''
@app.route('/user/create/')
def create_user():
    return render_template('create_user.html')




'''
创建用户
'''
@app.route('/user/add/',methods=['POST'])
def add_user():
    username = request.form.get('username','')
    password = request.form.get('password','')
    age = request.form.get('age','')
    _is_ok,_error = user.validate_add_user(username,password,age)
    if _is_ok:
        user.add_user(username,password,age)
        flash('新建成功!')
        return redirect('/users/')
        #return redirect(url_for('users',msg='新建成功'))
    else:
        return render_template('create_user.html',error=_error,username=username,password=password,age=age)




'''
删除用户
'''
@app.route('/user/delete/')
def delete_user():
    uid = request.args.get('id')
    user.delete_user(uid)
    flash('删除用户信息成功!')
    return redirect('/users/')



'''
打开用户信息的修改页面
'''
@app.route('/user/modify/')
def modify_user():
    uid = request.args.get('id','')
    _user = user.get_user_by_uid(uid)
    _error = ''
    _uid = ''
    _username = ''
    _password = ''
    _age = ''
    if _user is None:
        _error = '用户信息不存在!'
    else:
        _uid = _user.get('id')
        _username = _user.get('username')
        _password = _user.get('password')
        _age = _user.get('age')

    return render_template('user_modify.html',error=_error,password=_password,username=_username,age=_age,id=_uid)




'''
用户修改
'''
@app.route('/user/update/',methods=['POST'])
def update_user():
    _uid = request.form.get('id','')
    _username = request.form.get('username','')
    _password = request.form.get('password','')
    _age = request.form.get('age','')
    _is_ok,_error = user.validate_update_user(_uid,_username,_password,_age)
    if _is_ok:
        user.update_user(_uid,_username,_password,_age)
        flash('更新用户信息成功!')
        return redirect('/users/')
    else:
        return render_template('user_modify.html',error=_error,password=_password,username=_username,age=_age,id=_uid)




'''
日志上传
'''
@app.route('/uploadlogs/',methods=['POST'])
def uploadlog():
    _file = request.files.get('logfile')
    if _file:
        _filepath = 'temp/%s' %time.time()
        _file.save(_filepath)
        loganalysis(_filepath)
    return redirect('/log/')




'''
日志展示
'''
@app.route('/log/')
def log():
    topn = request.args.get('topn',10)
    topn = int(topn) if str(topn).isdigit() else 10

    rt_list = get_topn(topn=topn)
    return render_template('log.html',rt_list=rt_list,title_log='topn log')




'''
用户退出登录
'''
@app.route('/logout/')
def logout():
    session.clear()
    return redirect('/')




'''
dailog和ajax实现弹窗修改密码
'''
@app.route('/user/change-password/', methods=['POST'])
def change_user_password():
    uid = request.form.get('userid')
    manager_password = request.form.get('manager-password')
    user_password = request.form.get('password')
    print user_password
    _is_ok, _error = user.validate_change_user_password(uid,user_password,session['user']['username'],manager_password)
    if _is_ok:
        user.change_user_password(uid, user_password)
    return json.dumps({'_is_ok':_is_ok, 'error':_error})



'''
dailog和ajax实现弹窗添加用户
'''
@app.route('/user/create-user/',methods=['POST'])
def create__user():
    username = request.form.get('username')
    password = request.form.get('password')
    age = request.form.get('age')
    _is_ok, _error = user.validate_create_user(username,password,age)
    if _is_ok:
        user.create_user(username,password,age)
    return json.dumps({'_is_ok':_is_ok, 'error':_error})



'''
dailog和ajax实现更新用户信息弹窗
'''
@app.route('/user/update-user/',methods=['POST'])
def update__user():
    id = request.form.get('id')
    username = request.form.get('username')
    age = request.form.get('age')
    _is_ok,_error = user.validate_update_user(id,username,age)
    if _is_ok:
        user.update__user(id,username,age)
    return json.dumps({'_is_ok':_is_ok,'error':_error})



'''
dailog和ajax实现删除
'''
@app.route('/user/delete-user/',methods=['POST'])
def delete__user():
    uid = request.form.get('id')
    user.delete_user(uid)
    flash('删除用户信息成功!')
    return json.dumps({'_is_ok':True})


'''
dailog和ajax实现列表异步请求前端
'''
@app.route('/user/list/')
def user_list():
    users = user.get_users()
    res = json.dumps(users)
    return res





'''
资产列表页面
'''
@app.route('/assets/')
def asset_list():
    _assets = asset.get_list()
    return render_template('assets.html',assets=_assets)





'''
添加资产和更新的dialog的body的页面
'''
@app.route('/assets/create_update/',methods=['POST','GET'])
def create_asset():
    _cpu = request.form.get('_cpu')
    _ram = request.form.get('_ram')
    _disk = request.form.get('_disk')
    dic = {}
    dic['_cpu'] = _cpu
    dic['_ram'] = _ram
    dic['_disk'] = _disk
    _idcs = asset.get_idcs()
    return  render_template('asset_create.html',idcs=_idcs,dic=dic)







'''
添加资产
'''
@app.route('/assets/add/',methods=['POST','GET'])
def asset_add():
    _sn = request.form.get('sn','')
    _ip = request.form.get('ip','')
    _hostname = request.form.get('hostname','')
    _os = request.form.get('os','')
    _cpu = request.form.get('cpu','')
    _ram = request.form.get('ram','')
    _disk = request.form.get('disk',)
    _idc_id = request.form.get('idc_id','')
    _admin = request.form.get('admin','')
    _business = request.form.get('business','')
    _purchase_date = request.form.get('purchase_date','')
    _warranty = request.form.get('warranty')
    _model = request.form.get('model','')
    _vendor = request.form.get('vendor','')
    _is_ok,_error = asset.validate_create(_sn,_ip,_hostname,_os,_cpu,_ram,_disk,_idc_id,_admin,_business,_purchase_date,_model,_warranty,_vendor)
    if _is_ok:
        asset.create([_sn,_ip,_hostname,_os,_cpu,_ram,_disk,_idc_id,_admin,_business,_purchase_date,_warranty,_model,_vendor])
    return json.dumps({'_is_ok':_is_ok,'error':_error})




'''
更新资产
'''
@app.route('/assets/modify/',methods=['POST','GET'])
def asset_modify():
    _id = request.form.get('id','')
    _sn = request.form.get('sn','')
    _ip = request.form.get('ip','')
    _hostname = request.form.get('hostname','')
    _os = request.form.get('os','')
    _cpu = request.form.get('cpu','')
    _ram = request.form.get('ram','')
    _disk = request.form.get('disk',)
    _idc_id = request.form.get('idc_id','')
    _admin = request.form.get('admin','')
    _business = request.form.get('business','')
    _purchase_date = request.form.get('purchase_date','')
    _warranty = request.form.get('warranty')
    _model = request.form.get('model','')
    _vendor = request.form.get('vendor','')
    _is_ok,_error = asset.validate_update(_id,_sn,_ip,_hostname,_os,_cpu,_ram,_disk,_idc_id,_admin,_business,_purchase_date,_model,_warranty,_vendor)
    if _is_ok:
        asset.update([_sn,_ip,_hostname,_os,_cpu,_ram,_disk,_idc_id,_admin,_business,_purchase_date,_warranty,_model,_vendor,_id])
    return json.dumps({'_is_ok':_is_ok,'error':_error})





'''
删除资产
'''
@app.route('/assets/delete/',methods=['POST'])
def asset_delete():
    _id = request.form.get('id')
    _is_ok = asset.delete(_id)
    return json.dumps({'_is_ok':_is_ok})



'''
ajax请求资产列表
'''
@app.route('/assets/list/',methods=['POST','GET'])
def assets_list():
    # return render_template('asset_list.html')
    # _idcs = asset.get_idcs()
    # return  render_template('asset_create.html',idcs=_idcs)
    _assets = asset.get_list()
    return render_template('asset_list.html',assets=_assets)