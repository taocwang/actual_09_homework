#encoding:utf-8
import os
import sys

from flask import Flask,render_template,request,redirect,session,url_for,flash
from flask.ext.bootstrap import Bootstrap
from flask.ext.moment import Moment

from logs import cretae_log
from user import user
from datetime import datetime

#
reload(sys)
sys.setdefaultencoding('utf8')
#解决字符串默认为ASCII编码的问题,导致输出中文为乱码

app = Flask(__name__)
app.secret_key = os.urandom(32)
bootstrap = Bootstrap(app)
moment = Moment(app)

@app.route('/')
def index():
    return render_template('login.html')

@app.route('/top10/')
def top10():
    topnum = 10
    a = '/home/jcui/files/www_access_20140823.log'
    title = 'Top %s ' % topnum
    rtlist = cretae_log.log_anslysis(sfile=a, topnum=topnum)
    return render_template('logs_top.html',title=title,rtlist=rtlist)
#--------------------------------------------------------------------------------------

@app.route('/tests/')
def test():
    return render_template('tests/test2.html',current_time=datetime.utcnow())

#--------------------------------------------------------------------------------------
@app.route('/top/')
def topn():
    topnum = request.args.get('top',10)
    topnum = int(topnum) if str(topnum).isdigit() else 10
    a = '/home/jcui/files/www_access_20140823.log'
    title = 'Top %s ' % topnum
    rtlist = cretae_log.log_anslysis(sfile=a, topnum=topnum)
    return render_template('logs_top.html', title=title, rtlist=rtlist)

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

@app.route('/user/',methods=['POST','GET'])
@user.login_check
def users():
    params = request.args if request.method == 'GET' else request.form
    if not params:
        print user.get_user()
        return render_template('users.html', user_list=user.get_user())
    elif request.method == 'GET':
        if user.user_update(params):
            username = params.get('username')
            return render_template('users.html', user_list=user.get_user())
    else:
        username = params.get('username')
        if user.user_add(params):
            return  render_template('users.html', user_list=user.get_user())
        elif not user.user_add(params):
            return  render_template('useradd.html',username=username,error='用户名已存在')

@app.route('/user/userdel/',methods=['POST','GET'])
@user.login_check
def user_del():
    params = request.args if request.method == 'GET' else request.form
    username = params.get('username')
    if user.user_del(username):
        flash("用户删除成功")
        return redirect('/user/')
    return render_template('users.html')

@app.route('/user/useradd/',methods=['POST','GET'])
@user.login_check
def users_add():
    flash("用户添加成功")
    return render_template('useradd.html')

@app.route('/user/userupdate/',methods=['POST','GET'])
@user.login_check
def user_update():
    params = request.args if request.method == 'GET' else request.form
    flash("用户更新成功")
    for i in user.get_user():
        print i
    return render_template('user_update.html',username=params.get('username'))


@app.route('/logout/')
def logout():
    session.clear()
    print session
    return redirect('/')
'''
添加用户,删除用户,更新用户,判断用户名是否重复
添加,删除用户需要输入相应的信息

更新用户操作
1. /user/find/?username={{username}}   userfind action
user
显示页面 render_template('user_update.html',user=user)
action =
'''

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=9000,debug=True)


'''
功能ok
建议：
1. 尽量一个功能写一个函数
原因：如果某个功能有问题，只用修改查找一个函数的代码，不会影响其他功能
     如果后续想要针对功能添加权限控制，不需要修改函数内代码
    a. app.route中定义的url以/结尾, 跳转url中未添加，flask程序会自动在跳转url后添加/，帮助解决问题
    b. app.route中定义的url未一/结尾，但是url中添加/，此时会报url找不到（404错误）

2. 建议app.route中的url和跳转的url建议都以/结尾，有两种情况
    可以自己测试下，所以个人建议都保持统一以/结尾
3. 用户修改的时候，可以在用户的修改表单中回显用户的数据，有时候只需要修改一两个属性，如果不回显，他需要填写错有的
对于不需要修改的，他还要去查找以前填写的什么
'''
