# encoding: utf-8

num_list = [1,12,9,10,11,3,5,7,2,1,3,33,44,22,66]

for i in range(1,len(num_list)):
## ÿ��һ��ѭ��iΪ1��ʱ�򣬲������б���[1]��Ӧnum_list��ֵ��12.if�Ƚ�Ҳ����12<1 ��Ȼ��С����ѭ��
## ���ڶ���ѭ��iΪ2��ʱ��.�������б���[2,1]��Ӧnum_list��ֵ��9,12 if�Ƚ�Ҳ���� 9<12�͵���λ�á�Ȼ������ѭ��ֱ�����
        for j in range(i,0,-1):
#               print j
                if num_list[j] < num_list[j - 1]:
                        num_list[j],num_list[j - 1] = num_list[j - 1],num_list[j]
#       print num_list

print num_list