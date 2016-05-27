#!/usr/bin/env python
# -*- coding: utf-8 -*-
from flask import Flask, render_template, request, redirect
import user

# flask框架定义
app = Flask(__name__)

# 网站根目录
@app.route('/')
def index():
    # 访问根的时候直接进入登录页面
    return render_template('login.html')
    # return 'hello, Flask!'

# 登录页面
@app.route('/login/', methods=['POST', 'GET'])
def login():
    # 第一步：获取用户名和密码数据
    # if request.method == 'GET':
    #     params = request.args
    # else:
    #     params = request.form
    # if 简写方法：
    params = request.args if request.method == 'GET' else request.form
    username = params.get('username') # 获取用户提交的"username"参数
    password = params.get('password') # 获取用户提交的"password"参数

    # 第二步：登录验证，成功返回页面，失败给出提示
    if user.validate_login(username, password):
        print '登录成功'
        # return redirect('/logs/')
        return redirect('/users/')
    else:
        print '登录失败'
        return render_template('login.html', username=username, error=u'用户名或密码错误')

# 用户信息页面
@app.route('/users/')
def users():
    # print user.get_users()
    return render_template('users.html', user_list=user.get_users())

# 创建用户页面
@app.route('/user/create/')
def create():
    return render_template('adduser.html')

# 接收用户信息，将添加到user.json文件
@app.route('/user/add', methods=['POST', 'GET'])
def addUser():
    # 第一步：获取用户名，用于判断是否重复
    params = request.args if request.method == 'GET' else request.form
    username = params.get('username')
    age = params.get('age')
    password = params.get('password')
    # 第二步：判断用户是否存在，存在则提示，不存在则添加到user.json文件里
    if user.validate_find(username):
        # print '用户存在'
        return render_template('adduser.html', error=u'用户名存在，请重新输入')
    elif not username or not age or not password:
        return render_template('adduser.html', error=u'(用户名、年龄、密码)不能为空，请重新输入')
    else:
        # print '用户不存在, 请编写添加代码块'
        if user.add_users(username=username, age=age, password=password):
            return redirect('/users/')
        else:
            return '用户添加失败！'

# 更新用户信息页面
@app.route('/user/find/', methods=['GET'])
def finds():
    # 获取users.html用GET传过来的username信息
    username = request.args.get('username')
    return render_template('updateUser.html', username=username)

# 执行更新用户信息页面
@app.route('/user/update/', methods=['POST', 'GET'])
def update():
    # 获取用户更新信息，username作为唯一标识符，且不能更新
    username = request.args.get('username', '')
    age = request.form.get('age', '')
    password = request.form.get('password', '')
    # 更新操作代码块
    if not username or not age or not password:
        return render_template('updateUser.html', error=u'(年龄、密码)不能为空，请重新输入')
    elif user.update_users(username=username, age=age, password=password):
        return redirect('/users/')
    else:
        return "用户更新失败！"

# 删除用户信息
@app.route('/user/dele/')
def delete():
    username = request.args.get('username', '')
    return render_template('delUser.html', username=username)

@app.route('/user/delete/', methods=['POST', 'GET'])
def deleteUser():
    username = request.args.get('username', '')
    if user.del_users(username):
        # print '用户删除成功'
        return redirect('/users/')
    else:
        # print '用户删除失败'
        return render_template('delUser.html', user=username)

if __name__ == '__main__':
    app.run(port=8088, debug=True)