#encoding:utf-8
from flask import Flask
import os


app = Flask(__name__)                                       #生成Flask框架的对象
app.secret_key=os.urandom(32)                               #设定session_id


import views

