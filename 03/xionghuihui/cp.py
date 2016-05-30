#!encoding: utf-8

top = 'www_access.log'

cp_top = '2.py'

#读文件

a = open(top,'r')
cxt = a.read()
a.close()

#写文件
b = open(cp_top,'w')
b.write(cxt)
b.close()


#当文件很大时
a = open(top,'r')
b = open(cp_top,'w')
size = 1024

while True:
    cxt = a.read(size)
    if not cxt:
        break
    b.write(cxt)
a.close()
b.close()
