#encoding: utf-8

import time

s = time.time()
rs_dict = {}

handler = open('D:\/python\/nginx_log\/access.log')
for line in handler:
    nodes = line.split(' ')
   #key = (nodes[0], nodes[4])
   #key = (nodes[0], nodes[2])
    key = (nodes[0], nodes[6], nodes[8])
    rs_dict[key] = rs_dict.get(key, 0) + 1

print 'stat after:', time.time() -s
s = time.time()

handler.close()
rs_list = rs_dict.items()

for i in range(10):
    for j in range(len(rs_list) - 1 -i):
        if rs_list[j][1] > rs_list[j + 1][1]:
            tmp = rs_list[j]
            rs_list[j] = rs_list[j + 1]
            rs_list[j + 1] = tmp
            rt_tmp = rs_list[-1:-11:-1]

for line in rs_list[-1:-11:-1]:
    print line

print 'ok' , time.time() - s
