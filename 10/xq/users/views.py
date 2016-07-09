#encoding: utf-8
import sys
reload(sys)
sys.setdefaultencoding('utf-8')                     #设置命令行为utf-8,让代码里面的中文正常显示

#from flask import Flask                            #从flask包导入Flask类
from flask import render_template                   #从flask包导入render_template函数
from flask import request                           #从flask包导入request对象
from flask import redirect                          #从flask包导入redirect函数
from flask import session                           #从flask包导入session函数
from flask import flash                             #从flask包导入flash函数
from functools import wraps                         #从functools导入wraps函数
from modules import User,Assets                     #Modules修改成类的形式
import os,json
from users import app
from datetime import datetime
#import userdb as user                               #导入user模块
#import asserts

#app = Flask(__name__)
app.secret_key = os.urandom(32)

def login_required(func):                          #函数装饰器，用于装饰登陆是否有session，检验身份
    @wraps(func)
    def wrapper(*args, **kwargs):
        if session.get('user') is None:
            return redirect('/')
        rt = func(*args, **kwargs)
        return rt
    return wrapper

'''
处理时间不为json格式的问题
'''
class ComplexEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime):
            return obj.strftime('%Y-%m-%d %H:%M:%S')
        elif isinstance(obj, date):
            return obj.strftime('%Y-%m-%d')
        else:
            return json.JSONEncoder.default(self, obj)
'''
打开用户登录页面
'''
@app.route('/')                                     #将url path=/的请求交由index函数处理
def index():
    return render_template('login.html')            #渲染login.html模板，并返回页面内容

'''
用户登录信息检查
'''
@app.route('/login/', methods=["POST"])             #将url path=/login/的post请求交由login函数处理
def login():
    username = request.form.get('username', '')     #接收用户提交的数据
    password = request.form.get('password', '')
    #print request.form['username']
    #print "username is %s" %username
    # _users,_error = user.get_info(username=username)
    # if _users:
    #     _id = _users[0]['id']
    #     age = _users[0]['age']
    # else:
    #     _id = ''
    #希望把ID加进去作为session绑定，后面根据id修改对应用户的密码！
    #需要验证用户名密码是否正确
    _user = User.validate_login(username, password)
    if _user:                                       #判断用户登录是否合法
        session['user'] = _user                     #设置session,绑定用户身份信息，和用户名绑定，类似办银行卡
        flash("登陆成功！")                         #flask的消息闪现，一次生成一个， 通过函数get_flashed_messages()获取
        print session                               #打印session信息，用于查看，理解session
        return redirect('/dashboard/')                  #跳转到url展示用户页面
    else:
        #登录失败
        return render_template('login.html', username=username, error='用户名或密码错误')

'''
自动登录zabbix
'''
@app.route('/loginzbx/auto/')             #将url path=/login/的post请求交由login函数处理
def loginzabbix():
    _users,_errors = User.get_info()
    #print _users
    #获取当前用户的信息
    _user,_error = User.get_info(_id=session.get('user').get('id'))
    return redirect('http://monitor.xsjcs.cn/index.php')


'''
网络流量查看
'''
@app.route('/networkflow/')             #将url path=/login/的post请求交由login函数处理
def networkflow():
    _users,_errors = User.get_info()
    #print _users
    #获取当前用户的信息
    _user,_error = User.get_info(_id=session.get('user').get('id'))
    return render_template('networkflow.html',users=_users,curuser=_user,time=3600)

'''
网络质量查看
'''
@app.route('/networkquality/')             #将url path=/login/的post请求交由login函数处理
def networkquality():
    _users,_errors = User.get_info()
    #print _users
    #获取当前用户的信息
    _user,_error = User.get_info(_id=session.get('user').get('id'))
    return render_template('networkquality.html',users=_users,curuser=_user,time=3600)

'''
网络拓扑图查看
'''
@app.route('/networkmap/')             #将url path=/login/的post请求交由login函数处理
def networkmap():
    _users,_errors = User.get_info()
    #print _users
    #获取当前用户的信息
    _user,_error = User.get_info(_id=session.get('user').get('id'))
    return render_template('networkmap.html',users=_users,curuser=_user,time=3600)

'''
用户列表显示
'''
@app.route('/dashboard/')                               #将url path=/users/的get请求交由users函数处理
@login_required
def dashboard():
    #获取所有用户的信息
    _users,_errors = User.get_info()
    #print _users
    #获取当前用户的信息
    _user,_error = User.get_info(_id=session.get('user').get('id'))
    #print _user
    return render_template('dashboard.html',users=_users,curuser=_user)



'''
用户列表显示
'''
@app.route('/users/')                               #将url path=/users/的get请求交由users函数处理
@login_required
def users():
    #获取所有用户的信息
    _users,_errors = User.get_info()
    #print _users
    #获取当前用户的信息
    _user,_error = User.get_info(_id=session.get('user').get('id'))
    #print _user
    return render_template('users.html',users=_users,curuser=_user)

'''
跳转到新建用户信息输入的页面
'''
@app.route('/user/create/')                        #将url path=/user/create/的get请求交由create_user处理
@login_required
def create_user():
    return render_template('user_create.html')      #加载渲染user_create.html


'''
存储新建用户的信息，POST
'''

@app.route('/user/add/', methods=['POST'])          #将url path=/user/add的post请求交由add_user处理
@login_required
def add_user():
    username = request.form.get('username', '')
    password = request.form.get('password', '')
    age = request.form.get('age', '')
    _session_id = session['user']['id']
    _session_username = session['user']['username']
    # gender = request.form.get('gender','1')
    # hobby = request.form.getlist('hobby')
    # department = request.form.getlist('department')
    # img = request.files.get('img')
    # if img:
    #     print img.filename
    #     img.save('/tmp/kk.txt')
    # print request.form
    # print gender
    # print hobby
    # print department

    #检查用户信息是否合法
    _is_ok, _error = User.validate_add_user(_session_username,username, password, age)
    if _is_ok:
        User.add_user(username, password, age)      #检查ok，添加用户信息
        #flash("用户%s添加成功！" %username)
        #return redirect('/users/')                  #跳转到用户列表
    return json.dumps({'is_ok':_is_ok, "error":_error})
        # return render_template('user_create.html', \
        #                         error=_error, username=username, \
        #                         password=password, age=age)


'''
打开用户信息修改页面，默认GET
'''
@app.route('/user/modify/')                          #将url path=/user/modify/的get请求交由modify_user函数处理
@login_required
def modify_user():
    _id = request.args.get('id', '')
    _users,_error = User.get_info(_id=_id)
    if _users:
        _username = _users[0]['username']
        _password =_users[0]['password']
        _age = _users[0]['age']
    else:
        _error = '用户不存在'
    return render_template('user_modify.html',_error=_error,_id=_id,password=_password, age=_age, username=_username)

'''
提交表单，保存用户数据
'''
@app.route('/user/update/', methods=['GET','POST'])           #将url path=/user/update/的post请求交由update_user函数处理
@login_required
def update_user():
    #获取修改页面的用户信息
    _id = request.form.get('id', '')
    username = request.form.get('username', '')
    password = request.form.get('password', '')
    age = request.form.get('age', 0)
    _session_id = session['user']['id']
    _session_username = session['user']['username']
    #print type(_id),type(_session_id)
    #print type(_id),type(username),type(password),type(age)
    #检查在修改页面的用户信息
    _is_ok, _error = User.validate_update_user(_id,_session_id,username,_session_username,password,age)
    #print "valid:%s" %_is_valid_ok
    #print "error:%s"  %_error
    if _is_ok:
        User.update_user(_id,username, password, age)
        # flash("用户%s修改成功！"  %username)
        # return redirect('/users/')
    return json.dumps({'is_ok':_is_ok, "error":_error})
    # else:
    #     return render_template('user_modify.html', _id=_id,error=_error, username=username, password=password, age=age)

'''
用户删除
'''
@app.route('/user/delete/')
@login_required
def delete_user():
    _id = request.args.get('id')
    _user,_error = User.get_info(_id=_id)
    if _user is None:
        _error = '用户信息不存在'
    else:
        username = _user[0]['username']
        _session_username = session['user']['username']
        if User.check_is_admin(_session_username):
            User.delete_user(_id)
            flash("%s删除成功" %username)
        else:
            flash('权限不够，只有管理员才能删除用户信息！')
    return redirect('/users/')

'''
用户搜索页面，通过get回显
'''
@app.route('/user/finduser/')
def find_user():
    return render_template('user_find.html')

'''
用户查找，post操作
'''
@app.route('/user/find/',methods=['POST','GET'])
def finder_user():
    username = request.form.get('username','')
    users,_error = User.get_info(username=username)
    if users:
        return render_template('users.html',users = users)
    flash("Sorry，没有查到相关数据!")
    return render_template('users.html')

'''
log查询
'''
@app.route('/user/logs/',methods=['POST','GET'])
@login_required
def logs():
    count = request.form.get('count',10)
    count = int(count) if str(count).isdigit() else 10
    logs,_error = User.get_info(_count=count)
    return render_template("logs.html",logs=logs)

'''
自定义log查询
'''
@app.route('/user/customlogs/',methods=['POST','GET'])
@login_required
def custom_logs():
    sql = request.form.get('sql','select * from logs limit 10;')
    print "sql is %s" %sql
    _result,_error = User.get_info(_sql=sql)
    if not sql:
        return redirect('/user/customlogs/')
    if _result:
        return render_template("customlogs.html",result=_result,sql=sql)
    else:
        return render_template("customlogs.html",result=_result,sql=sql,error=_error)


'''
打开密码修改页面，默认GET
'''
@app.route('/user/modifypasswd/')                          #将url path=/user/modify/的get请求交由modify_user函数处理
@login_required
def modify_password():
    _id = session.get('user').get('id')
    print "id is %s" %_id
    _users,_error = User.get_info(_id=_id)
    if _users:
        _username = _users[0]['username']
        _password =_users[0]['password']
        _age = _users[0]['age']
    return render_template('passwd_modify.html',username=_username)

'''
提交更新密码表单，保存并自动返回首页
'''
@app.route('/user/updatepasswd/',methods=['POST','GET'])
@login_required
def update_passwd():
    _id = session.get('user').get('id')
    #提交表单中的原密码
    _password = request.form.get('_password')
    print "old passwd ：%s" %_password
    #提交表单中的新密码
    _password1 = request.form.get('_password1')
    _password2 = request.form.get('_password2')
    print "new passwd1:%s" %_password1
    print "new passwd2:%s" %_password2
    _result,_error = User.validate_new_password(_id,_password1,_password2)
    if  User.validate_password(_id,_password):
        if _result:
            User.update_password(_id,_password1)
            flash("密码修改成功！")
            return redirect('/users/')
        else:
            return render_template('passwd_modify.html',error=_error,_password=_password,_password1=_password1,_password2=_password2)
    else:
        flash("原密码输入错误,请重新输入！")
        return render_template('passwd_modify.html')

'''
用户上传页面显示
'''
@app.route('/user/upload/')
@login_required
def upload_page():
    return render_template('upload.html')

'''
用户上传操作
'''
@app.route('/user/uploadaction/',methods=['POST','GET'])
@login_required
def upload_action():
    img = request.files.get('img')
    if img:
        #_file_name = img.filename
        _file_name = img.filename
        _file_path = './users/static/images/%s' %_file_name
        _up_ok,_path =User.upload_validate_check(_file_path)
        _path = 'static/images/'+os.path.basename(_path)
        print _path
        if _up_ok:
            img.save(_file_path)
            return render_template('upload_action.html',_path=_path)
        else:
            flash("文件为空或格式不对，上传失败！")
            return render_template('upload_action.html')
    flash("上传失败！")
    return render_template('upload_action.html')

'''
用户密码修改
'''
@app.route('/user/charge-password/', methods=['POST'])
def charge_user_password():
    uid = request.form.get('userid')
    manager_password = request.form.get('manager-password')
    user_password = request.form.get('user-password')
    _is_ok, _error = User.validate_charge_user_password(uid, user_password, session['user']['username'], manager_password)
    if _is_ok:
        User.charge_user_password(uid, user_password)
    return json.dumps({'is_ok':_is_ok, "error":_error})


'''
列出资产信息
'''
@app.route('/asserts/')                               #将url path=/users/的get请求交由users函数处理
def get_asserts():
    #获取所有资产的信息
    _asserts = Assets.get_list()
    _idcs =  dict(Assets.get_idcs())
    return render_template('asserts.html',asserts=_asserts,_idcs=_idcs)

'''
创建资产信息
'''
@app.route('/asserts/create/',methods=['POST','GET'])                               #将url path=/users/的get请求交由users函数处理
def create_asserts():
    _idcs = Assets.get_idcs()
    print _idcs
    return render_template('assert_create.html',idcs=_idcs)

'''
新增资产信息
'''
@app.route('/asserts/add/',methods=['POST','GET'])                               #将url path=/users/的get请求交由users函数处理
def add_asserts():
    _sn = request.form.get('sn','')
    _ip = request.form.get('ip','')
    _hostname = request.form.get('hostname','')
    _os = request.form.get('os','')
    _cpu = request.form.get('cpu')
    _ram = request.form.get('ram')
    _disk = request.form.get('disk')
    _idc_id = request.form.get('idc_id')
    _admin = request.form.get('admin','')
    _business = request.form.get('business','')
    _purchase_date = request.form.get('purchase_date')
    _warranty = request.form.get('warranty')
    _vendor = request.form.get('vendor','')
    _model = request.form.get('model','')
    print request.form
    print "sn is %s,_idc_id is %s,_purchase_date is %s" %(_sn,_idc_id,_purchase_date)
    print _cpu
    _is_ok, _error = Assets.validate_create(_sn,_ip,_hostname,_os,_cpu,_ram,_disk,_idc_id,_admin,_business,_purchase_date,_warranty,_vendor,_model)
    if _is_ok:
        Assets.create(_sn,_ip,_hostname,_os,_cpu,_ram,_disk,_idc_id,_admin,_business,_purchase_date,_warranty,_vendor,_model)
    return json.dumps({'is_ok':_is_ok, 'error':_error, 'success':'添加成功'})

'''
资产删除
'''
@app.route('/assets/delete/')
@login_required
def delete_asset():
    _id = request.args.get('id')
    _asset,_error = Assets.get_by_id(_id=_id)
    if not _asset:
        _error = '资产不存在'
    else:
        _session_username = session['user']['username']
        if User.check_is_admin(_session_username):
            Assets.delete(_id)
            flash("删除成功")
        else:
            flash('权限不够，只有管理员才能删除资产信息！')
    return redirect('/asserts/')


'''
获取修改资产信息页面
'''
@app.route('/asserts/update/',methods=['POST','GET'])                               #将url path=/users/的get请求交由users函数处理
def update_asserts():
    _idcs = [('1', '北京鲁谷'), ('2', '北京森华'), ('3', '北京亦庄'), ('4', '北京大兴')]
    return render_template('assert_update.html',idcs=_idcs)

'''
提交数据，正式修改资产信息
'''
@app.route('/asserts/modify/',methods=['POST','GET'])
def modify_asset():
    #获取表单上修改后的信息
    _id = request.form.get('serverid','')
    _sn = request.form.get('sn','')
    _ip = request.form.get('ip','')
    _hostname = request.form.get('hostname','')
    _os = request.form.get('os','')
    _cpu = request.form.get('cpu')
    _ram = request.form.get('ram')
    _disk = request.form.get('disk')
    _idc_id = request.form.get('idc_id')
    _admin = request.form.get('admin','')
    _business = request.form.get('business','')
    _purchase_date = request.form.get('purchase_date')
    _warranty = request.form.get('warranty')
    _vendor = request.form.get('vendor','')
    _model = request.form.get('model','')
    print "id is %s,sn is %s,_idc_id is %s,_purchase_date is %s,_ram is %s" %(_id,_sn,_idc_id,_purchase_date,_ram)
    _is_ok, _error = Assets.validate_update(_sn,_ip,_hostname,_os,_cpu,_ram,_disk,_idc_id,_admin,_business,_purchase_date,_warranty,_vendor,_model)
    print _is_ok
    if _is_ok:
        #print "hello"
        Assets.update(_sn,_ip,_hostname,_os,_cpu,_ram,_disk,_idc_id,_admin,_business,_purchase_date,_warranty,_vendor,_model,_id)
    return json.dumps({'is_ok':_is_ok, 'error':_error, 'success':'更新成功'})

'''
接受前端js提交过来的id，返回整条数据信息
'''
@app.route('/asserts/getinfo/<id>')
def get_asset_by_id(id):
    _rt,_error = Assets.get_by_id(id)
    return json.dumps(_rt,cls=ComplexEncoder)


'''
找不到页面是提示404错误
'''
#如果返回代码是404，则返回页面没找到
@app.errorhandler(404)
def page_not_found(error):
    return render_template('page_not_found.html'), 404

'''
用户登出系统，清除session
'''
@app.route('/logout/')
def logout():
    #清除sessin
    session.clear()
    print session
    return redirect('/')
