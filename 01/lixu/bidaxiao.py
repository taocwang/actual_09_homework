#!/usr/local/bin/python2.7 python
#Filename : bidaxiao.py
#Author : LiXu
#Date : 2016/04/19

nums = [1,2,3,2,12,3,1,3,21,2,2,3,4111,22,3333,444,111,4,5,777,65555,45,33,45] 
num = nums[0]
num1 = nums[0]
for i in nums:
	if num < i :
		num = i
for j in nums:
	if num != j  and num1 < j :
                num1 = j
print  num,num1

'''
功能ok， 可考虑下用一次循环得到结果的情况
'''