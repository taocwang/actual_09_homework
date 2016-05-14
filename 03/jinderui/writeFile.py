# encoding: utf-8

path = 'nginx.log'

f = open(path,'r')
w = open('rnginx.log','w')

while True:
    wf = f.read(50)
    if not wf:
        break
    else:
        w.write(wf)

f.close()
w.close()

'''
功能ok
改进:
1. 可以将代码中的字面常量'rnginx.log', 50定义成变量，可以见名知意，如果多个地方使用以后改变量也好改

'''
