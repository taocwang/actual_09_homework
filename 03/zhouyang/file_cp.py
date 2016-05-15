#!/bin/env python

src_file='/home/share/www_access_20140823.log'
dst_file='nginx.log'

pre_size=512

hand_src=open(src_file,'r',pre_size)
content=hand_src.read()
hand_src.close

hand_dst=open(dst_file,'a',2)
hand_dst.write(content)
hand_dst.close()
