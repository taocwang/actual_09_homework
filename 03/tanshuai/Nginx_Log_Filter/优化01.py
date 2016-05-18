#!/usr/bin/env python
# -*- coding: utf-8 -*-
import time
s = time.time()

# 将统计结果放入dict
files_dict = {}
files = open('www_access_20140823.log', 'rb')
for line in files:
    src_list = line.split()
    IP, URL, Status = src_list[0], src_list[6], src_list[8]
    files_dict[(IP, URL, Status)] = files_dict.get((IP, URL, Status), 0) + 1
files.close()

# dict反转
new_dict = {}
for key, value in files_dict.items():
    new_dict.setdefault(value, [])
    new_dict[value].append(key)
arr = new_dict.keys()
print arr

count = 0
tableStr = '<table border = "1">'
trTmpl = '''
    <tr>
        <td>%s</td>
        <td>%s</td>
        <td>%s</td>
        <td>%s</td>
        <td>%s</td>
    </tr>
'''
tableStr += trTmpl % ('NO', 'IP', 'URL', 'STATUS', 'COUNT')
while count < 30:
    max_num = max(arr)
    tmp = new_dict[max_num]
    for tup in new_dict[max_num]:
        tableStr += trTmpl % (count + 1, tup[0], tup[1], tup[2], max_num)

    (count +1 , new_dict[max_num], max_num)
    # count += len(new_dict[max_num])
    count += 1
    arr.remove(max_num)
tableStr += '</table>'

f = open('res.html', 'w')
f.write(tableStr)
f.close()

print 'ok:', time.time() - s

