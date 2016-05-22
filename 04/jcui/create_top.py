#encoding:utf-8

page_tmp = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>{title}</title>
</head>
<body>
    <table border="1" align="left">
        <thead>
            <tr>
                {thead}
            </tr>
        </thead>
        <tbody>
            {tbody}
        </tbody>
        <tfoot>
            <tr>

            </tr>
        </tfoot>
    </table>

</body>
</html>
'''

def log_anslysis(sfile,dfile,topnum=10):
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

    title = 'Top %s 访问日志' % topnum
    thead = '<th>Num</th><th>IP</th><th>URL</th><th>STATE</th><th>NUMS</th>'
    tbody = ''
    for x in range(topnum):
        i = file_list[-1-x]
        tbody += '<tr><td>{nn}</td><td>{ip}</td><td>{url}</td><td>{status}</td><td>{nums}</td></tr>'.format(ip=i[0][0],
                                                                                                            url=i[0][1],
                                                                                                            status=i[0][
                                                                                                                2],
                                                                                                            nums=i[1],
                                                                                                            nn=x+1)
    # for i in file_list[-1:(0-topnum-1):-1]:
    #     tbody += '<tr><td>{nn}</td><td>{ip}</td><td>{url}</td><td>{status}</td><td>{nums}</td></tr>'.format(ip=i[0][0], url=i[0][1],
    #                                                                                            status=i[0][2],
    #                                                                                            nums=i[1],nn=(len(file_list)-file_list.index(i)))
    return  page_tmp.format(title=title, thead=thead, tbody=tbody)
    # f = open(dfile, 'w')
    # f.write(page_tmp.format(title=title, thead=thead, tbody=tbody))
    # f.close()


# topnum = 30
# a = '/home/jcui/files/www_access_20140823.log'
# b = '/home/jcui/files/top%s.html' % topnum
#
# log_anslysis(dfile=b,topnum=topnum,sfile=a)