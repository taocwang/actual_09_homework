#！encoding:utf-8
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

from flask import Flask           #导入FlASK框架。
from flask import render_template  #导入模版加载函数
from flask import request  #导入请求对象
from flask import redirect #导入跳转函数
import  user               #导入user模版
from flask import session  #导入session模块适合字典一样的
import os
from functools import wraps #去掉装饰器的bug
from flask import flash

app = Flask(__name__)               #创建Flask对象
app.secret_key = os.urandom(32)     #生成sessionid

'''
装饰器验证的，session会话
'''
def login_request(func):
    @wraps(func)
    def wrapper(*args,**kwargs):
        if session.get('user') is None:
            return  redirect('/')
        rt = func(*args,**kwargs)
        return rt
    return wrapper




'''
接收path的URL，加载登陆界面
'''
@app.route('/')                  #帮顶处理url  path = / 的函数为index
def index():
    return render_template('login.html')





'''
接收path=/login/url,进行用户名密码验证。
'''
@app.route('/login/',methods=['POST']) #绑定处理url /login的函数为index
def login():
    username = request.form.get('username','')
    password = request.form.get('password','')
    if   user.validate_login(username,password):
        session['user'] = {'username':username}
        return redirect('/users/')
    else:
        return render_template('login.html',username=username,error='用户或密码错误')





'''
显示用户列表信息
'''
@app.route('/users/')
@login_request
def users():
    users = user.get_users()
    return render_template('users.html',users=users)





'''
显示用户添加表单
'''
@app.route('/user/create/')
@login_request
def create_user():
    return render_template('user_create.html')




'''
用户添加操作的模块
'''
@app.route('/user/add/',methods=['POST'])
@login_request
def add_user():
    username = request.form.get('username','')
    password = request.form.get('password','')
    age = request.form.get('age','')
    _is_ok,_error = user.validate_add_user(username,password,age) #检查用户信息

    if _is_ok:
        user.add_user(username,password,age)   #添加用户
        flash('添加信息成功!')
        return  redirect('/users/')   #跳转用户列表
    else:
        return render_template('user_create.html',username=username,password=password,age=age,error=_error)





'''
删除用户用户操作模块
'''
@app.route('/user/delete/')
def delete_user():
    id = request.args.get('id')
    user.delete_user(id)
    flash('删除用户成功!')
    return redirect('/users/')





'''
显示更新修改用户表单
'''
@app.route('/user/modify/')
@login_request
def modify_user():
   id = request.args.get('id','')
   _user = user.get_user(id)
   _error = ''
   _username = ''
   _password = ''
   _age = ''
   if _user is None:
       _error = '用户信息不存在'
   else:
       _username = _user.get('username')
       _password = _user.get('password')
       _age = _user.get('age')


   return render_template('user_modify.html',error=_error,id=id,username=_username,password=_password,age=_age)





'''
更新修改用户信息操作模块
'''
@app.route('/user/update/',methods=['POST','GET'])
@login_request
def update_user():
       id = request.form.get('id','')
       username = request.form.get('username','')
       password = request.form.get('password','')
       age = request.form.get('age','')
       print id,username,password,age
       _is_ok,_error = user.validate_update_user(username,password,age,id)
       print _is_ok,_error
       if _is_ok:
           user.update_user(username,password,age,id)
           flash('更新用户成功!')
           return redirect('/users/')
       else:
           return render_template('user_modify.html',error=_error,id=id,username=username,password=password,age=age)




'''
查询用户信息分别年龄和用户名都可以查询
'''
@app.route('/user/query/',methods=['POST','GET'])
@login_request
def query_user():
    user_n_a=request.form.get('user_n_a')
    if str(user_n_a).isdigit():
        users = user.query_user(age=user_n_a)
        return render_template('users.html',users=users)
    else:
        if user.query_user(user_n_a) is False:
            return render_template('users.html',users=[],error="用户不存在或者您的查询方式不对!")
        else:
            users = [user.query_user(user_n_a)]
            print users
            return render_template('users.html',users=users)




'''
进行用户列表排序(升序或者是倒序)
'''
@app.route('/user/order/')
@login_request
def sort_user():
    desc_asc = request.args.get('order')
    print desc_asc
    if desc_asc == 'desc':
        users = user.sort_user(desc_asc)
    else:
        users = user.sort_user('asc')
    return render_template('users.html',users=users)




'''
进行日志数据前台进行展示
'''
@app.route('/log/',methods=['GET','POST'])
@login_request
def select_log():
    if request.method == 'GET':
        params = request.args
    else:
        params = request.form
    id_c = params.get('id_c',100)
    print id_c
    rt_list = user.select_log(id_c=id_c)
    if not str(id_c).isdigit():
        errors = '你输入的不正确!'
        return render_template('log.html',users=rt_list,error=errors)
    return render_template('log.html',users=rt_list)




'''
退出会话，清除session。
'''
@app.route('/logout/')
def logout():
    session.clear()
    return redirect('/')



if __name__ == '__main__':
    app.run(host='0.0.0.0',port=8080,debug=True)