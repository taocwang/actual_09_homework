#!/bin/env python
#encoding:utf-8

from db_act import db_act

def userdel(username):
    _sql="delete from user where username=%s;"
    args=username
    return db_act(_sql,args,fetch=False)