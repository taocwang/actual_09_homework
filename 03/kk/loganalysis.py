#encoding: utf-8

#line = '42.92.56.130 - - [23/Aug/2014:23:58:56 +0800] "GET /data/uploads/2013/0422/08/51748b0ef04e8.JPG HTTP/1.1" 200 \ "http://image.baidu.com/i?ct=503316480&z=0&tn=baiduimagedetail&ipn=d&word=%E7%94%98%E8%82%83%E7%9C%81%E7%99%BD%E9%93%B6%E5%B8%82%E5%9B%BE%E7%89%87&step_word=&pn=414&spn=0&di=161249202510&rn=1&is=&istype=&ie=utf-8&oe=utf-8&in=2087&cl=2&lm=-1&st=&cs=4215836718%2C4107041133&os=281963354%2C3297720507&ln=1996&fr=&fmq=1408807884851_R&ic=&s=&se=&sme=0&tab=&width=&height=&face=&ist=&jit=&cg=&objurl=http%3A%2F%2Fwww.cihongcharity.org%2Fbbs%2FUploadFile%2F2013-8%2F201381518472144233.jpg&fromurl=ippr_z2C%24qAzdH3FAzdH3Fooo_z%26e3B2zfpk_z%26e3Bv54AzdH3Fri5p5AzdH3F%25E0%25l9%25lb%25Eb%25bd%25bn%25E0%25lC%25b8%25E0%25ll%25BD%25El%25ln%25Bm%25Ec%25Bb%25bd%25E9%25BA%25BA%25E0%25A9%25BE%25Ec%25B8%25ba_z%26e3Bip4s" "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/29.0.1547.66 Safari/537.36 LBBROWSER" "-"'
import time

s = time.time()
rs_dict = {}

handler = open('www_access_20140823.log', 'r')
for line in handler:
    nodes = line.split(' ')
    key = (nodes[0], nodes[6], nodes[8])
    rs_dict[key] = rs_dict.get(key, 0) + 1
    #key = (ip, url, code)
    #if key not in rs_dict:
    #    rs_dict[key] = 0
    #rs_dict[key] += 1

print 'stat after:', time.time() -s
s = time.time()

handler.close()
rs_list = rs_dict.items()
#[(key, value), (key1, value1)]
for j in range(10):
    for i in range(len(rs_list) - 1 - j):
        if rs_list[i][1] > rs_list[i + 1][1]:
            tmp = rs_list[i]
            rs_list[i] = rs_list[i + 1]
            rs_list[i + 1] = tmp
            rt_tmp = rs_list[-1:-11:-1]

for line in rs_list[-1:-11:-1]:
    print line

print 'ok:', time.time() - s
