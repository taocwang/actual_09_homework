#encoding:utf-8

import time

''
'''
session      在服务端    一块存储
cookie       在浏览器端  一块存储
认证通过后,将sessions_id 放到服务端的session中
每次请求根据session_id获取session中的认证信息
如果认证信息存在 => 继续访问
如果无认证信息 => 跳转到登陆页面


导入 from flask import session

session ['session_name'] =  session_value

os.urandom(32)  随机生成32位字符串


消息闪现
    from flask import flash
    app.flash传递 = > 写到session中

    {% for msg in get_flashed_messages %}
    {{ msg }}
    {% endfor %}

'''




'''
装饰器

在所有函数之前执行一块代码
在函数之后执行一块代码

多个装饰器存在的bug
from functools import wraper

'''

#记录每个函数的执行时间

def time_wrapper(func):
    def wrapper():
        start = time.time()
        rt = func()
        exec_time = time.time() - start
        print '合计用时:%s' % exec_time
        return rt
    return wrapper

def test1():
    print 'test1'
    return 1

def test2():
    print 'test2'
    return 2

def test3():
    print 'test3'
    return 3

def test4():
    print 'test4'
    return 4

def test5():
    print 'test5'
    return 5

def wrapper(func):
    print '执行之前: %s' % func.__name__
    rt = func()
    print '执行之后: %s' % func.__name__
    return rt


print wrapper(test1)
print wrapper(test2)
print wrapper(test3)
print wrapper(test4)
print wrapper(test5)

@time_wrapper
def test6():
    print 'test6'
    time.sleep(2)
    return 6

print test6()

'''
mysql

show databases;
create database dbname ;
create table tablename (
    attrname attrtype,      字段名字,字段类型

);
attrtype => int
            varchar(n)

#设定主键,并设置id自增长
create table user(
  id int primary key auto_increment,
  username varchar(25),
  password varchar(32),
  age int,
  telphone varchar(32),
  email varchar(32)
) engine=innodb default charset=utf8;

#插入数据  insert
insert into user(username,password,age,telphone,email) values ('jcui','jcui','30','15110138509','cui@163.com') ;
insert into user(username,password,age,telphone,email) values ('admin','admin','30','15110138508','admin@163.com') ;

#查询  select
select * from user;

select password from user where username='jcui';

select * from user where username like '%jcui%';                #前% 表示任意字符+jcui   后% 表示jia+任意字符串   实例则表示包含jcui的

select * from user where age >=29;                      #范围查找

select count(*) from user where age >=29;         #统计 '

select ip,url,code , count(*) from accesslog groupby ip,url,code order by cnt desc limit 10;

#更新  update

update user set age=32  where username='jcui'  ;

update user set age=35  ;    #谨慎使用该命令,将对所有数据的age作修改

md5() 对密码进行加密

update user set password = md5(password);

select * from user where username = 'jcui' and password = md5('jcui')  ;         #查询用户名和加密的密码是否匹配


#删除  delete

delete from user where id=15 ;
delete from user where user='kk';
delete from user where age >= 30;
truncate table user ;   清空所有表的数据

#删除表 drop
drop table user;

desc table;
show create table user;

'''

import MySQLdb

conn = MySQLdb.connect(
    host = 'localhost' ,
    port = 3306 ,
    user = 'root',
    passwd = '6522123',
    db = 'jcui' ,
    charset = 'utf8'
)

cur = conn.cursor()
cur.execute('insert into user(username,password,age,telphone,email) values ("kk",md5("kk"),"28","15110138500","kk@163.com")')

conn.autocommit(True)     #设置自动提交
conn.autocommit(False)    #关闭自动提交
conn.commit()    #设置数据提交
conn.rollback()  #设置数据回滚
cur.execute('select * from user')   #需要先执行查询语句,然后执行下面的语句,显示一条或者多条
print cur.fetchone()   #查询一条数据
print cur.fetchall()   #查询所有数据
cur.close()
conn.close()

'''
import json as j   对json模块重命名
'''

'''
作业
1.修改,删除 改成db
2.修改和删除唯一标示修改为id
3. url ,ip ,code ,count 存储到数据库中

'''