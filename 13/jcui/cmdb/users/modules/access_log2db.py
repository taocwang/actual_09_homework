#encoding:utf-8

from dbutils import MySQLConnection as SQL
import geoip2.database
import time



if __name__ == '__main__':
    logfile = '/home/jcui/files/www_access_20140823.log'
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
                print 'city is null:%s' % ip
                continue
            lat = response.location.latitude
            lng = response.location.longitude
            rt_list.append((logtime, ip, url, status, lat, lng, city))
        except BaseException as e:
            print 'geo ip not found ip:%s' % ip
    log_files.close()
    _sql = 'insert into access_logs2(logtime,ip,url,status,lat,lng,city) values(%s,%s,%s,%s,%s,%s,%s)'
    SQL.excute_log_sql(_sql,rt_list)






























