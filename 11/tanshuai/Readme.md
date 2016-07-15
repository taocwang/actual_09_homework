# 模块
    1、安装
        pip install
    2、导入
        imoort
    3、查看模块的方法
        dir()
    4、查看模块帮助
        help()
    5、使用

###1、os模块
```
>>> import os
>>> os.urandom(223414)
# 把某个目录的文件打印(拿)出来
>>> os.listdir('/')
# 判断是不是目录，返回值:True/False
>>> os.path.isdir('./')
# 获取文件的路径
>>> os.path.dirname('D:\kk_cmdb\manage.py')
'D:\\kk_cmdb'
# join拼接文件的路径
>>> os.path.join('/test/test/','test.py')
'/test/test/test.py'
# 将路径格式化
>>> os.path.normpath('D:\kk_cmdb\manage.py')
'D:\\kk_cmdb\\manage.py'
# 获取目录里的文件
>>> for i in os.walk(r'D:\kk_cmdb'):
...     print i
...
('D:\\kk_cmdb', ['cmdb'], ['manage.py'])
('D:\\kk_cmdb\\cmdb', ['templates'], ['dbutils.py', 'gconf.py', 'log2db.py']
('D:\\kk_cmdb\\cmdb\\templates', [], ['layout.html', 'login.html', 'logs.html]

# 执行外部命令
>>> s = os.system('ping baidu.com')
>>> print s     返回(0执行正常/1执行错误 )
# 获取执行命令的结果
>>> fh = os.popen('ping baidu.com')
>>> fh.read()
'\n\xd5\xfd\xd4\xda Ping baidu.com [180.149.13
>>> fh.close()  # 读取后需要关闭

```

# sys

### time模块
```
>>> import time
>>> time.time()
1468129396.503
>>> time.localtime()
time.struct_time(tm_year=2016, tm_mon=7, tm_mday=10, tm_hour=13, tm_min=44, tm_sec=5, tm_wday=6, tm_yday=192, tm_isdst=0)
# 前一天的时间
>>> time.localtime(time.time() - 24 * 60 * 60)
time.struct_time(tm_year=2016, tm_mon=7, tm_mday=9, tm_hour=13, tm_min=44, tm_sec=26, tm_wday=5, tm_yday=191, tm_isdst=0)
# 转换时间
>>> time.mktime(time.localtime())
1468129600.0
# 当前时间
>>> time.strftime('%Y-%m-%d %H:%M:%S')
'2016-07-10 13:50:33'
# 前一天的时间
>>> time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time() - 24 * 60 * 60))
'2016-07-09 13:50:37'
# 时间转换
>>> time.strptime('2016-07-09 13:50:37', '%Y-%m-%d %H:%M:%S')
time.struct_time(tm_year=2016, tm_mon=7, tm_mday=9, tm_hour=13, tm_min=50, tm_sec=37, tm_wday=5, tm_yday=191, tm_isdst=-1)

>>>import datetime
>>> datetime.datetime.now()
datetime.datetime(2016, 7, 10, 14, 0, 36, 552000)
>>> datetime.datetime.now().strftime('%Y-%m-%d')
'2016-07-10'
>>> datetime.datetime.now().strptime('2016-07-10', '%Y-%m-%d')
datetime.datetime(2016, 7, 10, 0, 0)
#
>>> datetime.datetime.now() + datetime.timedelta(days=-1)
datetime.datetime(2016, 7, 9, 14, 7, 56, 112000)
>>> datetime.datetime.now() - datetime.timedelta(days=-1)
datetime.datetime(2016, 7, 11, 14, 8, 6, 171000)
```

### hashlib库
```
>>> import hashlib
>>> _md5 = hashlib.md5()
>>> _md5.update('123123')
>>> _md5.hexdigest()
'4297f44b13955235245b2497399d7a93'


```
CREATE table performs(
    id bigint primary key auto_increment,
    ip varchar(128),
    cpu float,
    ram float,
    time datetime
)engine=innodb default charset=utf8;










