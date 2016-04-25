#encoding:utf-8
''
'''
#插入排序
    所谓插入排序法，就是检查第i个数字，如果在它的左边的数字比它大，进行交换，这个动作一直继续下去，直到这个数字的左边数字比它还要小，就可以停止了。插入排序法主要的回圈有两个变数：i和j，每一次执行这个回圈，就会将第i个数字放到左边恰当的位置去。
'''
num_list = [23,344,34,5,6,-1,213,123,435]
# nums = int(raw_input('please input a num:'))


#二分查找



#随机抽取







'''
#选择排序 (请老师帮忙看下这个算法的写法是否正确,我是根据理解自己写的)
    选择排序：比如在一个长度为N的无序数组中，在第一趟遍历N个数据，找出其中最小的数值与第一个元素交换，第二趟遍历剩下的N-1个数据，找出其中最小的数值与第二个元素交换......第N-1趟遍历剩下的2个数据，找出其中最小的数值与第N-1个元素交换，至此选择排序完成。
'''
num_list = [23,344,34,5,6,-1,213,65535,123,435,10]

for i in range(0,len(num_list)-1):  #循环次数
    index = i
    for x in range(i+1,len(num_list)):
        if num_list[index] > num_list[x]:   #找到最小的数
            index = x
    print num_list[i],num_list[index]
    num_list[i],num_list[index] = num_list[index],num_list[i]   #将最小的数与当前队列第一个做交换
print "选择排序",num_list


'''
#冒泡排序
    它重复地走访过要排序的数列，一次比较两个元素，如果他们的顺序错误就把他们交换过来。走访数列的工作是重复地进行直到没有再需要交换，也就是说该数列已经排序完成
'''
num_list = [23,344,34,5,6,-1,213,65535,123,435,10]
for x in range(0,len(num_list)-1):  #循环次数
    for y in range(0,len(num_list)-1-x):
        if num_list[y] > num_list[y+1]:    #每两个比较
            num_list[y],num_list[y+1] = num_list[y+1],num_list[y]    #对调

print "冒泡排序",num_list
