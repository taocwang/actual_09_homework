#!/usr/bin/env python
# coding=utf-8


with open('www_access_20140823.log') as f:
    for line in f.readlines():
        with open('copy_of_nginx_access.log','a+') as f1:
            f1.write(line)
