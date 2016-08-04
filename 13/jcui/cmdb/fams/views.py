#encoding:utf-8

from fams import bp
from flask import render_template

@bp.route('/bp_test/')
def bp_test():
    return render_template('test.html')