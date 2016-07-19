#encoding:utf-8


import logging
import time
import os
import traceback

import requests
import json


logger = logging.getLogger(__name__)
App_key = 'c370af0f89fe66f06d1b70025d6a84c2'
App_secret = 'a458f162b35f53343750e885ea9b6f73'
server_url = 'http://localhost:9000/performs/'

def execute_cmd(_cmd):
    _fh = os.popen(_cmd)
    _cxt = _fh.read()
    _fh.close()
    return _cxt.rstrip()

def get_ip():
    _cmd = "ifconfig ens33 | grep 'inet 地址' | awk '{print $2}' |awk -F':' '{print $2}'"
    return execute_cmd(_cmd)

def collect_cpu():
    _cmd = "top -bn 1 |grep Cpu |awk '{print $8}'"
    return 100 - float(execute_cmd(_cmd))

def collect_ram():
    f = open('/proc/meminfo','r')
    _totol = float(f.readline().split()[1])
    _free = float(f.readline().split()[1])
    f.readline()
    _buff = float(f.readline().split()[1])
    f.close()
    return 100*(_free+_buff)/_totol



def collect():
    rt = {}
    rt['ip'] = get_ip()
    rt['cpu'] = collect_cpu()
    rt['ram'] = collect_ram()
    rt['time'] = time.strftime('%Y-%m-%d %H:%M:%S')

    return rt

def send(msg):
    try:
        _reponse = requests.post(server_url,data=json.dumps(msg),headers={"Content-Type":"application/json",'app_key':App_key,'app_secret':App_secret})
        if not _reponse.ok:
            logger.error('error send msg: %s',msg)
        else:
            _json = _reponse.json()
            if _json.get('code') != 200:
                logger.error('error send msg:%s ,result:%s',msg,_json)
    except BaseException as e:
        logger.error(traceback.format_exc())


if __name__ == '__main__':
    logging.basicConfig(Level=logging.DEBUG,
                        format="%(asctime)s %(name)s %(pathname)s %(levelname)s %(message)s",
                        filename='/home/jcui/temp/stdout.log')
    while True:
        try:
            _msg = collect()
            logger.debug(_msg)
            send(_msg)
            time.sleep(60)
            logger.debug(time.strftime('%Y-%m-%d %H:%M:%S'))
        except BaseException as e:
            logger.error(traceback.format_exc())

    '''
    Content-Type application/json

CREATE TABLE `performs` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `ip` varchar(128) DEFAULT NULL,
  `cpu` float DEFAULT NULL,
  `ram` float DEFAULT NULL,
  `time` datetime DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=218 DEFAULT CHARSET=utf8

    '''




























