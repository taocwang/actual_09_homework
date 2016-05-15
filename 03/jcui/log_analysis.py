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

#方法一
# @time_consuming()
# def log_analysis():
#     path = 'f:\www_access_20140823.log'
#     files = open(path,'r')
#     sequence = {}
#     for i in files:
#         ip ,filepath ,status = i.split()[0],i.split()[6],i.split()[8]
#         sequence[(ip,filepath,status)] = sequence.get((ip,filepath,status),0) + 1
#     files.close()
#     sequence_list = sequence.items()
#     for x in range(0,len(sequence_list)-1):
#         for y in range(0,len(sequence_list)-1-x):
#             if sequence_list[y][1] > sequence_list[y+1][1]:
#                 sequence_list[y],sequence_list[y+1] = sequence_list[y+1],sequence_list[y]
#
#     for x in sequence_list[-1:-11:-1]:
#         print '请求IP地址:{ip},请求文件路径:{url},请求结果状态:{status},请求次数:{nums} ' .format(ip=x[0][0],url=x[0][1],status=x[0][2],nums=x[1])

#方法二:
# @time_consuming()
# def log_analysis_1():
#     file_dict = {}
#     path = 'f:\www_access_20140823.log'
#     files1 = open(path,'r')
#     for i in files1:
#         x,y,z = i.split()[0],i.split()[6],i.split()[8]
#         file_dict[(x,y,z)] = file_dict.get((x,y,z),0) + 1
#     files1.close()
#     file_list = file_dict.items()
#     for a in range(0,len(file_list)):
#         index = a
#         for b in range(a+1,len(file_list)):
#             if file_list[index][1] > file_list[b][1]:
#                 index = b
#         file_list[a],file_list[index] = file_list[index],file_list[a]
#     for i in file_list[-1:-10:-1]:
#         print '请求IP地址:{ip},请求文件路径:{url},请求结果状态:{status},请求次数:{nums} ' .format(ip=i[0][0],url=i[0][1],status=i[0][2],nums=i[1])

#方法三(执行效率最快)
@time_consuming()
def log_analysis_2():
    file_dict = {}
    path = '/home/jcui/files/www_access_20140823.log'
    files1 = open(path,'r')
    for i in files1:
        i = i.split()
        x,y,z = i[0],i[6] ,i[8]
        # x,y,z = i.split()[0],i.split()[6],i.split()[8]
        file_dict[(x,y,z)] = file_dict.get((x,y,z),0) + 1
    files1.close()
    file_list = sorted(file_dict.items(), key=lambda x:x[1], reverse = True)
    for i in file_list[0:10]:
        print '请求IP地址:{ip},请求文件路径:{url},请求结果状态:{status},请求次数:{nums} ' .format(ip=i[0][0],url=i[0][1],status=i[0][2],nums=i[1])

#方法四(只取最大值,循环10次)
@time_consuming()
def log_analysis_3():
    file_dict = {}
    path = '/home/jcui/files/www_access_20140823.log'
    files1 = open(path,'r')
    for i in files1:
        i = i.split()
        x, y, z = i[0], i[6], i[8]
        file_dict[(x,y,z)] = file_dict.get((x,y,z),0) + 1
    files1.close()
    file_list = file_dict.items()
    for n in range(10):  #(由于只取top10,所以找出最大的10个值即可,该值可作为参数传递给函数调用)
        for i in range(0,len(file_list)-1):
            if file_list[i][1] > file_list[i+1][1]:
                file_list[i],file_list[i+1] = file_list[i+1],file_list[i]

    write_file = open('/home/jcui/files/top10.txt','w')
    for i in file_list[-1:-11:-1]:
        print '请求IP地址:{ip},请求文件路径:{url},请求结果状态:{status},请求次数:{nums} ' .format(ip=i[0][0],url=i[0][1],status=i[0][2],nums=i[1])
        write_file.writelines('请求IP地址:{ip} 请求文件路径:{url} 请求结果状态:{status} 请求次数:{nums} \n' .format(ip=i[0][0],url=i[0][1],status=i[0][2],nums=i[1]))
    write_file.close()


'''
功能ok，加油
改进:
1. line 60, line 74：可以考虑split一次，通过范围的结果通过索引创建key, split一次，总比split3次快把
'''
