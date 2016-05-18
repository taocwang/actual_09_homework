1. 对list进行排序
  [(1,4),(5,1),(2,3)]
  比较的原则：按照list中每一个元素tuple中最大的值排序
  比较的元素:list中每一个元素中最大的值
  交换的元素
  max 函数获取list/tuple中最大的值

sort_list = [(1,4),(5,1),(2,3)]

for i in range(len(sort_list) - 1):
    if max(sort_list[i]) > max(sort_list[i + 1]): #比较元素
        #交换元素
        temp = sort_list[i]
        sort_list[i] = sort_list[i + 1]
        sort_list[i + 1] = temp
