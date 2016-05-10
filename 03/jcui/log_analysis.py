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
def log_analysis():
    path = 'f:\www_access_20140823.log'
    files = open(path,'r')
    sequence = {}
    for i in files:
        ip ,filepath ,status = i.split()[0],i.split()[6],i.split()[8]
        sequence[(ip,filepath,status)] = sequence.get((ip,filepath,status),0) + 1
    files.close()
    sequence_list = sequence.items()
    for x in range(0,len(sequence_list)-1):
        for y in range(0,len(sequence_list)-1-x):
            if sequence_list[y][1] > sequence_list[y+1][1]:
                sequence_list[y],sequence_list[y+1] = sequence_list[y+1],sequence_list[y]

    for x in sequence_list[-1:-11:-1]:
        print '请求IP地址:{ip},请求文件路径:{url},请求结果状态:{status},请求次数:{nums} ' .format(ip=x[0][0],url=x[0][1],status=x[0][2],nums=x[1])

