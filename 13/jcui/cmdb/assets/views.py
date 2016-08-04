#encoding:utf-8

from assets import app

@app.route('/assets_test/')
def assets():
    return 'assets'