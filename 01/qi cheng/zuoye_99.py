#! /usr/bin/python
# Author : qicheng
# Date : 2016/04/18 14:00

print '\n9x9 Table\n'

for i in range(1, 10) :
    for j in range(1, i+1) :
            print j, 'x', i, '=', j*i, '\t',
	    # print '%d x %d = %d\t' %(j, i, j*i),
    print '\n'

print '\nDone!'

'''
功能ok
'''