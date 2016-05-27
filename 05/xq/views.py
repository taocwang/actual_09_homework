#!/usr/bin/env python
#encoding:utf-8
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

from flask import request,redirect,flash,render_template
from app import app
from app import mylog
import user

@app.route('/')
def index():
    return render_template('login.html')

@app.route('/<string:name>')
def test(name):
    return '<h1>hello,%s</h1>' %name

@app.route('/index2/')
def main():
    print request.args
    count = request.args.get('count',10)
    count = int(count) if str(count).isdigit() else 10
    user1 = mylog.get_sum('./app/www_access_20140823.log',count)
    return render_template("index2.html",count = count,user1 = user1)

@app.route('/login/',methods=['POST','GET'])
def login():
    params = request.args if request.method == 'GET' else request.form
    username =  params.get('username','')
    password =  params.get('password','')
    print type('age')
    if user.validate_login(username,password):
        flash("%s,欢迎回来！" %username )
        return redirect('/show/')
    else:
        flash("用户名或密码错误，请重新输入！")
        #return render_template('login.html',username=username,error='用户名或密码错误，请重新输入!')
        return render_template('login.html',username=username)

@app.route('/show/')
def show_user():
    user_list = user.get_user()
    #print user_list
    return render_template("showuser.html",user_list=user_list)

@app.route('/user/add/',methods=['POST','GET'])
def add_user():
    params = request.args if request.method == 'GET' else request.form
    if request.method == 'GET':
         return render_template("adduser.html")
    else:
        username =  params.get('username','')
        password =  params.get('password','')
        age =  params.get('age','')
        if user.add_user(username,password,age):
            flash("%s添加成功！" %username)
            return redirect('/show/')
        else:
            return render_template("adduser.html",error="用户已存在或为空，请重新添加！")
@app.route('/user/modify/',methods=['POST','GET'])
def mod_user():
    params = request.args if request.method == 'GET' else request.form
    if request.method == 'GET':
        global username1
        global password1
        global age1
        username = params.get('username','')
        password = params.get('password','')
        age = params.get('age','')
        username1 = username
        password1 = password
        age1  = age
        return render_template("modifyuser.html",username=username,password=password,age=age)
    else:
        username =  params.get('username','')
        password =  params.get('password','')
        age =  params.get('age','') 
        print "New:%s-%s-%s" %(username,password,age)
        print "Old:%s-%s-%s" %(username1,password1,age1)
        if username != username1 and user.modify_user(username,password,age) != 'flag':
            if user.del_user(username1,password1,age1):
                flash("%s的信息已修改成功！" %username1)
                if user.modify_user(username,password,age):
                    return redirect('/show/')
                else:
                    return render_template("modifyuser.html",error="修改失败！")
        elif user.modify_user(username,password,age) == 'flag':
            flash("修改失败，用户名已存在！")
            return redirect("/show/")
        else:
            if user.modify_user(username,password,age) == 'same':
                flash("%s信息没有变化！" %username)
                return redirect('/show/')
            elif user.modify_user(username,password,age):
                flash("%s修改成功！" %username)
                return redirect('/show/')
            return render_template("modifyuser.html",error="修改失败！")
@app.route('/user/del/',methods=['POST','GET'])
def del_user():
    username = request.args.get('username','')
    password =  request.args.get('password','')
    age =  request.args.get('age','')
    if user.del_user(username,password,age):
       flash("%s删除成功！" %username)
       return redirect('/show/')
    return render_template("showuser.html",error="删除失败！")

@app.route('/user/find/',methods=['POST','GET'])
def finder_user():
    username = str(request.form.get('username',''))
    new_user = user.find_user(username)
    #print new_user
    if user.find_user(username):
        return render_template('finduser.html',new_user = new_user)
    flash("Sorry，没有查到相关数据!")
    return render_template('finduser.html')

@app.route('/user/logout/',methods=['POST','GET'])
def login_out():
    return render_template('login.html')
