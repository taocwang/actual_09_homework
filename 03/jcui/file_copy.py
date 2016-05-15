#encoding:utf-8

import time

def time_consuming():
    def timess(func):
        start = time.time()
        func()
        end = time.time()
        print '用时:%.3fs' % (end-start)
        return
    return timess



@time_consuming()
def copy_file():
    size=4096
    sptah='f:\\360yunpan.zip'
    dpath='f:\\testcopy.zip'
    sfile = open(sptah,'rb')
    dfile = open(dpath,'wb')
    while True:
        data = sfile.read(size)
        if len(data) == 0:
            sfile.close()
            dfile.close()
            print '复制文件完毕,原文件:%s,目的文件:%s' % (sfile.name,dfile.name),
            break
        else:
            dfile.write(data)

'''
功能ok
改进:
1.line 30，一般如果写一个字符串类型的尽量使用write, 如果写list类型的再考虑writelines, 原因：遍历是需要时间的
2.可以将代码中的字面常量4096定义成变量，可以见名知意，如果多个地方使用以后改变量也好改
'''
