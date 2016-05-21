#!/bin/env python
#coding:utf8
'''将nginx的log分析出访问topn个，生成一个新文件和html文件'''

n=7 #定义top前多少 
src_file="www_access_20140823.log"
dst_file='top%d_access_def.log' % n
web_file_default="top10.html_default"
web_file="top%d_access_def.html"% n 
site_title='访问量TOP%d' % n 

def topn(src_file,dst_file,n=10):
    '''取得topn数据，并写入到文件'''
    cnt_dict={}
    handler=open(src_file,'rb')

    for line in handler:
        nodes=line.split()
        ip,path,code=nodes[0],nodes[6],nodes[8]
        key=(ip,path,code)
        #if key in cnt_dict:
         #   cnt_dict[key] += 1
        #else:
         #   cnt_dict[key]=1
        cnt_dict[key]=cnt_dict.get(key,0)+1  #get是函数，不能直接+=

    cnt_list=cnt_dict.items()
    cnt_list.sort(key=lambda x:x[-1],reverse=True)

    handler_dst=open(dst_file,'w')

    for topn_result in cnt_list[:n]:
        result="%s %s %s %s\n" % (str(topn_result[-1]),topn_result[0][0],topn_result[0][1],topn_result[0][-1])
        handler_dst.writelines(result)

    handler.close()
    handler_dst.close()
    return cnt_list
    
cnt_list=topn(src_file,dst_file,n) #关键数据下面的函数需要用，所以定为全局变量

def topn_web_file(web_file,n=10):
    '''利用上面的函数返回结果cnt_list，将结果写入到html文件'''
    format_web=open(web_file_default,'r')
    curr_web=open(web_file,'w')
    tbody=''
    for topn_result in cnt_list[:n]:
        tbody += '\t\t\t\t<tr>\n\t\t\t\t\t<th>%s</th><th>%s</th><th>%s</th><th>%s</th>\n\t\t\t\t</tr>\n' % (str(topn_result[-1]),topn_result[0][0],topn_result[0][1],topn_result[0][-1])

    curr_web.write(format_web.read().format(tbody=tbody,web_title=site_title))

    format_web.close()
    curr_web.close()

topn_web_file(web_file,n)

