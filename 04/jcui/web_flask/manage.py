#encoding:utf-8
from flask import Flask,render_template,request,redirect
import sys

from logs import cretae_log
from user import user

#
reload(sys)
sys.setdefaultencoding('utf8')
#解决字符串默认为ASCII编码的问题,导致输出中文为乱码

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('login.html')

@app.route('/top10/')
def top10():
    topnum = 10
    a = '/home/jcui/files/www_access_20140823.log'
    title = 'Top %s ' % topnum
    rtlist = cretae_log.log_anslysis(sfile=a, topnum=topnum)
    return render_template('top.html',title=title,rtlist=rtlist)


@app.route('/top/')
def topn():
    print request.args
    topnum = request.args.get('top',10)
    topnum = int(topnum) if str(topnum).isdigit() else 10
    a = '/home/jcui/files/www_access_20140823.log'
    title = 'Top %s ' % topnum
    rtlist = cretae_log.log_anslysis(sfile=a, topnum=topnum)
    return render_template('top.html', title=title, rtlist=rtlist)

@app.route('/login/',methods=['POST','GET'])
def login():
    params = request.args if request.method == 'GET' else request.form
    username = params.get('username','')
    password = params.get('password','')
    if user.validate_login(username, password):
        return redirect('/user/')
    else:
        return render_template('login.html',username=username,error='用户名或密码错误')

@app.route('/user/',methods=['POST','GET'])
def users():
    params = request.args if request.method == 'GET' else request.form
    if not params:
        return render_template('users.html', user_list=user.get_user())
    else:
        username = params.get('username','')
        if user.user_add(params):
            return  render_template('users.html',success='添加成功',user_list=user.get_user())
        elif not user.user_add(params):
            return  render_template('useradd.html',username=username,error='用户名已存在')


@app.route('/user/useradd',methods=['POST','GET'])
def users_add():
    return render_template('useradd.html')


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
    app.run(host='127.0.0.1',port=9000,debug=True)
