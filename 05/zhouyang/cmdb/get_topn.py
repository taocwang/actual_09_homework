#coding:utf-8
'''从nginx的日志中找出access前n的信息'''

def get_topn(file,n=10):
    acc_topn_dict={}
    with open(file,'r') as content:
        for line in content:
            line_list=line.split()
            ip,file_path,stat=line_list[0],line_list[6],line_list[8]
            key=(ip,file_path,stat)
            acc_topn_dict[key]=acc_topn_dict.get(key,0) + 1

    rt_topn=acc_topn_dict.items()
    rt_topn.sort(key=lambda x:x[1])
    return rt_topn[-1:-(n+1):-1]


if __name__=='__main__':
    log_file="www_access_20140823.log"
    print get_topn(log_file,3)
