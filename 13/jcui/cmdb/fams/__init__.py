#encoding:utf-8

from flask import Blueprint

bp = Blueprint('fams',__name__,url_prefix='/fams',template_folder='templates/fams',static_folder='static',)

import views