# 面向对象编程
    站在提供者的角度==》我有什么东西，我能提供什么东西
        属性
        方法

       封装、继承、多态(python不涉及？)     鸭子类型

    1). 封装
        将属性(数据)和方法封装起来，只提供有限的方法或属性给第三者，不希望第三者操作的数据和方法对外屏蔽；

        类 class

        class Animal(object):
            pass

        实例： 根据类的定义创建一个对象
            animal = Animal()

        先有属性后有实例

        构建函数：
            在构造类去实例化对象时调用的函数
            __init__(self):
                print 'init'

        创建属性：
            动物：
                name
                type
                age

            class Animal(object):
                def __init__(self, name, type, age):
                    self.name = name
                    self.type = type
                    self.age = age

            self:是调用对象的引用

            实例：
                属性：
                    def __init__(self):
                        self.attr = xxx
                        # init没有返回值

                方法：
                    def method(self, *args, **kwargs):
                        xxxx
                        return ''
                        # 方法是需要有返回值的
            类型：
                属性：
                    class Animal(object):
                        atype = 'animal'

                方法：
                     @classmethod
                     def cmethod(cls, *args, **kwargs):
                        xxxx
                        return ''

            实例可以调用类的属性和方法
            类的方法不能调用实例的属性和方法

            静态函数：(常用于一些工具类的函数)
                @staticmethod
                def smethod(*args, **kwargs):
                    xxx
                    return

            私有属性和方法：
                __属性
                __方法
    2). 继承

        继承者可以拥有父类的属性和方法

        class Animal(object):
        def __init__(self, name, age):
            self.name = name
            self.age = age

        def say(self):
            print self.name + 'say'
        def run(self):
            print self.name + 'run'

        class Dog(Animal):
            pass

# models

    1). dbutils
        MySQLConnection
            属性
                host
                port
                user
                passwd
                db
                charset
                conn
                cursor
            方法
                fetch()
                execute()
                commit()
                close()
        笔记：
        except BaseException as e:
            import traceback
            print traceback.format_exc()
            print e
        # 上面这段代码在调试错误的时候，打印全部错误


    2). user
    3). asset
