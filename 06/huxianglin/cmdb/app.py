#!/usr/bin/env python
# -*- coding: utf-8 -*-
from flask import Flask,render_template,request,redirect,session,url_for,flash
import loganalysis_v2
import userdb as user
from functools import wraps
import os
from datetime import timedelta
app=Flask(__name__)
app.secret_key = os.urandom(32)
'''
装饰器，目的：判断用户是否登录，如果没登录，直接跳转到登录界面
@wraps(func)的作用是假如使用装饰器的话，该函数的一些参数就变成了装饰器的参数，例如__name__等
使用该装饰器将修正该bug，改装时期需要在前面from functools import wraps导入该模块
'''
def login_required(func):
    @wraps(func)
    def wrapper(*args,**kwargs):
        if session.get('username') is None:
            print 'no session'
            return redirect(url_for('login',msg=u'请先登录'))
        rt=func(*args,**kwargs)
        return rt
    return wrapper

@app.route('/')
def index():
    if not 'username' in session:
        return redirect(url_for('login',msg=u'请先登录'))
    else:
        return redirect(url_for('users'))

'''
params = request.args if request.method == 'GET' else request.form
通过三目运算符实现动态匹配get和post请求
'''
@app.route('/log/',methods=['POST','GET'])
@login_required
def log():
    params = request.args if request.method == 'GET' else request.form
    topn=params.get('topn',10)
    topn=int(topn) if str(topn).isdigit() else 10
    rt_list=loganalysis_v2.sort_nginx(topn)
    if rt_list:
        return render_template('log.html',rt_list=rt_list,title="top"+str(topn))
    else:
        return "error"
'''
session.permanent = True开启这个参数之后，用户关闭浏览器该session不会被删除（默认为False）
app.permanent_session_lifetime = timedelta(minutes=10)设置session的超时时间为10分钟
session['username']=username登录用户生成session
'''
@app.route('/login/',methods=['POST','GET'])
def login():
    params = request.args if request.method == 'GET' else request.form
    username=params.get('username', '')
    password=params.get('password','')
    msg=params.get('msg','')
    if user.validate_user(username, password):
        session.permanent = True
        app.permanent_session_lifetime = timedelta(minutes=10)
        session['username']=username
        return redirect('/users/')
    else:
        return render_template('login.html',username=username,msg=msg)
'''
session.clear()清除该session，也可以通过session.pop()清除session，但是要知道session里面存储了什么东西
'''
@app.route('/logout/',methods=['GET','POST'])
def logout():
    session.clear()
    return redirect(url_for('login'))

@app.route('/users/')
@login_required
def users():
    params = request.args if request.method == 'GET' else request.form
    color=params.get('color','')
    Flag=params.get('Flag','')
    UserList=user.GetUsers()
    return render_template('users.html',color=color,Flag=Flag,userlist=UserList)

@app.route('/user/create/',methods=['POST','GET'])
@login_required
def usercreate():
    params = request.args if request.method == 'GET' else request.form
    msg=params.get('msg','')
    return render_template('createuser.html',msg=msg)

@app.route('/user/add/',methods=['POST','GET'])
@login_required
def useradd():
    params = request.args if request.method == 'GET' else request.form
    username,password,age=params.get('username',''),params.get('password',''),params.get('age','')
    Flag=user.JudgUser(username)
    if Flag:
        return redirect(url_for('usercreate',msg= u'抱歉，用户%s已经存在' %(username)))
    else:
        Flag=user.AddUser(username, password, age)
        if Flag:
            flash(u'用户%s添加成功' %(username))
            return redirect(url_for('users'))
            #return render_template('users.html',userlist=UserList,color='green',Flag=u'恭喜，添加成功')
        else:
            return redirect(url_for('usercreate',msg= u'抱歉，用户%s添加失败' %(username)))

@app.route('/user/modify/',methods=['GET'])
@login_required
def usermodify():
    id=request.args.get('id','')
    rt_list=user.GetUser(id)
    if rt_list:
        id,username,password,age=rt_list
        return render_template('modifyuser.html',id=id,username=username,password=password,age=age)
    else:
        return 'Error'

@app.route('/user/change/',methods=['POST','GET'])
@login_required
def userchange():
    params = request.args if request.method == 'GET' else request.form
    id,username,password,age=params.get('id',''),params.get('username',''),params.get('password',''),params.get('age','')
    Flag=user.ChangeUser(id,username, password, age)
    if Flag=='sameusername':
        rt_list=user.GetUser(id)
        password=rt_list[2]
        return render_template('modifyuser.html',id=id,username=username,password=password,age=age,msg=u'抱歉，用户%s已存在' %(username))
    elif Flag=='samepassword':
        rt_list=user.GetUser(id)
        password=rt_list[2]
        return render_template('modifyuser.html',id=id,username=username,password=password,age=age,msg=u'抱歉，用户%s修改后的密码不能和原密码相同' %(username))
    elif Flag:
        return redirect(url_for('users',color='green',Flag=u'恭喜，用户%s修改成功' %(username)))
    else:
        return render_template('modifyuser.html',error=u'抱歉，用户%s修改失败' %(username))

@app.route('/user/del/',methods=['GET'])
@login_required
def userdel():
    id=request.args.get('id','')
    rt_list=user.GetUser(id)
    username=rt_list[1]
    Flag=user.DelUser(id)
    if Flag:
        return redirect(url_for('users',color='green',Flag=u'恭喜，用户%s删除成功' %(username)))
    else:
        return redirect(url_for('users',color='red',Flag=u'抱歉，用户%s删除失败' %(username)))
    
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)