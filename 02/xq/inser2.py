#!/usr/bin/env python
# coding=utf-8


l=[3,2,4,6,3,10,2,33,55,21,99,1]
print "排序前为：%s" %l
def insertion_sort(list2):
    #从列表第二个元素开始插入
    for i in range(1, len(list2)):
        #先将待插入元素放入一个临时空间
        save = list2[i]
        j = i
        #比较待插入元素和之前已经排好序的大小，若比排好序的末尾元素小，则将末尾元素放入下一个坑
        while j > 0 and list2[j - 1] > save:
            list2[j] = list2[j - 1]
            j -= 1
            print "插入前为:%s" %l
            print '+' *40
        list2[j] = save
        print "排序了为：%s" %l

insertion_sort(l)
print "排序后为%s" %l
