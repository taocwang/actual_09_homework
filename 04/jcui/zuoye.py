#encoding:utf-8
''
import random

'''
作业

一个list[(1,4),(5,1),(2,3)],根据每个元组中的较大值进行排序
期待结果：[(2,3),(1,4),(5,1)]


'''
#方法一
def max_num_sort(lists):
    for n in range(len(lists)-1):
        for i in range(len(lists)-1):
            if max(lists[i]) > max(lists[i+1]):
                lists[i],lists[i+1] = lists[i+1],lists[i]
    print lists


#方法二
def max_num(tuples,reverse=False):
    nums = tuples[0]
    for i in tuples:
        if reverse :
            if i < nums:
                nums = i
        else:
            if i > nums:
                nums = i
    return nums


def list_sort(lists,reverse=False):
    reverse = reverse
    for n in range(len(lists)-1):
        for i in range(len(lists)-1):
            if max_num(lists[i],reverse=reverse) > max_num(lists[i+1],reverse=reverse):
                lists[i], lists[i + 1] = lists[i + 1], lists[i]
    return  lists

#随机生成列表
def random_list(n):
    num_lists = []
    for i in range(n):
        a = tuple(random.sample(range(0,100),random.randint(2,6)))
        num_lists.append(a)
    return num_lists


def page_tmp(thead,tbody,reverse):
    page_tmp = '''
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>{title}</title>
    </head>
    <body>
        <tr>
            <h1>{title}</h1>
        </tr>
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
    if not reverse :
        title = "按元祖内数字大小排序(按最大值排序)"
    else:
        title = "按元祖内数字大小排序(按最小值排序)"
    return page_tmp.format(title = title,thead = thead,tbody = tbody)

def create_page(x,path,reverse=False):
    thead = '<th>名称</th>'
    #原列表
    tbody = '<th>原列表</th>'
    for i in range(0,len(x)):
        thead += '<th>%s</th>' % (i+1)
        tbody += '<th>%s</th>' % str(x[i]).strip('()')

    #原列表中每个元祖的最大值或最小值
    tbody += '<tr><th>比较值</th>'
    for i in range(0,len(x)):
        tbody += '<th style="color:red;">%s</th>' % (max_num(x[i],reverse=reverse))
    tbody += '</tr>'
    #新列表
    tbody += '<tr><th>新列表</th>'
    new_list = list_sort(x,reverse=reverse)
    for i in range(0,len(x)):
        tbody += '<th>%s</th>' % str(new_list[i]).strip('()')
    tbody += '</tr>'

    #生成html
    try:
        f = open(path,'w')
        f.write(page_tmp(thead,tbody,reverse))
    except IOError as e:
        print '写入文件失败: %s' % e
    else:
        f.close()
        print "请访问页面查看结果: %s" % path


if __name__ == '__main__':
    num_list1 = [(1, 4), (5, 1), (2, 3), (10, 2), (6, 3)]
    max_num_sort(num_list1)
    num_list2 = [(11, 4), (5, 1), (2, 3), (10, 2), (6, 3),(23,4,43,4),(34,45),(1,1,1,1,1)]
    print list_sort(num_list2)
    num1,num2 = random_list(6),random_list(10)
    print '随机生成列表: %s' % num1
    #按元祖中的最大值进行排序
    print '按最大值排序: %s' % list_sort(num1)
    # #按元祖中的最小值进行排序
    print '按最小值排序: %s' % list_sort(num1, True)

    '''生成页面展示排序结果

    参数一: num2 随机生成列表,列表中的每个元素为一个元祖,也是随机生成,参数为生成的个数
    参数二: path 指定文件生成路径,若文件路径错误会触发异常
    参数三: 默认为False,即按列表中每个元祖的最大值进行排序;True,即为按列表中每个元祖的最小值进行排序

    '''
    path = '/home/op/test/index.html'
    create_page(num2,path,True)

