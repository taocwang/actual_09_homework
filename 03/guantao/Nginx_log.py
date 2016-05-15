#encoding:utf8
#参考kk老师的思路
Ngx_dict = {}     #定义一个空的字典

file = open('www_access_20140823.log' , 'r')     #指定文件路径，用读的方式打开

for a in file:
    keys = (a.split(' ')[0] , a.split(' ')[6] , a.split(' ')[8])   # 遍历文件内容，截取相关字段，定义keys格式
    Ngx_dict[keys] = Ngx_dict.get(keys , 0) + 1       #将截取的内容作为key值写入字典，并统计次数

file.close()

Ngx_list = Ngx_dict.items()                       #通过冒泡排序，截取出前10名
for a in range(0,10):
    for b in range(0, len(Ngx_list) -1 -a):
        if Ngx_list[b][1] > Ngx_list[b + 1][1]:
            x = Ngx_list[b]
            Ngx_list[b] = Ngx_list[b + 1]
            Ngx_list[b + 1] = x
            top = Ngx_list[-1:-11:-1]

for g in top:
    print g

