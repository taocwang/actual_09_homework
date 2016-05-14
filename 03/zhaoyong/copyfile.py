#encoding: utf-8

srcpath = 'test.txt'
dstpath = 'test1.txt'

srchandle = open(srcpath,'r')
cxt = srchandle.read()
srchandle.close()
print cxt

dsthandle = open(dstpath,'w')
dsthandle.write(cxt)
dsthandle.close()