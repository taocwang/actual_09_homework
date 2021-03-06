#encoding: utf-8
import sys
reload(sys)
sys.setdefaultencoding('utf-8')                     #设置命令行为utf-8,让代码里面的中文正常显示

from flask import Flask                             #从flask包导入Flask类
from flask import render_template                   #从flask包导入render_template函数
from flask import request                           #从flask包导入request对象
from flask import redirect                          #从flask包导入redirect函数
from flask import session                           #从flask包导入session函数
from flask import flash                             #从flask包导入flash函数
from functools import wraps                         #从functools导入wraps函数
import userdb as user                               #导入user模块
import os

app = Flask(__name__)

def login_required(func):                          #函数装饰器，用于装饰登陆是否有session，检验身份
    @wraps(func)
    def wrapper(*args, **kwargs):
        if session.get('user') is None:
            return redirect('/')
        rt = func(*args, **kwargs)
        return rt
    return wrapper

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
    print "username is %s" %username
    _users,_error = user.get_info(username=username)
    if _users:
        _id = _users[0]['id']
    else:
        _id = ''
    #希望把ID加进去作为session绑定，后面根据id修改对应用户的密码！
    #需要验证用户名密码是否正确
    if user.validate_login(username, password):     #判断用户登录是否合法
        session['user'] = {'username':username}     #设置session,绑定用户身份信息，和用户名绑定，类似办银行卡
        session['id'] = {'id':_id}
        flash("登陆成功！")                         #flask的消息闪现，一次生成一个， 通过函数get_flashed_messages()获取
        print session                               #打印session信息，用于查看，理解session
        return redirect('/users/')                  #跳转到url展示用户页面
    else:
        #登录失败
        return render_template('login.html', username=username, error='用户名或密码错误')

'''
用户列表显示
'''
@app.route('/users/')                               #将url path=/users/的get请求交由users函数处理
@login_required
def users():
    #获取所有用户的信息
    _users,_errors = user.get_info()
    return render_template('users.html', users=_users,username=session.get('user').get('username'))            #加载渲染users.html模板

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
    _is_ok, _error = user.validate_add_user(username, password, age)
    if _is_ok:
        user.add_user(username, password, age)      #检查ok，添加用户信息
        flash("用户%s添加成功！" %username)
        return redirect('/users/')                  #跳转到用户列表
    else:
        #跳转到用户新建页面，回显错误信息&用户信息
        return render_template('user_create.html', \
                                error=_error, username=username, \
                                password=password, age=age)


'''
打开用户信息修改页面，默认GET
'''
@app.route('/user/modify/')                          #将url path=/user/modify/的get请求交由modify_user函数处理
@login_required
def modify_user():
    _id = request.args.get('id', '')
    _users,_error = user.get_info(_id=_id)
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
    #print type(_id),type(username),type(password),type(age)
    #检查在修改页面的用户信息
    _is_valid_ok, _error = user.validate_update_user(_id,username,password,age)
    #print "valid:%s" %_is_valid_ok
    #print "error:%s"  %_error
    if _is_valid_ok:
        user.update_user(_id,username, password, age)
        flash("用户%s修改成功！"  %username)
        return redirect('/users/')
    else:
        return render_template('user_modify.html', _id=_id,error=_error, username=username, password=password, age=age)

@app.route('/user/delete/')
@login_required
def delete_user():
    _id = request.args.get('id')
    _user,_error = user.get_info(_id=_id)
    if _user is None:
        _error = '用户信息不存在'
    else:
        username = _user[0]['username']
        user.delete_user(_id)
        flash("%s删除成功" %username)
    return redirect('/users/')

@app.route('/user/find/',methods=['POST','GET'])
def finder_user():
    username = request.form.get('username','')
    users,_error = user.get_info(username=username)
    if users:
        return render_template('users.html',users = users)
    flash("Sorry，没有查到相关数据!")
    return render_template('users.html')

@app.route('/user/logs/',methods=['POST','GET'])
@login_required
def logs():
    count = request.form.get('count',10)
    count = int(count) if str(count).isdigit() else 10
    logs,_error = user.get_info(_count=count)
    return render_template("logs.html",logs=logs)


@app.route('/user/customlogs/',methods=['POST','GET'])
def custom_logs():
    sql = request.form.get('sql','select * from logs limit 10;')
    print "sql is %s" %sql
    _result,_error = user.get_info(_sql=sql)
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
    _id = session.get('id').get('id')
    print "id is %s" %_id
    _users,_error = user.get_info(_id=_id)
    if _users:
        _username = _users[0]['username']
        _password =_users[0]['password']
        _age = _users[0]['age']
    return render_template('passwd_modify.html',username=_username)

'''
提交更新密码表单，保存并自动返回首页
'''
@app.route('/user/updatepasswd/',methods=['POST','GET'])
def update_passwd():
    _id = session.get('id').get('id')
    #提交表单中的原密码
    _password = request.form.get('_password')
    print "old passwd ：%s" %_password
    #提交表单中的新密码
    _password1 = request.form.get('_password1')
    _password2 = request.form.get('_password2')
    print "new passwd1:%s" %_password1
    print "new passwd2:%s" %_password2
    _result,_error = user.validate_new_password(_id,_password1,_password2)
    if  user.validate_password(_id,_password):
        if _result:
            user.update_password(_id,_password1)
            flash("密码修改成功！")
            return redirect('/users/')
        else:
            return render_template('passwd_modify.html',error=_error,_password=_password,_password1=_password1,_password2=_password2)
    else:
        flash("原密码输入错误,请重新输入！")
        return render_template('passwd_modify.html')


@app.route('/user/upload/')
@login_required
def upload_page():
    return render_template('upload.html')


@app.route('/user/uploadaction/',methods=['POST','GET'])
@login_required
def upload_action():
    img = request.files.get('img')
    if img:
        #print img.filename
        img.save('/tmp/kk.txt')
    _up_ok,_content =user.upload_file_content('/tmp/kk.txt')
    print _up_ok,_content
    if _up_ok:
        return render_template('upload_action.html',_content=_content)
    else:
        flash("格式不正确，上传失败！")
        return render_template('upload_action.html')


@app.route('/logout/')
def logout():
    #清除sessin
    session.clear()
    print session
    return redirect('/')

@app.route('/test/')
def test():
     return render_template('user_create2222.html')

if __name__ == '__main__':
    app.secret_key = os.urandom(32)
    app.run(host='0.0.0.0', port=5000, debug=True)
