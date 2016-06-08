#encoding:utf-8
import os
import sys
import random
import string

from flask import Flask,render_template,request,redirect,session, flash

from modules import user,logs

#
reload(sys)
sys.setdefaultencoding('utf8')
#解决字符串默认为ASCII编码的问题,导致输出中文为乱码

app = Flask(__name__)
# app.secret_key = os.urandom(32)
app.secret_key = 'asdasd2342tdasfdasfasdasds'

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
    if user.user_del(int(id),username):
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
    id = params.get('id')
    if request.method == 'GET':
        users = user.get_alone_user(int(id))
        username = users.get('username')
        age = users.get('age')
        telphone = users.get('telphone')
        email = users.get('email')
        return render_template('userupdate.html', id=id,username=username, age=age, telphone=telphone, email=email)
    if user.user_update(params):
        flash("用户更新成功")
        return redirect('/user/')
    return render_template('userupdate.html',error='更新失败')

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


#test
# @app.route('/test/',methods=['POST','GET'])
# def test():
#     print request.form
#     print request.args
#     print request.files
#     # print request.header
#     return render_template('user.html',user_list=user.get_user())
'''
登出用户
'''
@app.route('/logout/')
def logout():
    session.clear()
    return redirect('/')

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=9000,debug=True)

