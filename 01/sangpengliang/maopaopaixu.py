#encoding:utf-8
array = [165,168,179,173,175,178]

for i in range(len(array)):
    for j in range(i):
        if array[j] > array[j + 1]:
            array[j], array[j + 1] = array[j + 1], array[j]
print array