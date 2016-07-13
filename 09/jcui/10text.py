#encoding:utf-8
''

'''
面向对象

    站在提供者的角度 => 由什么东西,能提供什么东西
        属性
        方法
    封装:
        将属性(数据)和方法封装起来,只提供优先的方法或者属性给第三方者,不希望第三者操作的数据和方法对外屏蔽
        类  class
        定义:
            class Animal(object):
                pass
        类型:   type (3.*版本之前都是type类型,3.*之后是class)
        实例: 根据类的定义创建一个对象
            app = Flask(__name__)
            animal = Animal()

        构造函数: 在调用类去实例化对象时调用的函数
            __init__(self):
                print 'init'

            class Animal(object):
                def __init__(self):
                    self.name = ''
                    self.age = ''

            self:调用对象的引用(传址)

            -------------------------------------
        实例:
            属性:
                def __init__(self,*args,**kwargs)
                    self.attt = xxxx
            方法:
                def method(self,*agrs,**kwargs)
                    xxxx
                    return ''

        类型:
            属性:
                calss Animal(object):
                    atype = 'animal'

            方法:
                @classmethod
                def cmethod(class,*args,**kwargs)
                    xxx
                    return ''
        实例可以调用类的属性,方法
        类的方法内不能调用实例的属性和方法

        静态函数:
            class Utils(object)

                @staticmethod
                def smethod(*args,**kwargs)
                    xxxx
                    return ''

        私有属性和方法:
            __属性
            __方法

        @property
        @setter.xxx


    继承:
        继承者可以拥有父类的属性和方法
        class Animal(object):
            def __init__(self,name,age=1):
                self.name = name
                self.age = age
            def run(self):
                return self.name + ' run'
            def say(self):
                return self.name + ' say'


    多态:


'''

#类的定义,及判断是否为一个对象
class Animal(object):
    pass

print type(Animal)

animal = Animal()

print type(animal) == Animal
print isinstance(animal,Animal)


#属性 (先由属性,后有实例)

animal.name = 'wangwang'
animal.age = 2

print animal.name
print animal.age

#无参数
class Animal(object):
    def __init__(self):
        self.name = ''
        self.age = 1

animal = Animal()
print animal.name
print animal.age


#有参数
class Animal(object):
    def __init__(self,name,age=1):
        self.name = name
        self.age = age
    def say(self):
        return self.name + ' say'
    def run(self):
        return self.name + ' run'

dog = Animal('wangwang')
print dog.name
print dog.age
print dog.say()

cat = Animal('mimi',4)
print cat.name
print cat.age
print cat.run()



print '=================1===================='

class Animal(object):
    atype = 'animal'
    def __init__(self):
        pass

print Animal.atype
dog = Animal()
print dog.atype


Animal.atype = 'maomi'
print Animal.atype
cat = Animal()
print cat.atype

cat.atype = 'mimi'
print Animal.atype
print cat.atype




print '=================2===================='

class Animal(object):
    atype = 'animal'

    @classmethod
    def run(cls):
        print cls.atype, ' run'

print Animal.atype
wawa = Animal()

wawa.run()

#静态方法

class Utils(object):

    @staticmethod
    def md5(cxt):
        return 11111

print Utils.md5('22222')

#私有属性和方法

class Animal(object):
    def __init__(self,name,age):
        self.__name = name
        self.age = age
    def get_name(self):
        return self.__name

cat = Animal('ruhua',12)

print cat.get_name()
print cat.age
try:
    print cat.name
except BaseException as e:
    print e


print '=================3===================='
#继承
class Animal(object):
    def __init__(self, name, age=1):
        self.name = name
        self.age = age

    def run(self):
        return self.name + ' run'

    def say(self):
        return self.name + ' say'

class Dog(Animal):
    def __init__(self,name,age,variety):
        super(Dog, self).__init__(name,age)
        self.variety = variety
    def say(self):
        super(Dog,self).say()
        print self.variety,self.name + ':wangwangwang'
    def get_variety(self):
        print self.variety


xx = Dog('xiaohua',12,'bixiong')
xx.say()

yy = Dog('xiaohua',12,'hashiqi')
yy.get_variety()
yy.say()

'''
models
    1.dbutils
        Mysqlconnection
            属性:
                host
                port
                user
                password
                db
                charset
                conn
                cursor
            方法:
                fetch()
                execute()
                commit()
                close()
    2.user


    3.assets

    使用实例化方法:
    1.在从User中查找的时候,get*** classmethod => return User
    2.添加 90% => 创建用户User实例,validate save
    3.修改 60% => 创建用户信息(40%)
    4.删除 id => classmethod
           User.delete => classmethod

    sqlalcheemy

'''




print '=================4===================='
user = {'id':1 ,'username':'kk' ,'age':23}

def test (id,username,age):
    print id
    print username
    print age

test(id=user['id'],username=user['username'],age=user['age'])
print '等价于'
test(**user)

print '=================5===================='

print '=================6===================='

print '=================7===================='


'''
作业
1. assets 改为类的调用
2. user.删除 调用sweetalert
'''

'''
os,sys
* argparse
time / datatime
hashlib = md5
paramiko = ssh  cmd && scp
getpass
logging,traceback.format_exc()


'''