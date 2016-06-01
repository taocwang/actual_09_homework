#encoding:utf-8
import gconfig,dbutils,datetime
def get_desc(srcpath):
    handle=file(gconfig.file_path + srcpath, 'r')
    # handle1=file(path + '/result.txt', 'wb')
    rt_dict={}
    while 1:
        line =handle.readline()
        if not line:
            break
        nodes = line.split()
        ip,url,code = nodes[0],nodes[6],nodes[8]
        key = (ip,url,code)
        if key not in rt_dict:
            rt_dict[key]=1
        else:
            rt_dict[key]=rt_dict[key]+1
    rt_list=rt_dict.items()
    handle.close()
    return rt_list

    # print "format done"
    # rt_list=rt_dict.items()
    # print len(rt_list)
    # for j in range(len(rt_list)):
    #     for i in range(len(rt_list)-1):
    #         if rt_list[i][1]>rt_list[i+1][1]:
    #             rt_list[i],rt_list[i+1]=rt_list[i+1],rt_list[i]
    # return rt_list[-1:-len(rt_list)-1:-1]


# def create_talble(tname,id,ip,url,code,count):
#     sql='create table %s(%s int primary key auto_increment,%s varchar(25), %s text,%s int,%s int)engine=innodb default charset utf8;'
#     args=(tname,id,ip,url,code,count)
#     fetch =False
#     dbutils.execute_sql(sql,args,fetch)


if __name__=="__main__":
    print datetime.datetime.now()
    srcpath = '/www_access_20140823.log'
    # srcpath = '/test.txt'
    # despath = "/top10.html"
    # loganalysis(srcpath,"/top15.html",15)
    olist=get_desc(srcpath)
    print len(olist)
    for info in olist:
        ip=info[0][0]
        url=info[0][1]
        code=info[0][2]
        cnt=info[1]
        args=(ip,url,code,cnt)
        sql='insert into nginx_log(ip,url,code,cnt) values(%s,%s,%s,%s)'
        fetch =False
        dbutils.execute_sql(sql,args,fetch)
    print datetime.datetime.now()