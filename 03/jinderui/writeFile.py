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
