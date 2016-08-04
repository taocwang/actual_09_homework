#!/bin/env python
#encoding:utf-8
import user
from user import view

if __name__ == '__main__':
    user.app.run(host='0.0.0.0',port=18018,debug=True)

