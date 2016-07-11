#coding:utf-8
import time
import logging
import os
import json
import requests
import traceback

ser_url='http://192.168.0.102:8080/performs/'

loger=logging.getLogger(__name__)

def exc_cmd(cmd):
    _ch=os.popen(cmd)
    _re=_ch.read()
    _ch.close()
    return _re

def get_ip():
    _cmd="ifconfig eth1|grep -w inet"
    _re=exc_cmd(_cmd)
    ip=_re.strip().split()[1]
    return ip

def collect_cpu():
    _cmd="top -n1|grep Cpu"
    _re=exc_cmd(_cmd)
    free_cpu=float(_re.strip().split(',')[3].strip().split()[1])
    return 100 - free_cpu

def collect_ram():
    with open('/proc/meminfo') as e:
        _total=float(e.readline().split()[1])
        _free=float(e.readline().split()[1])
        _buffer=float(e.readline().split()[1])
    return 100 - 100*(_free+_buffer)/_total

def collect():
    _rt={}
    _rt['ip']=get_ip()
    _rt['time']=time.strftime('%Y-%m-%d %H:%M:%S')
    _rt['cpu']=collect_cpu()
    _rt['ram']=collect_ram()
    return _rt

def send():
    try:
        _data=collect()
        _response=requests.post(ser_url,data=json.dumps(_data),headers={'Content-Type':'application/json'})
        if not _response.ok:
            loger.error('error send %s failed'% _data)
    except BaseException as e:
        loger.error(traceback.format_exc())


if __name__ == '__main__':
    while True:
        try:    
            logging.basicConfig(level=logging.INFO,
                                format="%(asctime)s %(name)s %(lineno)d %(message)s",
                                filename="agent.log")
        
            send()
            time.sleep(60)
        except BaseException as e:
            loger.error(traceback.format_exc())