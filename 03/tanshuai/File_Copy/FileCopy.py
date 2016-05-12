#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
以1024字节copy文件
'''

# 1、打开源文件和目标文件；
SF = open('www_access_20140823.log', 'rb')
DF = open('test.txt', 'wb')

# 2、读取源文件，并写入目标文件；
while True:
    src_file = SF.read(1024)
    if not src_file:
        break
    DF.write(src_file)
# 3、关闭文件
SF.close()
DF.close()