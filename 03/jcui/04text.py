#encoding:utf-8
''
'''
第四课课堂内容
by 2016-05-15
'''
#逻辑思维
#解决问题的思路 - 想清楚人是如何做事情，然后用语言来写出
#推荐图书 - 清华大学 严蔚敏 数据结构

#三点--------
#语法
#逻辑思维
#工程思维

#安装mysql模块  sudo apt-get install python-mysqldb
import MySQLdb


#继续上节课的文件操作

#file.flush()     #将内存的文件写入到文件中，但此时未关闭文件

path = '/home/jcui/files/text.txt'
newpath = '/home/jcui/files/test.txt'
# h = open(path,'w')
# h.write('asd \n')
# h.flush()
# #此时查看文件
# h.close()


'''
mode
r   以只读方式打开
w   写,每次打开文件都会清空源文件,文件不在则新建文件
a   追加,文件永远写入到文件末尾
b   二进制拷贝
rb  以二进制读
wb  以二进制写
+
w+  以读写的方式打开文件,每次打开文件会清空源文件，文件不存在则新建文件
r+  以读写的方式打开文件,每次打开文件不会清空源文件，在写文件时会从文件开始写，写入几个字节，则占有几个字节
a+  以读写的方式打开文件,文件永远写入到文件末尾

h.tell()   查看当前指针
h.seek()   设置文件的指针位置
    h.seek(3)  跳到文件的第三个字符
    h.seek(-1,2) 跳到文件最后一个字符
    h.seek(-3,2) 跳到文件的倒数第三个字符
'''
#
# h = open(path,'a')
# h.write('22222')
# h.close()
#
# #
# h = open(path,'w+')
# h.read()
# h.write('hello world')
# h.close()

#
# h = open(path,'r+')
# print h.readline()
# print h.tell()
# h.write('Chinese English \n')
# h.close()

#
h = open(path,'r')
n = open(newpath,'w')
f = h.readlines()
h.close()
for x in range(len(f)):
    if x == 1:
        n.write('wd')
    else:
        n.write(f[x].rstrip().replace('reboot','hello'))
n.close()

'''
异常
在运行时不可预知的一些错误，

常见异常错误提示：

BaseException

'''

try:
    pass     #可能出错的代码
except:
    pass     #如果出错的操作
else:
    pass     #如果不出错指向的代码
finally:
    pass     #无论是否有错误都执行的代码

#example

try:
    1/0
except:
    print 'error'
else:
    print 'ok'
finally:
    print 'over'


try:
    open('/root/llll.txt','r')
    print 'ok'
except BaseException as e:
    print 'open error'
    print e

copy_list = [('/bin/wwww','/home/jcui/files/wbc')]

for src,dst in copy_list:
    sfile = ''
    dfile = ''
    try:
        sfile = open(src,'rb')
        dfile = open(dst,'wb')
        size = 4096
        while True:
            cxt = sfile.read(size)
            if not cxt:
                break
            dfile.write(cxt)
    except BaseException as e:
        print 'error'
        print e
    finally:
        if sfile:
            sfile.close()
        if dfile:
            dfile.close()


'''
前端开发
html     内容
css      美观
js       动作


html => 不严格的xml
具体实例见create_top.pys
'''


'''
函数

对一堆代码进行命名，这堆代码功能和名称功能对应，在以后使用的时候只使用函数的命名进行代码的调用

好处：
代码复用
见名知意

def name():
    pass
a,b,c = 1,2,3

def name(a,b,c):
    print a,b,c

name(a,b,c)

def name(A,B,C=1):
    print A,B,C

name(a,C=c,B=b)
'''


'''
函数返回值 return


'''

def fob(n):
    ll = ''
    for i in range(n+1):
        if i == 0 :
            x = 1
        elif i == 1:
            ll = 1
            x = x*i
        else:
            x = x * i
            ll = '%s x %s' % (ll,i)
    return '%s = %s' % (ll,x)
print fob(10)
print fob(4)

'''
函数的递归调用
'''
def fab(n):
    if n == 0 :
        return 1
    return n * fab(n-1)

print fab(3)

'''
函数的作用域
LGB  (变量查找顺序，从local，globa，built)
L =>  local  当前函数
G =>  globa  全局
B =>  built  内置

http://mushdog.sinaapp.com/publish/01.htm
http://mushdog.sinaapp.com/publish/02.htm
http://mushdog.sinaapp.com/publish/03.htm
http://mushdog.sinaapp.com/publish/04.htm
'''

gname = 'jcui'
ggname = ''
def test():
    lname = 'local jcui'
    print lname
    print gname
    print ggname

test()
print gname

print ''
def test1():
    gname = 'yhzhao'
    lname = 'local yhzhaos'
    print gname
    print lname
test1()
print gname

print ''
def test2():
    global gname
    gname = 'test jcui'
    print gname
test2()
print gname

print ''
#传值   （元祖和字典）
gname = 'jcui'
def test3(gname):
    print gname
    gname = 'local jcui'
    print gname
test3(gname)

print ''
#传址  (列表，地址类，指针类)
gname = ['globa name']
def test4(gname):
    print gname[0]
    gname[0] = 'local name'
    print gname[0]
test4(gname)

#不确定参数
def test4(*args):
    print args  #返回一个元祖

test4(1,2,43,54,)

def test5(**kwargs):
    print kwargs   #返回一个字典
test5(a=1,b=2,c=4)

def test6(name,age=20,*args,**kwrams):
    print name
    print age
    print args
    print kwrams
test6('kk',30,1,3,4,5,a=6,b=7)



def add_num(*args):
    rt = 0
    for x in args:
        rt += x
    return rt
print add_num(1,2,3,4,5,6)


'''
作业

一个list[(1,4),(5,1),(2,3)],根据每个元组中的较大值进行排序
期待结果：[(2,3),(1,4),(5,1)]


'''