#!encoding:utf-8

import os   #导入系统模块用于执行命令linux的shell底下的命令 os.popen
import time  #导入时间模块time time.strftime('%Y-%m-%d %H:%M:%S') 导入时间模块然后写入数据库里面的时间的字段
import logging #导入日志模块 用于记录agent的日志
import requests #导入requests 用于请求服务器的连接
import json  #导入json 用户数据的传输
import traceback #tracebak.print_exc 打印捕获的异常
SERVER_URL = 'http://localhost:8000/performs/' #request 访问的URL
logger = logging.getLogger(__name__)  #生成统计的对象
APP_KEY = 'dc7f8bd6c614b92259d38e83b48678a6'
APP_SECRET = 'ad3890a4bf2b125b4014206266a75c52'

#执行命令的模块
def execute_cmd(cmd):
    _fh = os.popen(cmd)
    _cxt = _fh.read()
    _fh.close()
    return _cxt

#得到系统ip的模块
def get_ip():
    _cmd = "ifconfig eth0 | grep 'inet addr' | awk '{print $2}'"
    _cxt = execute_cmd(_cmd)
    return str(_cxt.split(':')[-1]).strip()

#收集cpu的模块
def collect_cpu():
    _cmd = "top -n 1 | grep Cpu | awk '{print $5}'"
    _cxt = execute_cmd(_cmd)
    return 100 - float(_cxt.split('%')[0])


#收集内存的模块
def collect_ram():
    _fh = open('/proc/meminfo')
    _total = float(_fh.readline().split()[1])
    _free = float(_fh.readline().split()[1])
    _buffer = float(_fh.readline().split()[1])
    _fh.close()
    return 100 - 100 * (_free + _buffer) /_total

#收集成一个字典
def collect():
    _rt = {}
    _rt['ip'] = get_ip()
    _rt['cpu'] = collect_cpu()
    _rt['ram'] = collect_ram()
    _rt['time'] = time.strftime('%Y-%m-%d %H:%M:%S')
    return _rt

def send(msg):
    try:
        _response = requests.post(SERVER_URL,data=json.dumps(msg),headers={"Content-Type":"application/json",'app_key':APP_KEY,'app_secret':APP_SECRET}) #这个是请求一个数据带着什么数据进行请求
        if not _response.ok: #判断这个对象里面的方法ok是否是True还是False
            logger.error('error send msg:%s',msg)  #不是的话就是记录日志信息
        else:
            _json = _response.json()  #生产个一个json的对象里面有状态码的记录
            if _json.get('code') != 200: #如果不是200的情况下就记录日志错误的
                logger.error('error send msg:%s ,result:%s',msg,_json)
    except BaseException as e:
        logger.error(traceback.format_exc())#记录异常处理的捕捉


if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG,format="%(asctime)s %(name)s [%(lineno)d] %(levelname)s:%(message)s",
                        filename="agent.log")
    while True:
        try:
            _msg = collect()
            send(_msg)
            time.sleep(5)
        except BaseException as e:
            logger.error(traceback.format_exc())


