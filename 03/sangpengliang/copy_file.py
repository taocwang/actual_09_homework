#encoding: utf-8

srcpath = 'D:/\python/\/nginx_log/\/access.log'
dstpath = 'D:/\python/\/nginx_log/\/access_copy.log'

#读取文件内容
srchandler = open(srcpath, 'r')
cxt = srchandler.read()
srchandler.close()

#写新文件
dsthandler = open(dstpath, 'w')
dsthandler.write(cxt)
dsthandler.close()
