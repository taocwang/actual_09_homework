# encoding: utf-8
def log(sfile,dfile,topn=5):
	d = {}
	
	'''
	打开文件把数据读入到字典里面用ip,url,返回值组成元组作为key。
	先把所有key赋空值，发现key在字典里面就把value加1。直到循环完成
	'''
	with open(sfile,'r') as f:
		for line in f.readlines():
			line = line.strip().split()
			ip,url,code = line[0],line[6],line[8]
			key = ip,url,code
	    		d[key] = d.get(key,0) + 1

# 把字典转换成列表
	dList = d.items()

	dl = sorted(dList,key=lambda x:x[1])
	title = 'TOP %d log' %(topn)

# 定义表头
	thead = '<th>num</th><th>IP</th><th>URL</th><th>Code</th>'

	tbody = ''

# 把统计好的内容放入变量tbody
	for node in  dl[-1:-topn -1:-1]:
	    tbody += '<tr><td>%s</td><td>%s</td><td>%s</td><td>%s</td></tr>' % (node[1], node[0][0],node[0][1],node[0][2])
# 读取模板文件
	with open('htmltmp.txt','r') as rf:
		page_tpl = rf.read()

#把格式化好的文件写入目标文件
	with open(dfile,'w') as htmlhandler:
		htmlhandler.write(page_tpl.format(title=title,thead=thead,tbody=tbody))

log(sfile='log',dfile='top20.html',topn=20)
log(sfile='log',dfile='top3.html',topn=3)
