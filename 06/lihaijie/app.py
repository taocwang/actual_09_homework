#encoding:utf-8
import sys,os,loganalysis
import userdb as user
reload(sys)
sys.setdefaultencoding("utf-8")
from flask import Flask,render_template,request,redirect,session,url_for,flash
from functools import wraps
app = Flask(__name__)
app.secret_key = os.urandom(32)

def login_required(func):
    @wraps(func)
    def wrapper(*args,**kwargs):
        if session.get("user")is None:
            return redirect("/")
        rt = func(*args,**kwargs)
        return rt
    return wrapper

@app.route("/")
def index():
    return render_template("login.html")


@app.route("/login/",methods=["POST","GET"])
def login():
    params =request.args if request.method == "GET" else request.form
    username = params.get("username")
    password = params.get("password")
    if user.validate_login(username,password):
        session["user"] = {"username":username,"password":password}
        return redirect("/users/")
    else:
        return render_template("login.html",username=username,error="username or password is error")

@app.route("/logout/")
def logout():
    # print session
    session.clear()
    return redirect("/")

@app.route("/users/")
@login_required
def get_user():
    print session
    if session.get("user")is None:
        return redirect("/")
    users =user.get_users()
    return render_template("users.html",users=users)

@app.route("/user/create/")
@login_required
def create_user():
    return render_template("user_create.html")

@app.route("/user/add/",methods=["POST"])
@login_required
def add_user():
    username= request.form.get("username","")
    password= request.form.get("password","")
    age= request.form.get("age","")
    _is_ok,_error = user.validate_add_user(username,password,age)
    if _is_ok:
        user.add_user(username,password,age)
        flash("添加用户信息成功")
        return redirect('/users/')
    else:
        return render_template('user_create.html', info=_error)

@app.route("/user/modify/")
@login_required
def modify_user():
    uid=int(request.args.get("id",""))
    _user = user.get_user(uid)
    _id=""
    _username=""
    _password=""
    _age=""
    _error=""
    if _user is None:
        _error = "user is no exists"
    else:
        _id = _user.get("id")
        _username = _user.get("username")
        _password = _user.get("password")
        _age = _user.get("age")
        # print _username,_password,_age
    return render_template("user_modify.html",uid=_id,username=_username,\
                           password=_password,age=_age,info=_error)

@app.route("/user/update/",methods=["POST"])
@login_required
def update_user():
    uid=request.form.get("uid")
    username=request.form.get("username")
    password=request.form.get("password")
    age=request.form.get("age")
    # print uid,username,password,age
    _is_ok, _error = user.validate_update_user(uid, username, password, age)
    # print _is_ok, _error
    if _is_ok:
        user.update_user(uid, username, password, age)
        flash("修改用户信息成功")
        return redirect('/users/')
    else:
        return render_template("user_modify.html",username=username,\
                           _password=password,age=age,info=_error)


@app.route("/user/delete/")
@login_required
def delete_user():
    uid=int(request.args.get("id"))
    user.delete_user(uid)
    flash("删除用户成功")
    return redirect('/users/')

@app.route("/logs/",methods=["GET","POST"])
@login_required
def logs():
    params =request.args if request.method == "GET" else request.form
    topn = params.get("topn",10)
    _is_ok, _error = user.validate_topn(topn)
    # print _is_ok, _error
    if not _is_ok:
        rt_list=user.logs_from_db(10)
        return render_template("logs.html",rt_list=rt_list,error=_error)
    else:
        rt_list=user.logs_from_db(int(topn))
        return render_template("logs.html",rt_list=rt_list)
    # print rt_list
    # src_log = '/www_access_20140823.log'
    # topn = request.args.get("topn",10)
    # # print type(topn)
    # topn = int(topn)if str(topn).isdigit else 10
    # rt_list = loganalysis.get_topn(srcpath=src_log,topn=topn)
    # # ctx="".join(rt_list[0][0])
    # # return ctx

# @app.route("/user/check/",methods=["POST","GET"])
# def check_username():
#     username = request.form.get("username","")
#     if user.check_username(username):
#         return render_template("user_create.html",info="username is register")
#     else:
#         return render_template("user_create.html",info="username can register")
# @app.route("/register/",methods=["POST","GET"])
# def register():
#     params =request.args if request.method == "GET" else request.form
#     username = params.get("username")
#     password = params.get("password")
#     age = params.get("age")
#     if user.validate_register(username,password,age):
#         return render_template("register.html",info="User name already exists")
#     else:
#         return render_template("register.html",info="register sucess")
if __name__ == "__main__":
    app.run(host="0.0.0.0",port=9001,debug=True)