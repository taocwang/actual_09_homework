# encoding: utf-8

num_list = [1,12,9,10,11,3,5,7,2,1,3,33,44,22,66]

for i in range(1,len(num_list)):
## 每第一次循环i为1的时候，产生的列表是[1]对应num_list的值是12.if比较也就是12<1 。然后不小继续循环
## 当第二次循环i为2的时候.产生的列表是[2,1]对应num_list的值是9,12 if比较也就是 9<12就调换位置。然后依次循环直到完成
        for j in range(i,0,-1):
#               print j
                if num_list[j] < num_list[j - 1]:
                        num_list[j],num_list[j - 1] = num_list[j - 1],num_list[j]
#       print num_list

print num_list