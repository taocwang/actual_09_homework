#!/bin/env python
#encoding:utf-8
import user
from user import view

if __name__ == '__main__':
    user.app.run(host='192.168.0.102',port=8080,debug=True)