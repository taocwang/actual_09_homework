#!/usr/bin/env python
# -*- coding: utf-8 -*-
import copy
from Canvas import Line
# users = dict((('a','D'),('b',(1,2,3)),('c',{'A':1,'B':'D'})))
# print 'D' in users.values()
# for i in users:
#     print i,users[i]
#     
# users1=users
# users2=users.copy()
# users1['a']=123
# print users
# print users1
# print users2
# 
# users={'xxx':123,'yyy':456}
# print dict.fromkeys(users,3)
# 
# print zip(['a','b','c'],[1,2,3,4])
# for k,v in users.items():
#     print str(k) +' ==> '+ str(v)
#     
# a={'a':123,'b':[1,2,3,4,5],'c':6}
# b=copy.deepcopy(a)
# a['b'][1]=100
# print a,id(a['b'])
# print b,id(b['b'])

# a={'a':123,'b':[1,2,3,4,5],'c':6}
# b={}
# for i in a.keys():
#     b[i]=a[i]
# print b

# a=['a','b','c']
# b=[1,2,3,4]
# c=['a','s','d']
# print zip(a,b,c)
# 
# read_me='''
# first of all, i want make it clear that i can not claim understanding this holy book  in just a few weeks, and i would not dare comment on this sacred book, in addition, i don't think i can give you a full picture of the holy bible in just few words.i can not preach anything here. what i want to do here is to express my understanding by sharing two events described in this book. the fist story i want to share is abandoned tower of babel.according to the bibel,people use the same language to communicate with each other in ancient times.with the soaring vanity,they decided to build a heaven-reaching tower to show off their achievement, god knows, he change the human language into different kinds and make it difficult for people to communicate with each other,hence the failure of building tower of  babel.this story tells people,never do things in selfishness, but make a life out of enternal glory.the other story,before jesus christ was crucified,he said, father,forgive them, for they know not what they do. with great love, he shouldered all the sins of  people. what can we learn from this story?we live in this world thanks to the love of god, for this reanson, we should make our lives glorious to honor our god.finally,i want to sum up by saying that only if we put our lives in the eternal love of god,can we live a perfect life, and  what you appealed is what god expected!
# '''
# a=list(set(read_me))
# b={}
# for i in a:
#     b[i]=list(read_me).count(i)
# print b
# chars_dict={}
# for c in read_me:
#     if c not in chars_dict:
#         chars_dict[c]=1
#     else:
#         chars_dict[c]+=1
# print chars_dict
# chars_dict={}
# for c in read_me:
#     if c not in chars_dict:
#         chars_dict[c]=0
#     chars_dict[c]+=1
# print chars_dict
# chars_dict={}
# for c in read_me:
#     chars_dict[c]=chars_dict.get(c,0)+1
# print chars_dict
# chars_dict={}
# for c in read_me:
#     chars_dict.setdefault(c,0)
#     chars_dict[c]+=1
# print chars_dict


# users=[
#     {'name' : 'kk', 'score' : [61, 72, 80]},
#     {'name' : 'kk2', 'score' : [52, 62, 60]},
#     {'name' : 'kk3', 'score' : [43, 81, 64]},
#     {'name' : 'kk4', 'score' : [64, 75, 65]},
#     {'name' : 'kk5', 'score' : [75, 95, 66]},
#     {'name' : 'kk6', 'score' : [82, 80, 72]},
#     {'name' : 'kk7', 'score' : [61, 72, 90]},
#     {'name' : 'kk8', 'score' : [82, 52, 73]},
#     {'name' : 'kk9', 'score' : [73, 71, 74]},
#     {'name' : 'kk10', 'score' : [64, 95, 85]},
#     {'name' : 'kk11', 'score' : [65, 85, 66]},
#     {'name' : 'kk12', 'score' : [92, 70, 82]},
# ]
# scores={}
# class_name_dict={0:'数学',1:'语文',2:'英语'}
# for user in users:
#     for class_type in range(0,3):
#         score_prefix=user['score'][class_type]/10
#         key=(class_name_dict[class_type],'%s0-%s9'%(score_prefix,score_prefix))
#         scores[key]=scores.get(key,0)+1
# scoreslist=[]
# for i in scores:
#     scoreslist.append([i[0],i[1],scores[i]])
# scoreslist.sort( key=lambda x:x[0])
# for i in scoreslist:
#     print i[0]+'\t'+i[1]+'\t'+str(i[2])


# users={'a':1,'b':2,'c':3}
# print users.pop('c',None)
# print users.pop('c',None)
# print users.popitem()
# print users.popitem()
# print users.popitem()


# users={'a':1,'b':2,'c':3}
# users.update({'a':'xxx','d':678})
# print users


# sour_teachers={'teach':'pc','waihao':'pc','name':'pc','age':12,'job':'IT'}
# dest_teachers={}
# for i in sour_teachers:
#     if sour_teachers[i] not in dest_teachers:
#         dest_teachers[sour_teachers[i]]=i
#     else:
#         if isinstance(dest_teachers[sour_teachers[i]], list):
#             dest_teachers[sour_teachers[i]].append(i)
#         else:
#             dest_teachers[sour_teachers[i]]=[dest_teachers[sour_teachers[i]],i]
# print dest_teachers

# sour_teachers={'teach':'pc','waihao':'pc','name':'pc','age':12,'job':'IT'}
# dest_teachers={}
# for k,v in sour_teachers.items():
#     dest_value=dest_teachers.get(v)
#     if dest_value == None:
#         dest_teachers[v]=k
#     else:
#         if isinstance(dest_value,list):
#             dest_teachers[v].append(k)
#         else:
#             dest_teachers[v]=[dest_teachers[v],k]
# print dest_teachers

'''
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
字符串
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
'''
#print dir(str)
# char_stats={'a':5,'b':3,'e':8,'f':5}
# print char_stats
# print sorted(char_stats.items(),key=lambda x:x[1],reverse=True)
# read_me='''
# first of all, i want make it clear that i can not claim understanding this holy book  in just a few weeks, and i would not dare comment on this sacred book, in addition, i don't think i can give you a full picture of the holy bible in just few words.i can not preach anything here. what i want to do here is to express my understanding by sharing two events described in this book. the fist story i want to share is abandoned tower of babel.according to the bibel,people use the same language to communicate with each other in ancient times.with the soaring vanity,they decided to build a heaven-reaching tower to show off their achievement, god knows, he change the human language into different kinds and make it difficult for people to communicate with each other,hence the failure of building tower of  babel.this story tells people,never do things in selfishness, but make a life out of enternal glory.the other story,before jesus christ was crucified,he said, father,forgive them, for they know not what they do. with great love, he shouldered all the sins of  people. what can we learn from this story?we live in this world thanks to the love of god, for this reanson, we should make our lives glorious to honor our god.finally,i want to sum up by saying that only if we put our lives in the eternal love of god,can we live a perfect life, and  what you appealed is what god expected!
# '''
# chars_dict={}
# for c in read_me:
#     chars_dict[c]=chars_dict.get(c,0)+1
# char_list=chars_dict.items()
# for i in range(0,len(char_list)-1):
#     for j in range(i+1,len(char_list)):
#         if char_list[i][1]>char_list[j][1]:
#             char_list[i],char_list[j]=char_list[j],char_list[i]
# print char_list[-1:-11:-1]

# print "my name is {:<50},my age is {:>50} years".format('huxianglin', 23)

'''
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
文件操作
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
'''
# f = open('test.txt','r')
# for line in f.readlines():
#    print line,
# f.close() 


# f=open('test.txt','r')
# users=f.readline().strip().split(',')
# new_user=[]
# for i in users:
#     user,pwd=i.split(':')
#     new_user.append((user,pwd))
# f.close()
# print new_user

# f=open('test.txt','w')
# f.write('kk:12,woniu:34,pc:56,wd:32')
# f.close()


