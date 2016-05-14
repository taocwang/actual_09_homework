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

'''
功能ok
改进点:
1. 可以考虑将代码中的字面常量定义为变量比如www_access_20140823.log=>src_file, test.txt=>dst_file, 1024=>buffer_zie
'''
