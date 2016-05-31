#encoding:utf-8

#对日志进行处理,返回ip,url,code,nums
def log_anslysis(sfile):
    file_dict = {}
    try:
        files = open(sfile, 'r')
        for i in files:
            i = i.split()
            x, y, z = i[0], i[6], i[8]
            file_dict[(x, y, z)] = file_dict.get((x, y, z), 0) + 1
    except BaseException as e:
        print e
        return ''
    finally:
        if files:
            files.close()
    return sorted(file_dict.items(),key=lambda x:x[1],reverse=False)

if __name__ == "__main__":
    file = '/home/op/test/www_access_20140823.log'
    print log_anslysis(file)