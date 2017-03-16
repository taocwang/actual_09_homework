#encoding:utf-8

''

'''
python多线程和多进程


进程是什么? 线程是什么? 区别?

线程ID,寄存器的值,线程的栈,优先级



CAP原理

Consistency 一致性
Availability 可用性
Partition tolerance 可靠性(分区容错性)

任何分布式只可满足二点,无法三者兼顾

高可用、数据一致是很多系统设计的目标，但是分区又是不可避免的事情：
CA without P：如果不要求P（不允许分区），则C（强一致性）和A（可用性）是可以保证的。但其实分区不是你想不想的问题，而是始终会存在，因此CA的系统更多的是允许分区后各子系统依然保持CA。
CP without A：如果不要求A（可用），相当于每个请求都需要在Server之间强一致，而P（分区）会导致同步时间无限延长，如此CP也是可以保证的。很多传统的数据库分布式事务都属于这种模式。
AP wihtout C：要高可用并允许分区，则需放弃一致性。一旦分区发生，节点之间可能会失去联系，为了高可用，每个节点只能用本地数据提供服务，而这样会导致全局数据的不一致性。现在众多的NoSQL都属于此类。

'''


'''
OIO、NIO、AIO的区别

OIO:线程发起IO请求，不管内核是否准备好IO操作，从发起请求起，线程一直阻塞，直到操作完成

NIO:线程发起IO请求，立即返回；内核在做好IO操作的准备之后，通过调用注册的回调函数通知线程做IO操作，线程开始阻塞，直到操作完成。

AIO:线程发起IO请求，立即返回；内存做好IO操作的准备之后，做IO操作，直到操作完成或者失败，通过调用注册的回调函数通知线程做IO操作完成或者失败。


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
