#!/bin/env python
#coding:utf-8
import hashlib

def md5_str(some_str):
    _md5=hashlib.md5()
    _md5.update(some_str)
    return _md5.hexdigest()

if __name__ == '__main__':
    print md5_str('123123')