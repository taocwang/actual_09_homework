#encoding:utf-8

def log_anslysis(sfile,topnum=10):
    if topnum == 10:
        dfile = '/home/jcui/files/top%s.html' % topnum
    file_dict = {}
    path = sfile
    files1 = open(path, 'r')
    for i in files1:
        i = i.split()
        x, y, z = i[0], i[6], i[8]
        file_dict[(x, y, z)] = file_dict.get((x, y, z), 0) + 1
    files1.close()
    file_list = file_dict.items()
    for n in range(topnum):  # (由于只取top10,所以找出最大的10个值即可,该值可作为参数传递给函数调用)
        for i in range(0, len(file_list) - 1):
            if file_list[i][1] > file_list[i + 1][1]:
                file_list[i], file_list[i + 1] = file_list[i + 1], file_list[i]

    return file_list[-1:(0-topnum-1):-1]