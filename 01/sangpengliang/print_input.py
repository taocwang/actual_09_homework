#encoding: utf-8

works = []
while True:
    _action = raw_input('你要干嘛？（add=》添加，do=>执行）：')
    if _action == 'add':
        _work = raw_input('请输入工作内容：')
        works.append(_work)
    elif _action == 'do':
        if len(works) == 0:
            print '没有工作内容'
        else:
            print '工作内容：%s' % works.pop(0)
    elif _action == 'exit':
        if len(works) != 0:
            print '还有工作未完成，你别跑'
        else:
            break

    else:
        print '你输入不正确'