#encoding: utf-8

import time

s = time.time()
rs_dict = {}

handler = open('www_access_20140823.log', 'r')
for line in handler:
    nodes = line.split(' ')
    key = (nodes[0], nodes[6], nodes[8])
    rs_dict[key] = rs_dict.get(key, 0) + 1

print 'stat after:', time.time() -s
s = time.time()

handler.close()
rs_list = rs_dict.items()
#[(key, value), (key1, value1)]
for j in range(10):
    for i in range(len(rs_list) - 1 - j):
        if rs_list[i][1] > rs_list[i + 1][1]:
            tmp = rs_list[i]
            rs_list[i] = rs_list[i + 1]
            rs_list[i + 1] = tmp
            rt_tmp = rs_list[-1:-11:-1]

for line in rs_list[-1:-11:-1]:
    print line

print 'ok:', time.time() - s
