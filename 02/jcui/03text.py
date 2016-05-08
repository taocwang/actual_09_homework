#encoding:utf-8
''
'''
第三课课堂内容
by 2016-05-08
'''

'''
字典
定义： {}包含，每个元素是由key：value的形式组成，每个元素通过逗号分割
通过key访问元素，删除元素，修改元素（dict中由存在的key）
'''
user = {'jcui':{'name':'jcui','age':30,'school':'PKBJ'},'yhzhao':{'name':'yhzhao','age':30,'school':'PKBJ'}}

#访问
print user['jcui']['name']
print user['jcui']['age']
#增加
user['jcui']['phone'] = 15110138508
print user
#删除
del user['yhzhao']['age']
print user
#修改
user['yhzhao']['age'] = 30
user['yhzhao']['age'] = 28
print user
#查询
print 'jcui' in user
print 'sss' in user
if 'age' in user['jcui']:
    print user['jcui']['age']


test = [['jcui','abc'],['age',18]]
print dict(test)

print len(user)       #注意len,in 只针对key

for i in user:
    print i,user[i]

#get
print user.get('jcui')
print user.get('vincent')   #返回null
print user.get('vincent','exist')   #返回exist

#copy  复制并重新生成一个新的dict
user2 = user         #user2和user 指向同一个地址
user3 = user.copy()  #user3 是新生成一个dict
user2['vincent'] = {'name':'vincent','age':25}
del user3['jcui']
print user2
print user3
print user

#clear 清空字典的所有元素
user3.clear()
print user3

#fromkesy   初始化字典
user3 = user3.fromkeys([1,2,3,54],True)
print user3

#has_key     判断key是否存在字典中
print user.has_key('jcui')

#items  以key：values 展示字典,结果为一个list
print user3.items()

#keys  打印key ,结果为一个list
print user3.keys()

#values  打印value ,结果为一个list
print user3.values()

#pop  指定key,删除当前key机value并返回,如果不存在则会报错.可以指定第二个参数为None或者指定字符串
print user3,'----'
print user3.pop(3)
# print user3.pop(3)        #报错
print user3.pop(3,None)
print user3.pop(3,'试试')

#popitem  每次随机删除一个，并返回
print user3.popitem()

#update
user = {}
user1 = {'name':'jcui'}
user2 = {'age':30 ,'school':'PKBJ'}
user1.update(user2)

print user1
print user.update(user1)

#setdefault  演示在下面


#遍历
for k,v in user3.items():
    print k,v


#zip()  list的合并,可以用于将list合并并转换为字典
user1 = ['jcui','vincent','yhzhao']
user2 = [3,4,5]

user3 = dict(zip(user1,user2))
print user3


#实现copy功能
user1 = {'age': 30, 'school': 'PKBJ', 'name': 'jcui'}
user2 = {}
for k,v in user1.items():
    user2[k] = v
print user2

user3 = {}
user3 = dict(zip(user1.keys(),user1.values()))
print user3


#统计每个字符串出现的次数
read_me = '''
first of all, i want make it clear that i can not claim understanding this holy book  in just a few weeks, and i would not dare comment on this sacred book, in addition, i don't think i can give you a full picture of the holy bible in just few words.i can not preach anything here. what i want to do here is to express my understanding by sharing two events described in this book. the fist story i want to share is abandoned tower of babel.according to the bibel,people use the same language to communicate with each other in ancient times.with the soaring vanity,they decided to build a heaven-reaching tower to show off their achievement, god knows, he change the human language into different kinds and make it difficult for people to communicate with each other,hence the failure of building tower of  babel.this story tells people,never do things in selfishness, but make a life out of enternal glory.the other story,before jesus christ was crucified,he said, father,forgive them, for they know not what they do. with great love, he shouldered all the sins of  people. what can we learn from this story?we live in this world thanks to the love of god, for this reanson, we should make our lives glorious to honor our god.finally,i want to sum up by saying that only if we put our lives in the eternal love of god,can we live a perfect life, and  what you appealed is what god expected!
'''
#方法1
str_keys = {}
for i in read_me:
    if i in str_keys:
        str_keys[i] += 1
    else:
        str_keys[i] = 1
print str_keys

#方法2
str_keys2 = {}
for i in read_me:
    if str_keys2.get(i):
        str_keys2[i] += 1
    else:
        str_keys2[i] = 1
print str_keys2

str_keys2.clear()
for i in read_me:
    str_keys2[i] = str_keys2.get(i,0) + 1
print str_keys2

#方法3
#setdefault
str_keys3 = {}
for i in read_me:
    str_keys3.setdefault(i,0)
    str_keys3[i] = str_keys3[i] + 1
print str_keys3

#课堂联系    score 成绩： 第一列数学，第二列语文，第三列英语
#统计每个学科每个分数区间的人数
nums = [
    {'name' : 'kk', 'score' : [61, 72, 80]},
    {'name' : 'kk2', 'score' : [52, 62, 60]},
    {'name' : 'kk3', 'score' : [43, 81, 64]},
    {'name' : 'kk4', 'score' : [64, 75, 65]},
    {'name' : 'kk5', 'score' : [75, 95, 66]},
    {'name' : 'kk6', 'score' : [82, 80, 72]},
    {'name' : 'kk7', 'score' : [61, 72, 90]},
    {'name' : 'kk8', 'score' : [82, 52, 73]},
    {'name' : 'kk9', 'score' : [73, 71, 74]},
    {'name' : 'kk10', 'score' : [64, 95, 85]},
    {'name' : 'kk11', 'score' : [65, 85, 66]},
    {'name' : 'kk12', 'score' : [92, 70, 82]},
]

# print nums
sorces = {}
names = {0:'math',1:'chinese',2:'english'}
for user in nums:
    for class_type in range(len(user['score'])):
        score_prefix = user['score'][class_type] / 10      #得到所在的范围区间
        key = (names[class_type],'%s0-%s9' % (score_prefix,score_prefix))    #得到格式化后的key
        sorces[key] = sorces.get(key,0) + 1
print sorces

rt_lisrt = []
for k,v in sorces.items():
    rt_lisrt.append(k + (v,))
print rt_lisrt


#将字典中的数据翻转

user = {
    'name':'jcui',
    'names':'jcui',
    '123':'WD',
    '1233':'WD',
    'age':33 ,
    'ages':35
}

user_re = {}
for k,v in user.items():
    if v not in user_re:
        user_re[v] = k
    else:
        if isinstance(user_re[v],list):
            user_re[v].append(k)
        else:
            user_re[v] = [user_re[v],k]
print user_re


user_re.clear()
for k,v in user.items():
    _user = user_re.get(v)
    if _user is None:
        user_re[v] = k
    elif isinstance(user_re,list):
        _user.append(k)
    else:
        user_re[v] = [_user,k]

print user_re,'====='


'''
字符串
'''
#方法：

list1 = ['abc','def','gh']
#join  连接字符串
print ','.join(list1)
print ':'.join(list1)
print '-'.join(list1)

#split  分割字符串
list1 = 'abc,de,er,er,er'
print list1.split(',')
print list1.split('c')
print list1.split('e')

#find   检查元素是否在字符串中
list1 = 'abc,de,er,er,er'
print list1.find('er')
print list1.find('z')  #如果查找不到则返回-1，不会报错

#index
list1 = 'abc,de,er,er,er'
print list1.index('c')
# print list1.index('z')      #如果查找不到则会报错

#capitallize  首字母大写
print list1.capitalize()

#upper  全部大写
print list1.upper()

#lower   全部小写
print list1.lower()

#实现首字母大写
list1 = 'aPPer'
print list1[0].upper()+list1[1:].lower()

#count 字符串统计
print list1.count('P')
print list1.count('r')

#replace  替换
print list1.replace('P','p',2)   #第三个字段表示替换重复出现的个数，默认为全部替换；0 不替换；1 替换一个；2 替换二个；


#lstrip  删除字符串左侧的空格和回车
#rstrip  删除字符串右侧空格和回车,指定字符串的时候，将删除字符串
#strip   删除字符串左右两侧的空格和回车
list1 = '  abc   '
print list1
list1 = list1.strip()
print list1

#endswith    以指定字符串结尾返回True

#startswith  以指定字符串开头返回True

#.format  占位符，等同于格式化的%

print 'mysql is {} ,versone {}'.format('my my ','5.5.18')
print 'mysql is {name} ,versone {ver}'.format(ver='5.5.18',name='mymy')

#isalnum   字母和数字返回True,否则False

print 'abc123'.isalnum()

#isalpha   字母返回True,否则False

print 'abc'.isalpha()

#isdigit   整数返回True,否则False

print '123'.isdigit()

#splitlines  按换行分割字符串

print 'asd \n edf'.splitlines()


#练习：‘reboot'字符串倒序  （不能用切片）
a = 'reboot'
b = list(a)
b.reverse()
print ''.join(b)

#练习：
#  最终输入用户的ID信息
#  比如用户输入user1:119，user2,118
#  最终输出[('user1','119')('user2','118')]

# user_get = raw_input('please input name1:nums1,name2:nums2')
user_get = 'jcui:123,wd:124,kk:1239'
list1 = user_get.strip()
list1 = user_get.split(',')
print list1
list2 = []
for x in list1:

    ll = tuple(x.split(':'))
    list2.append(ll)
print list2

rt_list = []
list = user_get.rstrip().split(',')
for i in list:
    i = i.strip()
    name,id = i.split(':')
    rt_list.append((name.strip(),int(id)))

print rt_list

print str_keys2 ,'============'

str_list = str_keys2.items()

print str_list
for x in range(len(str_list)-1):
    for i in range(0,len(str_list)-1-x):
        if str_list[i][1] > str_list[i+1][1]:
            str_list[i],str_list[i+1] = str_list[i+1],str_list[i]

print str_list[-1:-11:-1]
str_list.reverse()
print str_list[0:10]


'''
文件

文件路径：
绝对路径和相对路径
绝对路径：　/boot , /
相对路径：　当前进程启动目录

#文件读
# 找到文件
# 打开文件  open(path,mode)
    mode:
        r   读
        w   写
        a   追加
# 查看,修改(保存)
# 关闭

'''


path = '/home/jcui/files/text.txt'
files = open(path,'r')
cxt = files.read()
files.close()

print cxt

# read(size)  size可指定每次可读取的字节，
path = '/home/jcui/files/text.txt'
files = open(path,'r')
while True:
    cct = files.read(4)
    print cct
    if not cct:
        break
files.close()
# readlines(size)  size，指定字符或者换行，结束打印

path = '/home/jcui/files/text.txt'
files = open(path,'r')
while True:
    cct = files.readline(3)
    print cct
    if not cct:
        break
files.close()

# readlines    全部读取文件，返回一个list，每行一个元素

path = '/home/jcui/files/text.txt'
files = open(path,'r')
cet = files.readlines()
files.close()

print cet

# 迭代

path = '/home/jcui/files/text.txt'
files = open(path,'r')
for line in files:
    print line
files.close()

#读取文件并切割
# fiels = open(path,'r')
# user_get = files.read()
#
# rt_list = []
# list = user_get.rstrip().split(',')
# for i in list:
#     i = i.strip()
#     name,id = i.split(':')
#     rt_list.append((name.strip(),int(id)))
# print rt_list
# files.close()


#文件写
files = open(path,'w')
files.write('wd:123,jcui:123,kk:123')
files.close()

files = open(path,'w')
files.writelines(['wd:123,jcui:123,kk:123,','wd:123,jcui:123,kk:123',',wd:123,jcui:123,kk:123'])
files.close()

'''
server {{
    listen       {port} {server};
    server_name  {servername};

    access_log  {access_log}  main;

    location / {{
        root   {home};
        index  index.html index.htm;
        proxy_pass   http://127.0.0.1:{proxy_port};
    }}
}}

/home/shre/www_access_20140823.log
cat /home/shre/www_access_20140823.log |awk {print $1""$7""$9} |sort|uniq -c|sort -nr|head -10
'''