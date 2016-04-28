1. 插入排序

描述: 首先有一个有序序列, 插入一个元素, 结果保证依然是一个有序的序列

[1, 3, 5], 2
[1, 2, 3, 5]

问题: 要找到新插入元素在有序序列中的插入位置
怎么找插入位置: 将新插入的元素依次从右到左和序列中的元素比较，找到第一个比它小或者它已经是第一个元素（元素比它大，交换）
[1, 3, 5], 2
[1, 3, 2, 5]
[1, 2, 3, 5]

[6, 4, 5, 3, 1]
如果序列中只有一个元素, 可以认为序列有序
把第二个元素插入到由第一个元素组成的序列中，结果保证插入后依然是一个有序的
[4, 6, 5, 3, 1]
第三个元素插入到有前两个元素组成的序列中，结果保证插入后依然是一个有序的
[4, 5, 6, 3, 1]

可以从序列的第二个元素开始 直到 最后一个元素，将N个元素插入到前面N-1个元素组成的有序序列中
第四个元素插入到前面3个元素组成的序列中， 保证插入后是一个有序的
[4, 5, 3, 6, 1]
[4, 3, 5, 6, 1]
[3, 4, 5, 6, 1]
第5个元素插入到前面4个元素组成的序列中， 保证插入后是一个有序的
[3, 4, 5, 1, 6]
[3, 4, 1, 5, 6]
[3, 1, 4, 5, 6]
[1, 3, 4, 5, 6]


num_list = [6, 4, 5, 3, 1]
for i in range(1, len(num_list)):
    for j in range(i, 0, -1):
        if num_list[j - 1] > num_list[j]:
            # a, b = b, a(交换)
            num_list[j - 1], num_list[j] = num_list[j], num_list[j - 1]
        else:
            break


2. 二分法查找

描述: 在一个有序序列(从小到大)中查找一个元素
      需要每次将查找的元素和序列中间位置的元素进行比较
      1. 查找 == 中间, 找到了
      2. 查找 > 中间, 查找的元素在序列中后半段中
      3. 查找 < 中间, 在前半段

num_list = [1, 3, 4, 5, 6]

a.
find_num = 1
start = 0
end = len(num_list) - 1(4)
middle = (start + end) / 2(2)

find_num < num_list[middle]
start = 0
end = middle - 1(1)
middle = (start + end) / 2(0)

find_num == num_list[middle]


num_list = [1, 3, 4, 5, 6]
b.
find_num = 6
start = 0
end = len(num_list) - 1(4)
middle = (start + end) / 2(2)

find_num > num_list[middle]
start = middle + 1(3)
end = len(num_list) - 1(4)
middle = (start + end) / 2(3)

find_num > num_list[middle]
start = middle + 1(4)
end = len(num_list) - 1(4)
middle = (start + end) / 2(4)

find_num == num_list[middle]


num_list = [1, 3, 4, 5, 6]
c.
find_num = 2
start = 0
end = len(num_list) - 1(4)
middle = (start + end) / 2(2)

find_num < num_list[middle]
start = 0
end = middle - 1(1)
middle = (start + end) / 2 (0)

find_num > num_list[middle]
start = middle + 1(1)
end = 1
middle = (start + end) / 2(1)

find_num < num_list[middle]
start = 1
end = middle - 1(0)
start > end => 未找到

num_list = [1, 3, 4, 5, 6]
find_num = int(raw_input('please input a num:'))
start = 0
end = len(num_list) - 1

while True:
    middle = (start + end) / 2
    if find_num == num_list[middle]:
        print '找到了, 索引为:%s' % middle
        break
    elif find_num > num_list[middle]:
        print '在后半段'
        start = middle + 1
    else:
        print '在前半段'
        end = middle - 1
    if start > end:
        print '找不到'
        break        
