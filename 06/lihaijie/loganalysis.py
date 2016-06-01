#encoding:utf-8
import os,sys
from gconfig import file_path
def get_topn(srcpath,topn=10):
    handle=file(file_path + srcpath, 'r')
    # handle1=file(path + '/result.txt', 'wb')
    rt_dict={}
    while 1:
        line =handle.readline()
        if not line:
            break
        nodes = line.split()
        ip,url,code = nodes[0],nodes[6],nodes[8]
        key = (ip,url,code)
        if key not in rt_dict:
            rt_dict[key]=1
        else:
            rt_dict[key]=rt_dict[key]+1
    handle.close()
    # print "format done"
    rt_list=rt_dict.items()
    for j in range(topn):
        for i in range(len(rt_list)-1):
            if rt_list[i][1]>rt_list[i+1][1]:
                rt_list[i],rt_list[i+1]=rt_list[i+1],rt_list[i]
    return rt_list[-1:-topn-1:-1]
    # print "sort done"  
    # for info in rt_list[-1:-11:-1]:
        # handle1.write("%s %s %s %s\n" % (info[0][0],info[0][1],info[0][2],info[1]))
    # handle1.close()
    # print "write done" 
    # page_tpl ='''
    # <!DOCTYPE html>
    # <html>
        # <head>
            # <meta charset="utf-8"/>
            # <title>{title}</title>
        # </head>
        # <body>       
            # <table border="1px">
                # <thead>
                    # <tr>
                        # {thead}
                    # </tr>
                # </thead>
                # <tbody>                
                        # <tr>
                          # {tbody}
                        # </tr>
                # </tbody>
            # </table>
        # </body>
    # </html>
    # '''
    # title = 'TOP "%s" 访问日志' % topn
    # thead = "<th>IP</th><th>URL</th><th>CODE</th><th>COUNT</th>" 
    # tbody = ""
    # for info in rt_list[-1:-topn-1:-1]:
        # tbody = tbody + "<tr><td>%s</td><td>%s</td><td>%s</td><td>%s</td></tr>" % \
        # (info[0][0],info[0][1],info[0][2],info[1])
    # htmlhandler = open(path + despath,"wb")
    # htmlhandler.write(page_tpl.format(title=title,thead=thead,tbody=tbody))
    # htmlhandler.close()
    # return page_tpl.format(title=title,thead=thead,tbody=tbody)

if __name__=="__main__":
    srcpath = '/www_access_20140823.log'
    # despath = "/top10.html"    
    # loganalysis(srcpath,"/top15.html",15)
    print get_topn(srcpath,5)