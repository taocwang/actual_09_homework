#encoding: utf-8

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

from user import app

if __name__ == '__main__':
        app.run(host='0.0.0.0',port=8888,debug=True)
