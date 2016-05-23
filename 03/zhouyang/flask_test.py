#coding:utf-8
'''展示log'''
from flask import Flask

app=Flask(__name__)

def hello():
    return "index hello zy"

@app.route("/logs")
def topn_log():
    import nginx_log_v3
    return nginx_log_v3.topn_web_file()

if __name__ == "__main__":
    app.run(host='0.0.0.0',port=18081,debug='True')