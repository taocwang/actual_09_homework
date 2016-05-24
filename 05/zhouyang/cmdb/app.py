#coding:utf-8

from flask import Flask
from flask import render_template  #跳转到一个路由，执行路由下的整个def逻辑。与下面的redirect有区别！
from flask import request
from flask import redirect  #跳转到一个页面，不执行def逻辑

import sys
reload(sys)
sys.setdefaultencoding('utf8')


app=Flask(__name__)

@app.route('/')
def index():
    #return redirect('/login/')  不能这样转，这样会执行/login/的验证逻辑，所以会导致首页跳过去之后提示用户名错误信息。
    return render_template('login.html')

@app.route('/logs/')
def log_topn():
    log_file="www_access_20140823.log"

    cnt=request.args.get('topn',10)
    cnt= int(cnt) if str(cnt).isdigit() else 10

    import get_topn
    rt_list=get_topn.get_topn(log_file,cnt)
    return render_template('topn.html',n=cnt,rt_list=rt_list)

@app.route('/login/',methods=['GET','POST']) #不注明methods则默认是GET方法
def login():
    params=request.args if request.method == 'GET' else request.form
    username=params.get('username','')
    password=params.get('password','')
    import login
    if login.check_user(username,password):
        return redirect('/logs/')
    else:
        return render_template('login.html',username=username,error='您输入的用户名或密码错误!')

@app.route('/userinfo/')
def userinfo():
    import login
    import uconf
    user_list=login.get_users(uconf.user_conf)
    return render_template('show_users.html',user_list=user_list)

@app.route('/user/create/',methods=['GET','POST'])
def adduser():
    import adduser
    params=request.args if request.method == 'GET' else request.form
    username=params.get('username','')
    password=params.get('password','')
    age=params.get('age','')
    age=int(age) if str(age).isdigit() else ''
    if username and password and age:
        if adduser.adduser(username,password,age):
            return render_template('adduser.html',res='用户名注册成功')
        else:
            return render_template('adduser.html',fres='用户名已存在，请重新注册')
    else:
        return render_template('adduser.html',fres='注册信息不全，请重新注册',user=username)

@app.route('/usermodify/',methods=['GET','POST'])
def usermodify():
    '''这个有问题，搞不定'''
    import usermodify
    params=request.args if request.method == 'GET' else request.form
    username=params.get('username','')
    password=params.get('password','')
    age=params.get('age','')
    age=int(age) if str(age).isdigit() else ''
    usermodify.usermodify(username,password,age)
    return render_template('usermodify.html',username=username)



if __name__=='__main__':
    app.run(host='127.0.0.1',port=8080,debug=True)

