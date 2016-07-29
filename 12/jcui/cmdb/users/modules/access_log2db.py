#encoding:utf-8

from dbutils import MySQLConnection as SQL
import geoip2.database
import time
import urllib2
import json

def get_city(ip):
    url = 'http://api.map.baidu.com/location/ip?ak=omi69HPHpl5luMtrjFzXn9df&ip=%s&coor=bd09ll' % ip
    res = urllib2.Request(url)
    html = json.loads(urllib2.urlopen(res).read())
    if html['status'] == 0:
        city = html.get('content').get('address_detail').get('city')
        lat = html.get('content').get('point').get('y')
        lng = html.get('content').get('point').get('x')
        return [True,city,lat,lng]

    return [False]

if __name__ == '__main__':
    # logfile = '/home/jcui/files/www_access_20140823.log'
    logfile = '/home/jcui/files/access.log'
    SQL.excute_sql('delete from access_logs2',(),fetch=False)
    reader = geoip2.database.Reader('../data/GeoLite2-City.mmdb')
    log_files  = open(logfile,'r')

    rt_list = []
    while True:
        line = log_files.readline()
        if line == '':
            break
        nodes  = line.split()
        ip,logtime,url,status = nodes[0],nodes[3][1:],nodes[6],nodes[8]
        logtime = time.strftime('%Y-%m-%d %H:%M:%S',time.strptime(logtime,'%d/%b/%Y:%H:%M:%S'))
        try:
            response = reader.city(ip)
            if 'China' != response.country.name:
                print 'ip not in china:%s' % ip
                continue
            city = response.city.names.get('zh-CN','')
            if city == '':
                _rt = get_city(ip)
                if _rt[0]:
                    city,lat,lng = _rt[1],_rt[2],_rt[3]
                    if city == '':
                        print 'city is null:%s' % ip
                        continue
                else:
                    print 'city is null:%s' % ip
                    continue
            else:
                lat = response.location.latitude
                lng = response.location.longitude
            #lng 经度
            #lat 纬度
        except BaseException as e:
            print ip
            _rt = get_city(ip)
            if _rt[0]:
                city, lat, lng = _rt[1], _rt[2], _rt[3]
                if city == '':
                    print 'city is null:%s' % ip
                    continue
            else:
                print 'geo ip not found ip:%s' % ip

        rt_list.append((logtime, ip, url, status, lat, lng, city))

    log_files.close()
    _sql = 'insert into access_logs2(logtime,ip,url,status,lat,lng,city) values(%s,%s,%s,%s,%s,%s,%s)'
    SQL.excute_log_sql(_sql,rt_list)






























