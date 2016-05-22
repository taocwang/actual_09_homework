#encoding:utf-8

from flask import Flask,render_template
import create_top

app = Flask(__name__)

@app.route('/')
def index():
    return 'hello world'


@app.route('/top10')
def top_page():
    topnum = 10
    a = '/home/jcui/files/www_access_20140823.log'
    b = '/home/jcui/files/top%s.html' % topnum
    return  create_top.log_anslysis(dfile=b,topnum=topnum,sfile=a)

@app.route('/user/<username>')
def user(username):
    return username

@app.route('/top/<topnum>')
def top_pages(topnum):
    topnum = int(topnum)
    a = '/home/jcui/files/www_access_20140823.log'
    b = '/home/jcui/files/top%s.html' % topnum
    c = create_top.log_anslysis(dfile=b, sfile=a ,topnum=topnum)
    return c
if __name__ == '__main__':
    app.run(host='127.0.0.1',port=9000,debug=True)