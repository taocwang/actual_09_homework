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