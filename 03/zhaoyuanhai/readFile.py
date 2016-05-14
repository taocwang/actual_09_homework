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

'''
功能ok
1.可以考虑将的代码中的字面常量定义为变量，比如1024=>buffer_size
2. line12 len(text) == 0 和not text的结果有什么不同呢?能不能相互替换?
'''
