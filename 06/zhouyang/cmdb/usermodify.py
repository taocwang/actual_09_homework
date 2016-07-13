#coding:utf-8
import uconf
import json
from db_act import db_act

def usermodify(username,password,age):
    _sql="update user set password=md5(%s),age=%s where username=%s;"
    args=(password,age,username)
    return db_act(_sql,args,fetch='False')

if __name__ == '__main__':
   usermodify('zy1',123,22)


