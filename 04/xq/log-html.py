#!/usr/bin/env python
# coding=utf-8

def page_html(filename,cnt):
    k={}
    l=[]

    with open(filename) as f:
        for line in f:
            l.append((line.split()[0] + " " + line.split()[6] + " " + line.split()[8]))
    #print l[0:10]
    for i in l:
        k[i]=k.setdefault(i,0)+1
    kk=sorted(k.items(),key=lambda x: -x[1])

    #print kk[0]
    #for j in range(10):
    #    print kk[j][0],kk[j][1],
    #    print ""

    title = "TOP %s访问日志" %cnt
    thead = "<th>IP</th><th>URL</th><th>Code</th><th>次数</th>"
    tbody = ''

    for ii in kk[0:cnt]:
        tbody += '<tr><td align="center">%s</td><td>%s</td><td align="center">%s</td><td align="center">%s</td></tr>' % \
                (ii[0].split()[0],ii[0].split()[1],ii[0].split()[2],ii[1])
    with open('html.tpl') as f:
        htmllog=f.read().format(title=title,thead=thead,tbody=tbody)

    with open('top%s.html' %cnt,'w') as f1:
        f1.write(htmllog)
page_html('www_access_20140823.log',20)
page_html('www_access_20140823.log',100)
