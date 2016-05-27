#!/usr/bin/env python
# -*- coding: utf-8 -*-
from flask import Flask,render_template,request,redirect
import loganalysis_v2
import user
import gconf
app=Flask(__name__)

@app.route('/')
def index():
    return render_template('login.html')

@app.route('/log/',methods=['POST','GET'])
def log():
    params = request.args if request.method == 'GET' else request.form
    topn=params.get('topn',10)
    topn=int(topn) if str(topn).isdigit() else 10
    SrcFileName='www_access_20140823.log'
    rt_list=loganalysis_v2.FilterNginx(SrcFileName,Num=topn)
    return render_template('log.html',rt_list=rt_list,title="top"+str(topn))

@app.route('/login/',methods=['POST','GET'])
def login():
    params = request.args if request.method == 'GET' else request.form
    username=params.get('username', '')
    password=params.get('password','')
    if user.validate_user(username, password):
        return redirect('/users/')
    else:
        return render_template('login.html',username=username,error=u'用户名或密码错误')

@app.route('/users/')
def users():
    UserList=user.GetUser(gconf.UserFile)
    return render_template('users.html',userlist=UserList)

@app.route('/user/create/')
def usercreate():
    return render_template('createuser.html')

@app.route('/user/add/',methods=['POST','GET'])
def useradd():
    params = request.args if request.method == 'GET' else request.form
    username,password,age=params.get('username',''),params.get('password',''),params.get('age','')
    Flag=user.JudgUser(username)
    print Flag
    if Flag:
        return render_template('createuser.html',userexist= u'抱歉，用户%s已经存在' %(username))
    else:
        Flag=user.AddUser(username, password, age)
        if Flag:
            UserList=user.GetUser(gconf.UserFile)
            return render_template('users.html',userlist=UserList,color='green',Flag=u'恭喜，添加成功')
        else:
            return render_template('createuser.html',userexist= u'抱歉，用户%s添加失败' %(username))

@app.route('/user/modify/',methods=['GET'])
def usermodify():
    username,password,age=request.args.get('username',''),request.args.get('password',''),request.args.get('age','')
    return render_template('modifyuser.html',username=username,password=password,age=age)

@app.route('/user/change/',methods=['POST','GET'])
def userchange():
    params = request.args if request.method == 'GET' else request.form
    username,password,age=params.get('username',''),params.get('password',''),params.get('age','')
    Flag=user.ChangeUser(username, password, age)
    if Flag=='samepassword':
        return render_template('modifyuser.html',username=username,password=password,age=age,samepassword=u'抱歉，用户%s修改后的密码不能和原密码相同' %(username))
    elif Flag:
        UserList=user.GetUser(gconf.UserFile)
        return render_template('users.html',userlist=UserList,color='green',Flag=u'恭喜，修改成功')
    else:
        return render_template('modifyuser.html',error=u'抱歉，用户%s修改失败' %(username))

@app.route('/user/del/',methods=['GET'])
def userdel():
    username=request.args.get('username','')
    Flag=user.DelUser(username)
    if Flag:
        UserList=user.GetUser(gconf.UserFile)
        return render_template('users.html',userlist=UserList,color='green',Flag=u'恭喜，用户%s删除成功' %(username))
    else:
        UserList=user.GetUser(gconf.UserFile)
        return render_template('users.html',userlist=UserList,color='red',Flag=u'抱歉，用户%s删除失败' %(username))
    
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
