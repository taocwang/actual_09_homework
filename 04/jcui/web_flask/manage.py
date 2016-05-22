#encoding:utf-8
from flask import Flask,render_template,request,redirect

from logs import cretae_log
from user import user

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
        return redirect('/users/')
    else:
        return render_template('login.html',username=username,error='user or pass error')

@app.route('/users/')
def users():
    return render_template('users.html', user_list=user.get_user())

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
