#encoding: utf-8

num_list = [6,5,2,10,4,8]
for i in range(1,len(num_list)):
    for j in range(i,0,-1):
        if num_list[j - 1] > num_list[j]:
            #a, b = b, a(交换)、
            num_list[j - 1], num_list[j] = num_list[j], num_list[j - 1]
        else:
                break
    print num_list

print num_list