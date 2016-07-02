#coding:utf-8
'''路由映射模块'''
from flask import render_template  #跳转到一个路由，执行路由下的整个def逻辑。与下面的redirect有区别！
from flask import request
from flask import redirect  #跳转到一个页面，不执行def逻辑
from flask import session
from functools import wraps  #解决多层装饰器中，上层会错误的获取到下层装饰器的__name__的bug
from flask import flash  #消息闪现
import json
from user import app

import sys
reload(sys)
sys.setdefaultencoding('utf8')

def checkinfo(func):
    '''装饰器，验证用户信息'''
    @wraps(func)
    def wrapper(*args,**kwargs):
        if not session.get('user'):
            return render_template('login.html')
        rt=func()
        return rt
    return wrapper

@app.route('/')
@checkinfo
def index():
    #return redirect('/login/')  不能这样转，这样会执行/login/的验证逻辑，所以会导致首页跳过去之后提示用户名错误信息。
    return render_template('index.html')

@app.route('/logs/')
@checkinfo
def log_topn():
    cnt=request.args.get('topn',10)
    cnt= int(cnt) if str(cnt).isdigit() else 10

    import get_topn
    rt_list=get_topn.get_topn(cnt)
    return render_template('topn_v2.html',n=cnt,rt_list=rt_list)

@app.route('/login/',methods=['GET','POST']) #不注明methods则默认是GET方法
def login():
    params=request.args if request.method == 'GET' else request.form
    username=params.get('username','')
    password=params.get('password','')
    #import login
    import userdb as login
    if login.check_user(username,password):
        session['user']={'username':username}  #用户信息验证通过后，将信息存储到session中
        flash('登陆成功')
        return redirect('/')
    else:
        return render_template('login.html',username=username,error='您输入的用户名或密码错误!')

@app.route('/userinfo/')
@checkinfo
def userinfo():
    #print session
    import userdb as login
    import uconf
    user_list=login.get_users()
    #return render_template('show_users.html',user_list=user_list)
    #return render_template('show_users_v2.html',user_list=user_list)
    return render_template('users.html',user_list=user_list)

@app.route('/readytoadduser/',methods=['POST','GET'])
def readytoadduser():
    return render_template('user_create.html')

@app.route("/user/add/",methods=['POST','GET'])
def user_add():
    params=request.args if request.method == 'GET' else request.form
    import users
    _is_ok,msg=users.create_user(params)
    return json.dumps({'_is_ok':_is_ok,'msg':msg})


@app.route('/user/create/',methods=['GET','POST'])
def adduser():
    import adduser
    params=request.args if request.method == 'GET' else request.form
    username=params.get('username','')
    password=params.get('password','')
    age=params.get('age','')
    age=int(age) if str(age).isdigit() else ''
    gender=params.get('gender','1')
    hobby=params.getlist('hobby')
    department=params.get('department')
    remark=params.get('remark')
    img=request.files.get('img')
    if img:
        print img.filename
        img.save('d:\zz.txt')
    print 'gender %s\n hobby %s\n department %s\n remark %s\n img %s' % (gender,hobby,department,remark,img)
    if username and password and age:
        if adduser.adduser(username,password,age):
            flash('用户注册成功')  #消息闪现方式
            return render_template('readytoadduser_v2.html')
            #return render_template('adduser.html',res='用户名注册成功')  #传参渲染方式
        else:
            #return render_template('adduser.html',fres='用户名已存在，请重新注册')
            flash('用户名已存在，请重新注册')
            return render_template('readytoadduser_v2.html')
    else:
        flash('请写全注册信息!')
        return render_template('readytoadduser_v2.html')

@app.route('/userdel/',methods=['GET','POST'])
@checkinfo
def userdel():
    import userdel
    params=request.args if request.method == 'GET' else request.form
    username=params.get('username','')
    if username == session.get('user')['username']:
        if userdel.userdel(username) == 0:
            return "该用户不存在！"
        else:
            flash('用户%s删除成功' % username)
            return redirect('/userinfo/')
    else:
        return "无权限删除其他用户！"

@app.route('/readytousermodify/',methods=['GET','POST'])
@checkinfo
def readytousermodify():
    username=request.args.get('username','')
    if username == session.get('user')['username']:
        return render_template('usermodify.html',params=username)
    else:
        return "无权限修改其他用户！"

@app.route("/user/modify/",methods=['GET','POST'])
@checkinfo
def user_modify():
    params=request.args if request.method == 'GET' else request.form
    username=params.get('username')
    old_passwd=params.get('password')
    new_passwd=params.get('new_password')
    try_passwd=params.get('try_password')
    age=params.get('age')
    import users
    _is_ok,msg=users.update_user(username,old_passwd,new_passwd,try_passwd,age)
    return json.dumps({'_is_ok':_is_ok,'msg':msg})

@app.route('/logout/')
def logout():
    session.clear()
    return render_template('login.html')

@app.route('/upload/')
@checkinfo
def upload_file():
    '''文件上传'''
    return render_template('upload_file.html')

@app.route('/upload_ok/',methods=['GET','POST'])
@checkinfo
def upload_ok():
    _file_name=''
    save_path="d:\\tmp"
    _file=request.files.get('re_file')
    if _file:
        _file_name = _file.filename
        _file.save('%s\%s' % (save_path,_file_name))
        flash('文件%s上传成功' % _file_name )
    else:
        flash('文件%s上传失败！'% _file_name)
    return redirect('/upload/')

@app.route('/assets/')
def assets():
    import assets
    _assets=assets.get_list()
    return  render_template('assets.html',_assets=_assets)

@app.route('/assets/create/',methods=['POST','GET'])
def create_asset():
    idcs=[('1','北京-亦庄DC1楼'),('2','深圳-沙河西1楼')]
    return render_template('asset_create.html',idcs=idcs)

@app.route('/asset/add/',methods=['POST','GET'])
def asset_add():
    import assets
    params=request.args if request.method == 'GET' else request.form
    is_ok,error = assets.validate_create(params)
    if is_ok:
        if assets.create(params):
            return json.dumps({'_is_ok':1,'msg':'添加成功'})
        else:
            return json.dumps({'_is_ok':0,'msg':'数据录入失败，请检查资产唯一性！'})
    else:
        return json.dumps({'_is_ok':0,'msg':error})

@app.route('/assets/update/',methods=['POST','GET'])
def update_asset():
    params=request.args if request.method == 'GET' else request.form
    se_sn=params.get('sn')
    import assets
    asset_info_dict=assets.get_by_id(se_sn)
    return render_template('asset_update.html',params=asset_info_dict)

@app.route('/asset/modify/',methods=['POST','GET'])
def modify_asset():
    params=request.args if request.method == 'GET' else request.form
    ram=params.get('ram')
    cpu=params.get('cpu')
    disk=params.get('disk')
    admin=params.get('admin')
    ip=params.get('ip')
    sn=params.get('sn')
    import assets
    if assets.validate_update(ip):
        if assets.update(sn,ip,cpu,ram,disk,admin):
            return json.dumps({'_is_ok':1,'msg':'修改成功'})
        else:
            return json.dumps({'_is_ok':0,'msg':'数据录入失败，请检查资产唯一性！'})
    else:
        return json.dumps({'_is_ok':0,'msg':error})

@app.route('/asset/delete/',methods=['POST','GET'])
def asset_del():
    params=request.args if request.method == 'GET' else request.form
    del_sn=params.get('sn')
    import assets
    if assets.delete(del_sn):
        return json.dumps({'_is_ok':1,'msg':'删除成功'})
    else:
        return json,dumps({'_is_ok':0,'msg':'删除失败'})
