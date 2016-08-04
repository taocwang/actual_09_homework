#encoding:utf-8


from flask import Blueprint

app = Blueprint('assets',__name__,url_prefix='/assets')

import views