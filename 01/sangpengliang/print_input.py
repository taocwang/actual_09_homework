#encoding: utf-8

works = []
while True:
    _action = raw_input('��Ҫ�����add=����ӣ�do=>ִ�У���')
    if _action == 'add':
        _work = raw_input('�����빤�����ݣ�')
        works.append(_work)
    elif _action == 'do':
        if len(works) == 0:
            print 'û�й�������'
        else:
            print '�������ݣ�%s' % works.pop(0)
    elif _action == 'exit':
        if len(works) != 0:
            print '���й���δ��ɣ������'
        else:
            break

    else:
        print '�����벻��ȷ'