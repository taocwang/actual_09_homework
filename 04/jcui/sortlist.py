#encoding:utf-8

def default_cmp(x,y):
    if x>y:
        return True
    else:
        return False
def default_key(x):
    return x

def list_sort(lists,key=default_key,cmp=default_cmp):      #key默认只对纯数字的列表比较
    for n in range(len(lists)-1):
        for i in range(len(lists)-1):
            if cmp(key(lists[i]),key(lists[i+1])):
                lists[i], lists[i + 1] = lists[i + 1], lists[i]
    return lists

print __name__

if __name__ == '__main__':
    print '123123123'