#!/usr/bin/env python

import time

start_date = time.time()
nginx_dict = {}
nginx_file = open('www_access_20140823.log')
for line  in nginx_file:
    nodes = line.split()
    key = (nodes[0],nodes[6],nodes[8])
    #print key
    nginx_dict[key] = nginx_dict.get(key,0) + 1
    #print nginx_dict

use_date = time.time() - start_date
nginx_file.close()

ng_list = nginx_dict.items()

for j in range(10):
    for i in range(len(ng_list)-1-j):
        if ng_list[i][1] > ng_list[i+1][1]:
            tmp =  ng_list[i]
            ng_list[i] = ng_list[i+1]
            ng_list[i+1] = tmp
            ng_tmp = ng_list[-1:-11:-1]

for line in ng_list[-1:-11:-1]:
    print line


