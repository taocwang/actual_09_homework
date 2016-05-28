#encoding:utf-8
from flask import Flask
from flask import render_template,request,redirect
from uservalid import uservalid
from uservalid import get_user
import useradd
import userdel
import userupdate
import userquery
import json

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')
@app.route('/user/',methods = ['GET','POST'])
def user():
    if request.method == 'GET':
        params = request.args
    else:
        params = request.form
    username = params.get('username')
    password = params.get('password')
    if uservalid(username,password):
        return redirect('/userlist/')
    else:
        return render_template('index1.html',username=username,error='Your Username or Password is error!')
@app.route('/userlist/',methods=['GET','POST'])
def userlist():
    userlist=get_user()
    return render_template('admin_list.html',userlist=userlist)
@app.route('/useradd_l/',methods=['GET','POST'])
def useradd_l():
    return render_template('admin_add.html')
@app.route('/useradd/',methods=['GET','POST'])
def useradda():
    if request.method == 'GET':
        params = request.args
    else:
        params = request.form
    username = params.get('username')
    password = params.get('password')
    telephone =params.get('telephone')
    mail = params.get('mail')
    usertel = params.get('usertel')
    name = params.get('name')
    if params.get('adminrole') == '0':
        adminrole = '长官'
    elif params.get('adminrole') == '1':
        adminrole = '排长'
    elif params.get('adminrole') == '2':
        adminrole = '排长'
    else:
        adminrole = '工兵'
    if useradd.useradd(username,password,telephone,mail,usertel,name,adminrole):
        return redirect('/userlist/')
    return render_template('admin_add.html',error='username User repeat!')
@app.route('/userdel/',methods=['GET','POST'])
def userdela():
     if request.method == 'GET':
        params = request.args
     else:
        params = request.form
     username = params.get('username')
     if userdel.userdel(username):
         return redirect('/userlist/')
     else:
         return 'user is Invalid user'
@app.route('/userupdatemo/',methods=['GET','POST'])
def userupdatea():
    return render_template('change_password.html')
@app.route('/userupdate/',methods=['GET','POST'])
def update():
     if request.method == 'GET':
        params = request.args
     else:
        params = request.form
     username = params.get('username')
     if params.get('newpassword') == params.get('newpassword2'):
           password = params.get('newpassword2')
           if userupdate.userupdate(username,password):
              return redirect('/')
           else:
              return render_template('change_password.html',error='not user exist')
     else:
         return render_template('change_password.html',error='Two passwords are different!')

@app.route('/userquery/',methods=['GET','POST'])
def userquerya():
    if request.method == 'GET':
        params = request.args
    else:
        params = request.form
    username = params.get('query')
    if userquery.userquery(username):
        userquery_dict = userquery.userquery_get(username)
        return render_template('admin_query.html',userlist=userquery_dict)
    else:
        return render_template('admin_list.html',error='The user you entered does not exist')

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=8080,debug=True)

'''
功能ok
建议
1. 函数和函数之间间隔2个空行
2. 模块是将一些相同功能或操作对象的函数封装成一个文件，增、删、改、差都是对user的操作，可以放在一个文件中
    如果都一模块划分，那和所有的函数都写在文件中没有区别（写在文件中还能方便一次性阅读）
3. 既然读取用户信息的代码写成了函数，那存储的呢
    增、删、改都需要对文件修改，代码都是一样的，能否改写成一个函数提供功能呢

4. 用户修改的时候，可以在用户的修改表单中回显用户的数据，有时候只需要修改一两个属性，如果不回显，他需要填写错有的
对于不需要修改的，他还要去查找以前填写的什么
'''
