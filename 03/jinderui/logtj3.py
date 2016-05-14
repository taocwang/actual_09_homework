# encoding: utf-8

#导入外部函数
from operator import itemgetter

d = {}
'''
打开文件把数据读入到字典里面用ip,url,返回值组成元组作为key。
先把所有key赋空值，发现key在字典里面就把value加1。直到循环完成
'''
with open('nginx.log','r') as f:
    for line in f.readlines():
        linelist = line.strip().split(' ')
        dfile = linelist[0],linelist[6],linelist[8]
        d.setdefault(dfile,0)
        d[dfile] = d.setdefault(dfile,0) + 1

# 把生成的字典转换成列表
dl = d.items()

#利用外部模块指定key排序
dl2 = sorted(dl,key=itemgetter(1))


# 取top10
for x in dl2[-1:-11:-1]:
    print "ip:{ip}  url:{url}  state:{state}  num:{num}".format(ip=x[0][0],url=x[0][1],state=x[0][2],num=x[1])

'''
功能ok，继续加油
'''
