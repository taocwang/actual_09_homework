#!/bin/env python
#coding:utf-8

file="/home/share/www_access_20140823.log"
handle=open(file,'r')
d_list=[]
d_dict={}

for line in  handle:
    content='%s %s %s' %(line.split()[0],line.split()[6],line.split()[8])
        d_list.append(content)

	for net in d_list:
	    if net in d_dict:
	            d_dict[net]=d_dict[net]+1
		        else:
			        d_dict[net]=1

				#前十访问
				list_fin=d_dict.items()
				list_fin.sort(key=lambda x:x[-1])

				for item in list_fin[-10:]:
				    print item
