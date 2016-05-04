#encoding: utf-8


num_list = [1,2,3,2,12,3,1,3,21,2,2,3,4111,22,3333,444,111,4,5,777,65555,45,33,45]

for i in range(0,len(num_list) -1):
    print i
    for j in range(i+1, len(num_list)):
        print j
        if num_list[i] > num_list[j]:
            num_list[i],num_list[j] = num_list[j],num_list[i]
            print num_list