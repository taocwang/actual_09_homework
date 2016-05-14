#encoding: utf-8

srcpath = 'www_access_20140823.log'
dstpath = '2.log'

#读取文件内容
srchandler = open(srcpath, 'r')
cxt = srchandler.read()
srchandler.close()


#写新文件
dsthandler = open(dstpath, 'w')
dsthandler.write(cxt)
dsthandler.close()

# 方法二

srchandler = open(srcpath, 'r')
dsthandler = open(dstpath + '.2', 'w')
size = 1024

while True:
    cxt = srchandler.read(size)
    if not cxt:
        break
    dsthandler.write(cxt)

dsthandler.close()
srchandler.close()
