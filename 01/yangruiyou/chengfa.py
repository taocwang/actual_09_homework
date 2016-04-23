#!/usr/bin/python

for i in range(1,10):
    for j in range(1,i+1):
        print str(i) + '*' + str(j) + '=' + str(i*j) + '    ',
    print ''

'''
功能ok，可以多练习下 字符串格式化的形式，字符串格式化是否可以解决在数字与字符串连接时对数字进行强制转化的问题
'''