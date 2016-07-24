#encoding:utf-8
''
'''
cmdb/
    configs/
        __init__.py
        gconf.py
    user/
        *.py
        import gconf => from configs import gconf
                        from utils import ssh
        commands/
            __init__.py
            python xxx.py
    asset/
        static/
        templates/
        views.py
        models.py
    log/
        static/
        templates/
        views.py
        models.py
    utils/
        __init__.py
        mail.py
        db.py
        encrypt.py
        ssh.py
    manage.py


今日课程

1. echarts
    a. 饼状图
        状态分布图
    b. 层叠柱状图
        最近12小时,每5分钟,每个状态码出现次数的层叠柱状图
    c. 地图
        ip => 坐标


create table access_logs2(
id bigint primary key auto_increment,
logtime datetime,
ip varchar(128),
url text,
status int,
lat float,
lng float
) engine=innodb default charset=utf8;

'''