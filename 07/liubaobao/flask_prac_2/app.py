#encoding:utf-8
'''
导入系统模块，加载系统模块，设置程序的默认字符集，避免和前段取回来的数据自负编码不一样的错误情况。
'''
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
import os
import userdb as user

'''
导入flask的框架Flask的类
导入flask框架里面的render_template函数
导入flask框架里面的request类
导入flask框架里面的redirect函数
导入flask框架里面的session函数
导入flask框架里面的flash消息闪现的函数,导入url_for函数
'''
from flask import Flask
from flask import request,render_template,redirect,session,flash,url_for
from functools import  wraps #去掉装饰器的Bug
import dbutils
from log2db import log2db
from loganalysisdb import get_topn

app=Flask(__name__) #创建flask对象
app.secret_key=os.urandom(32) #生成session id

'''
装饰器验证,session会话
'''
def login_requerid(func):
    @wraps(func)
    def wrapper(*args,**kwargs): #自动适应参数和变化的参数
        if session.get('user') is None:
            return redirect('/')
        rt = func(*args,**kwargs)
        return rt
    return wrapper


'''
面对于用户登录的页面打开的登录页面
'''
@app.route('/')                                    #url path=/的请求交给index函数处理
def index():
    return render_template('login.html')            #加载login.html模版，并返回页面


'''
用户登录信息的检查
'''
@app.route('/login/',methods=['POST'])
def login():
    username  = request.form.get('username','')
    password  = request.form.get('password','')

    #需要进行密码验证是否正确
    if user.validate_login(username,password):
        session['user'] = {'username':username}
        return redirect('/users/')
    else:
        #登录失败
        return render_template('login.html',username=username,error='用户名或者密码错误!')


'''
登陆成功显示用户列表
'''
@app.route('/users/')
def users():
    users = user.get_users()                     #得到返回值列表
    return render_template('users.html',users=users)    #进行前端页面显示


'''
添加用户的跳转表单页面
'''
@app.route('/user/create/')
def usercreate():
    return render_template('user_create.html')

'''
添加用户表单页面提交
'''
@app.route('/user/add/',methods=['POST'])
def user_add():
    username = request.form.get('username')
    password = request.form.get('password')
    age = request.form.get('age')
    print username,password,age
    _is_ok,_error=user.validate_add(username,password,age)
    if _is_ok:
        flash('新建成功')
        user.user_add(username,password,age)
        return redirect('/users/')
    else:
        return render_template('user_create.html',error=_error)

'''
删除用户
'''
@app.route('/user/delete/',methods=['POST','GET'])
def user_delete():
    id = request.args.get('id')
    user.user_delete(id)
    flash('删除用户成功!')
    return redirect('/users/')


'''
更新用户的表单页面
'''
@app.route('/user/modify/',methods=['GET'])
def modify_user():
    id=request.args.get('id')
    _users = user.get_user(id)
    print _users
    _error = ''
    username = ''
    password = ''
    age = ''
    if _users is None:
        _error = u'用户信息不存在'
    username = _users.get('username','')
    password = _users.get('password','')
    age = _users.get('age')
    return render_template('user_modify.html',id=id,username=username,password=password,age=age,error=_error)



'''
更新用户页面进行提交
'''
@app.route('/user/update/',methods=['POST'])
def update_user():
    id = request.form.get('id')
    username = request.form.get('username')
    password = request.form.get('password')
    age = request.form.get('age')
    print id,username,password,age
    _is_ok,_error = user.validate_user_update(id,username,password,age)
    if _is_ok:
        user.update_user(id,username,password,age)
        return redirect('/users/')
        flash('修改成功!')
    else:
        return render_template('user_modify.html',id=id,username=username,password=password,age=age,error=_error)


'''
显示上传日志文件的页面
'''
@app.route('/log/')
def log():
    return render_template('log.html')


'''
上传日志文件插入数据库的内容
'''
@app.route('/log_count/', methods=['POST'])
def log_count():
    img = request.files.get('img')
    if img:
        filename=img.filename
        img.save(filename)
        log2db(filename)
        flash('上传成功!')
        return redirect('/log/')


'''
日志查看前端
'''
@app.route('/log_show/',methods=['GET','POST'])
def log_show():
    topn=request.args.get('topn',10)
    topn = int(topn)  if str(topn).isdigit() else 10
    rt_list = get_topn(topn=topn)
    return render_template('log_show.html',rt_list=rt_list)

'''
前端显示数据库日志
'''



'''
退出会话，清除session
'''
@app.route('/logout/')
def logout():
    session.clear()
    print session
    return redirect('/')


if __name__ == '__main__':
    app.run(host='0.0.0.0',port=9001,debug=True)