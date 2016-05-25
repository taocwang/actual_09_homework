from flask import Flask, render_template, request, redirect
import loganalysis
import user

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('login.html')


@app.route('/logs/')
def logs():
    logfile = '/Users/yang/PycharmProjects/app/www_access_20140823.log'
    topn = request.args.get('topn', 10)
    topn = int(topn) if str(topn).isdigit() else 10
    rt_list = loganalysis.get_topn(logfile=logfile, topn=topn)
    # return loganalysis.loganalysis(logfile=logfile)
    return render_template('logs.html', rt_list=rt_list, title='Log Topn')


@app.route('/login/', methods=['POST', 'GET'])
def login():
    try:
        params = request.args if request.method == 'GET' else request.form
        username = params.get('username', '')
        # print username
        password = params.get('password', '')
        # print password

        print user.validate_login(username, password)
        if user.validate_login(username, password):
            return redirect('/logs/')
        else:
            return render_template('login.html', username=username, error='username or password is error')
    except BaseException as e:
        print e
        return []


@app.route('/new_users/', methods=['POST', 'GET'])
def newuser():
    params = request.args if request.method == 'GET' else request.form
    username = request.form.get('username', '')
    password = request.form.get('password', '')
    age = request.form.get('age', '')
    if user.new_users(username, password, age):
        return render_template('new_users.html', useradd_info='New User [%s]is success.') % username
    else:
        return render_template('new_users.html', useradd_info='username or password or age is ERROR.')


@app.route('/users/')
def users():
    return render_template('users.html', user_list=user.get_users())


if __name__ == '__main__':
    app.run(host='192.168.1.106', port=9001, debug=True)
