d = [1,3,5,22,45000,33,1,3,4,5,567,23424,4,2,567,3332]
max1 = 0
max2 = 0
for i in d:
    if i > max1:
        max1 = i 
    for j in d:
        if  max2 < max1 and j != max1:
            max2 = j
print max2
print max1
