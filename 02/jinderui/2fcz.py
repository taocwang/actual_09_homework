#encoding: utf-8
num_list = range(1,101)
guess = int(raw_input(" please input number 1-100: "))

start = 0
end = len(num_list)

index = None



### �ж�������Ƿ���ȷ
if guess not in num_list:
    print "input number error. please input 1-100 "
else:
### ͨ���м�ֵ�������ֵ���бȽϡ����������ֵС���м�ֵ�͡��Ͱ�����end���¸�ֵ���ı�����λ�á����¼�����µ��м�ֵ��Ȼ�������ֵ�ں��м�ֵ���бȽ�
### ���������ֻ�����м�ֵ���Ͱ�����start���¸�ֵ���ı�����λ��
    while  True:
    	middle = (start + end) /2
    	if num_list[middle] == guess:
    		index = middle
    		print "%s index is %s" %(guess,index)
    		break
    	elif num_list[middle] > guess:
    		end = middle -1
    	else: 
    		start = middle + 1