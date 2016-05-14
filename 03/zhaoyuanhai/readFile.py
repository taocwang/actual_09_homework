#!/usr/bin/env python
#_*_coding:utf-8_*_

fpath="/Users/yhzhao/Downloads/绿盟安全审计系统-堡垒机系列用户手册.docx"
spath="/Users/yhzhao/Downloads/copyFile.docx"

f = open(fpath, 'rb')
s = open(spath, 'ab')

while True:
    text = f.read(1024)
    if len(text) == 0:
        break
    s.write(text)

s.close()
f.close()
