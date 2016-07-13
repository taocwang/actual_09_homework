#!encoding: utf-8
list=[(1,4),(5,1),(2,3)]

for j in range(len(list) -1):
  for i in range(len(list) -1):
     if max(list[i]) > max(list[i + 1]):
         list[i],list[i + 1] =list[i + 1],list[i]
print '1 num'
print list


def sort_list(list1):
  for j in range(len(list1) -1): 
    for i in range(len(list1) -1):
       if max(list1[i]) > max(list1[i + 1]):
           list1[i],list1[i + 1] =list1[i + 1],list1[i]

print '2 num'
list=[(1,4),(5,1),(2,3)]
sort_list(list)
print list


def sort_list2(list1):
  temp_list = list1[:]
  for j in range(len(temp_list) -1): 
    for i in range(len(temp_list) -1):
        if max(temp_list[i]) > max(temp_list[i + 1]):
           temp_list[i],temp_list[i + 1] =temp_list[i + 1],temp_list[i]
  return temp_list

print '3 num'
list=[(1,4),(5,1),(2,3)]
print sort_list2(list)
print list




def sort_max(x):
  max_num = x[0]
  for i in x:
      if max_num <  i:
          max_num = i
  return max_num

def sort_list2(list1):
  temp_list = list1[:]
  for j in range(len(temp_list) -1):
    for i in range(len(temp_list) -1):
        if sort_max(temp_list[i]) > sort_max(temp_list[i + 1]):
           temp_list[i],temp_list[i + 1] =temp_list[i + 1],temp_list[i]
  return temp_list

print '4 num'
list=[(1,4),(5,1),(2,3)]
print sort_list2(list)
print list
