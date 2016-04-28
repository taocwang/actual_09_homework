#encoding: utf-8

num_list = [1, 3, 4, 5, 6]
find_num = int(raw_input('please input a num:'))
start = 0
end = len(num_list) - 1

while True:
    middle = (start + end) / 2
    if find_num == num_list[middle]:
        print u'找到了, 索引为:%s' % middle
        break
    elif find_num > num_list[middle]:
        print u'在后半段'
        start = middle + 1
    else:
        print u'在前半段'
        end = middle - 1
    if start > end:
        print u'找不到'
        break        
