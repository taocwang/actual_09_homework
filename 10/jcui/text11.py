#encoding:utf-8



''



'''
模块: os,sys
    1) pip install xxxx
    2) import
    3) dir()
    4) help()
    5) 用

os.urandom(32)   #生成随机字符串
os.listdir()
os.system()
os.popen()
os.path()

sys
argparse

#time
A: time.time()

B: time.localtime()

C: time.strftime()



B -> A
time.mktime(time.localtime())
B -> C
time.strftime('%Y-%m-%d',time.localtime(time.time() - 24*60*60))
C -> B
time.strptime('2016-07-30','%Y-%m-%d')


#datetime

datetime.datetime.now()

datetime.datetime.now().strftime('%Y-%m-%d')
datetime.datetime.strptime('2016-03-03','%Y-%m-%d')

datetime.timedelta(days=1)
#得到昨天的日期
datetime.datetime.now() -  datetime.timedelta(days=1)
#得到明天的日期
datetime.datetime.now() -  datetime.timedelta(days=-1)


#md5的模块
hashlib

_md5 = hashlib.md5()

_md5.update('123456')
_md5.hexdigest()



#logging

import logging
logger = logging.getLogger(__name__)

if __name__ == '__main__':
    logging.basicConfig(Level=logging.debug,
                        format="%(asctime)s %(name)s %(pathname)s %(levelname)s %(message)s",
                        filename='stdout.log')
    logger.debug('i am debug')
    logger.info('i am info')
    logger.error('i am errer')

'''


'''
监控系统:
182.61.42.4
root
1qaz@WSX




作业:

1. asset的采购时间改为%Y-%m-%d

2. 添加用户,修改用户密码改为md5_str函数

3. 今天的课程做完.

4. web执行命令
    form 提交ip,port,username,password,cmd=>ssh.py 获取结果显示
            管理员密码 =>


'''

import os
import sys
import argparse
import logging
#
# print dir(os)

#遍历文件
def getfiles(dirpath):
    filelist = []
    if os.path.isdir(dirpath):
        _names = os.listdir(dirpath)
        for _name in _names:
            newpath = dirpath +'/'+ _name
            if os.path.isdir(newpath):
                filelist.extend(getfiles(newpath))
            elif newpath.endswith('.py'):
                filelist.append(newpath)
        return filelist

def get_ip(dotemp):
    return os.popen(dotemp)
    # return os.system(dotemp)

if __name__ == '__main__':
    # if len(sys.argv) >= 2:
    #     dirpath = sys.argv[1]
    # else:
    #     print "usage : argv error"
    #     sys.exit(-1)
    #
    # print getfiles(dirpath)
    # _cnt = get_ip('ifconfig')
    # print _cnt.read()
    # _cnt.close()
    logger = logging.getLogger(__name__)
    #.....
    # _params = argparse.ArgumentParser()
    # _params.add_argument('-D','--dirpath',help='要遍历的目录')
    # _params.add_argument('-H','--host',help='要访问的服务器地址,默认为localhost',default='localhost')
    # _params.add_argument('-P','--port',help='要访问服务器所对应的短裤,默认为80端口',type=int,default=80)
    # _params.add_argument('-C','--cmd',help='要执行的命令',nargs="+",default=[])
    # _args = _params.parse_args()
    # if _args.dirpath is None:
    #     _params.print_help()
    #     exit(-1)
    # print _args.cmd
    # print _args.dirpath
    # print _args.host
    # print _args.port
    #
    # dirpath = _args.dirpath
    # print getfiles(dirpath)
    #.....

    logging.basicConfig(Level=logging.debug,
                        format="%(asctime)s %(name)s %(pathname)s %(levelname)s %(message)s",
                        filename='/home/jcui/temp/stdout.log')
    logger.debug('i am debug')
    logger.info('i am info')
    logger.error('i am errer')






