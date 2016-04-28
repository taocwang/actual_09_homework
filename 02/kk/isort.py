#encoding: utf-8
num_list = [6, 4, 5, 3, 1]
for i in range(1, len(num_list)):
    for j in range(i, 0, -1):
        if num_list[j - 1] > num_list[j]:
            # a, b = b, a(交换)
            num_list[j - 1], num_list[j] = num_list[j], num_list[j - 1]
        else:
            break
    print num_list

print num_list