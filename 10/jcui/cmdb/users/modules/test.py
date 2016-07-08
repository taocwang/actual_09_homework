#encoding:utf-8
def ip_check(ip):
    q = ip.split('.')
    return len(q) == 4 and len(filter(lambda x: x >= 0 and x <= 255, \
        map(int, filter(lambda x: x.isdigit(), q)))) == 4



# class Assete(object):
#     def __init__(self,id,**kwargs):
#         self.id = id
#         for k,v in kwargs.iteritems():
#             setattr(self,k,v)
#
#
# class Person1(object):
#     def __init__(self, name, score):
#         self.name = name
#         self.__score = score
#     def get_score(self):
#         return self.__score
#
# class Person2(object):
#     count = 30
#     def  __init__(self,name):
#         self.name = name
#         Person2.count = Person2.count + 1

class Person(object):
    def __init__(self,name,score):
        self.name = name
        self.score = score
        self.ll = lambda :'A'
    def get_grade(self):
        if self.score >  80 :
            return self.name + ': 优'
        elif self.score >60 :
            return self.name + ': 良'
        else:
            return self.name + ': 差'

class Student(Person):
    def __init__(self,name,score,pp):
        super(Student,self).__init__(name,score)
        self.pp = pp

import json

class Tt(object):
    def __init__(self,lists):
        self.lists = lists
    def read(self):
        return self.lists



if __name__ == '__main__':
    # print help(dict.iteritems)
    # print help(dict.items)

    # a = {
    #     'name':'jcui',
    #     'age':18,
    #     'grade':'3'
    # }
    # print a.items()    #返回一个列表
    # print a.iteritems()   #返回一个迭代对象
    #
    # p1 = Person2('Bob')
    # print Person2.count
    #
    # p2 = Person2('Alice')
    # print Person2.count
    #
    # p3 = Person2('Tim')
    # print Person2.count
    #
    # print lambda : 'a'
    p1 = Person('jcui',60)
    print p1.get_grade()
    print p1.ll

    p2 = Student('kk',60,'feifei')
    print p2.get_grade()
    print p2.pp
    print p2.name

    s = Tt('["Tim", "Bob", "Alice"]')
    print json.load(s)