#encoding:utf-8

import logging
from dbutils import MySQLConnection as SQL
from dbutils import sendmail
from gconfig import alarm_revices
import datetime
import sys
from modules import Assets

reload(sys)
sys.setdefaultencoding('utf8')

logger = logging.getLogger(__name__)

CNT = 3
CPU_PERCENT = 2
RAM_PERCENT = 2

def has_alarm(ip):
    _sql = 'select cpu,ram from performs where ip = %s and time >= %s order by time desc limit %s'
    _time = datetime.datetime.now() - datetime.timedelta(minutes=5)
    _args = (ip,_time.strftime('%Y-%m-%d %H:%M:%S'),CNT)
    _rt_cnt,_rt_list = SQL.excute_sql(_sql,_args)
    if _rt_cnt >= CNT:
        _cpu_alarm = True
        _ram_alarm = True
        for _cpu,_ram in _rt_list:
            if _cpu < CPU_PERCENT:
                _cpu_alarm = False
            if _ram < RAM_PERCENT:
                _ram_alarm = False
        return _cpu_alarm,_ram_alarm
    return False,False


def monitor():
    # _ip_list = ['192.168.1.35']
    _assets = Assets.get_list()
    _title = 'CPU、内存告警'
    for _ast in _assets:
        _ip = _ast['ip']
        _cpu_alarm,_ram_alarm =has_alarm(_ip)
        _content_list = ['主机{ip}告警'.format(ip=_ip)]
        if _cpu_alarm:
            _content_list.append('CPU连续{cnt}次超过{percent}%'.format(cnt=CNT,percent=CPU_PERCENT))
        if _ram_alarm:
            _content_list.append('内存连续{cnt}次超过{percent}%'.format(cnt=CNT,percent=RAM_PERCENT))
        if len(_content_list) > 2:
            sendmail(alarm_revices,_title,','.join(_content_list))
            logger.info('send mail to:%s ,title:%s ,msg:%s' ,alarm_revices, _title,','.join(_content_list))




if __name__ == '__main__':
    logging.basicConfig(Level=logging.debug,
                        format="%(asctime)s %(name)s %(pathname)s %(levelname)s %(message)s",
                        filename='/home/jcui/temp/monitor.log')
    monitor()