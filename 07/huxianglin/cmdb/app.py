#!/usr/bin/env python
# -*- coding: utf-8 -*-
from flask import Flask,render_template,request,redirect,session,url_for,flash
import loganalysis_v2
import userdb as user
import time
import logfile_inputdb
from functools import wraps
import os
from datetime import timedelta
app=Flask(__name__)
app.secret_key = os.urandom(32)
'''
app.permanent_session_lifetime = timedelta(minutes=10)设置session的超时时间为一天
'''
app.permanent_session_lifetime = timedelta(seconds=24 * 60 * 60)
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
        return render_template('log.html',username=session.get('username',''),privilege=session.get('privilege',''),\
                               rt_list=rt_list,pageheader=u'Nginx访问日志top%s' %(topn))
    else:
        return "error"

@app.route('/uploadlog/')
@login_required
def uploadlog():
    return render_template('uploadlog.html',username=session.get('username',''),privilege=session.get('privilege',''),\
                           pageheader=u'Nginx日志上传')

@app.route('/updatelog/',methods=['POST'])
@login_required
def updatelog():
    _file=request.files.get('logfile')
    if _file:
        _filepath='upload/%s.log' % time.time()
        _file.save(_filepath)
        Flag=logfile_inputdb.FilterNginx(_filepath)
    if Flag:
        return render_template('uploadlog.html',username=session.get('username',''),privilege=session.get('privilege',''),\
                           pageheader=u'Nginx日志上传',Flag=u'Nginx日志上传成功',color='alert-success')
    else:
        return render_template('uploadlog.html',username=session.get('username',''),privilege=session.get('privilege',''),\
                           pageheader=u'Nginx日志上传',Flag=u'Nginx日志上传失败',color='alert-danger')

'''
session.permanent = True开启这个参数之后，用户关闭浏览器该session不会被删除（默认为False）
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
        session['username']=username
        session['privilege']=user.GetPrivilege(username)
        return redirect('/users/')
    elif username or password:
        return render_template('login.html',msg=u'用户名或密码错误')
    else:
        return render_template('login.html',msg=msg)
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
    return render_template('users.html',pageheader=u'用户信息列表',UserList=UserList,\
                           username=session.get('username',''),privilege=session.get('privilege',''),\
                           color=color,Flag=Flag)

@app.route('/user/create/',methods=['POST','GET'])
@login_required
def usercreate():
    params = request.args if request.method == 'GET' else request.form
    msg=params.get('msg','')
    return render_template('createuser.html',pageheader=u'添加用户',username=session.get('username',''),\
                           privilege=session.get('privilege',''),msg=msg)

@app.route('/user/add/',methods=['POST','GET'])
@login_required
def useradd():
    params = request.args if request.method == 'GET' else request.form
    username,password,age,privilege=params.get('username',''),params.get('password',''),\
                                    params.get('age',''),params.get('privilege','')
    Flag=user.JudgUser(username)
    if Flag:
        return redirect(url_for('usercreate',msg= u'抱歉，用户%s已经存在' %(username)))
    else:
        Flag=user.AddUser(username, password, age,privilege)
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
        id,username,password,age,privilege=rt_list
        return render_template('modifyuser.html',username=session.get('username',''),\
                               privilege=session.get('privilege',''),modifyid=id,modifyusername=username,\
                               modifypassword=password,modifyage=age,modifyprivilege=privilege,\
                               pageheader=u'修改用户信息')
    else:
        return 'Error'

@app.route('/user/change/',methods=['POST','GET'])
@login_required
def userchange():
    params = request.args if request.method == 'GET' else request.form
    id,username,password,age,privilege=params.get('id',''),params.get('username',''),params.get('password',''),\
                             params.get('age',''),params.get('privilege','')
    Flag=user.ChangeUser(id,username, password, age,privilege)
    if Flag=='sameusername':
        # rt_list=user.GetUser(id)
        # password=rt_list[2]
        return render_template('modifyuser.html',username=session.get('username',''),\
                               privilege=session.get('privilege',''),modifyid=id,modifyusername=username,\
                               modifypassword=password,modifyage=age,modifyprivilege=privilege,\
                               msg=u'抱歉，用户%s已存在' %(username),pageheader=u'修改用户信息')
    elif Flag=='samepassword':
        rt_list=user.GetUser(id)
        password=rt_list[2]
        return render_template('modifyuser.html',username=session.get('username',''),\
                               privilege=session.get('privilege',''),modifyid=id,modifyusername=username,\
                               modifypassword=password,modifyage=age,modifyprivilege=privilege,\
                               msg=u'抱歉，用户%s修改后的密码不能和原密码相同' %(username),\
                               pageheader=u'修改用户信息')
    elif Flag:
        return redirect(url_for('users',color='alert-success',Flag=u'恭喜，用户%s修改成功' %(username)))
    else:
        return render_template('modifyuser.html',username=session.get('username',''),\
                               privilege=session.get('privilege',''),modifyid=id,modifyusername=username,\
                               modifypassword=password,modifyage=age,modifyprivilege=privilege,\
                               msg=u'抱歉，用户%s修改失败' %(username),\
                               pageheader=u'修改用户信息')

@app.route('/user/del/',methods=['GET'])
@login_required
def userdel():
    id=request.args.get('id','')
    rt_list=user.GetUser(id)
    username=rt_list[1]
    Flag=user.DelUser(id)
    if Flag:
        return redirect(url_for('users',color='alert-success',Flag=u'恭喜，用户%s删除成功' %(username)))
    else:
        return redirect(url_for('users',color='alert-danger',Flag=u'抱歉，用户%s删除失败' %(username)))
    
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)