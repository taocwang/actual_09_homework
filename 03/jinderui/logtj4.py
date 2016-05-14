# encoding: utf-8

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

# 用zip把字典转换成列表（翻转value和key）
dl = zip(d.values(),d.keys())

# sorted排序
dl2 = sorted(dl)
# 取top10
for x in dl2[-1:-11:-1]:
    print "num:{num:d}  ip:{ip}  url:{url}  state:{state}".format(num=x[0],ip=x[1][0],url=x[1][1],state=x[1][2])
