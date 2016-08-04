#encoding:utf-8

''

'''
python多线程和多进程


进程是什么? 线程是什么? 区别?

线程ID,寄存器的值,线程的栈,优先级



CAP原理
'''



'''
StringIO


button bind('click')   时间后的请求

window.location('/assets/download/')


'''


'''
API

    restful,rpc
    一切皆资源 url
    干什么?

    增:POST
    删:DELETE
    改:PUT
    查:GET
    cpu,ram = POST url ,提交的数据(json) ,return json


'''

import csv

if __name__ == '__main__':
    fhandler = open('user.csv','r')
    csv_reader = csv.reader(fhandler)
    for _line in csv_reader:
        print _line
    fhandler.close()


    fhandler = open('user.csv','a')
    csv_writer = csv.writer(fhandler)
    csv_writer.writerow([6,'ada',21,232323])
    csv_writer.writerows([[9,'xiaoxia',21,232323],[10,'lala',34,232323]])
    fhandler.close()
