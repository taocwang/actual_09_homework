#encoding:utf-8
''
import random

'''
作业

一个list[(1,4),(5,1),(2,3)],根据每个元组中的较大值进行排序
期待结果：[(2,3),(1,4),(5,1)]


'''
#方法一
def max_num_sort(lists):
    for n in range(len(lists)-1):
        for i in range(len(lists)-1):
            if max(lists[i]) > max(lists[i+1]):
                lists[i],lists[i+1] = lists[i+1],lists[i]
    print lists


#方法二
def max_num(tuples,reverse=False):
    nums = tuples[0]
    for i in tuples:
        if reverse :
            if i < nums:
                nums = i
        else:
            if i > nums:
                nums = i
    return nums


def list_sort(lists,reverse=False):
    reverse = reverse
    for n in range(len(lists)-1):
        for i in range(len(lists)-1):
            if max_num(lists[i],reverse=reverse) > max_num(lists[i+1],reverse=reverse):
                lists[i], lists[i + 1] = lists[i + 1], lists[i]
    print  lists

#随机生成列表
def random_list(n):
    num_lists = []
    for i in range(n):
        a = tuple(random.sample(range(0,100),2))
        num_lists.append(a)
    return num_lists



if __name__ == '__main__':
    num_list1 = [(1, 4), (5, 1), (2, 3), (10, 2), (6, 3)]
    max_num_sort(num_list1)
    num_list2 = [(11, 4), (5, 1), (2, 3), (10, 2), (6, 3),(23,4,43,4),(34,45),(1,1,1,1,1)]
    list_sort(num_list2)
    x = random_list(10)
    #按元祖中的最大值进行排序
    list_sort(x,reverse=False)
    #按元祖中的最小值进行排序
    list_sort(x, reverse=True)