#encoding: utf-8

from cmdb import views

if __name__ == '__main__':
    views.app.run(host='0.0.0.0', port=9001, debug=True)
