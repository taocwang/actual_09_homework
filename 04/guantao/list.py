#coding:utf-8


LIST_NUM = [(1,4),(5,1),(2,3),(6,9),(7,1)]
'''
用max函数获取到元素的最大值，然后用冒泡进行排序


'''

for j in range(len(LIST_NUM) -1):
    for i in range(len(LIST_NUM) -1):
        if max(LIST_NUM[i]) > max(LIST_NUM[i + 1]):
            A = LIST_NUM[i]
            LIST_NUM[i] = LIST_NUM[i + 1]
            LIST_NUM[i + 1] = A

print LIST_NUM
