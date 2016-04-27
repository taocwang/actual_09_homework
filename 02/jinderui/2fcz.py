#encoding: utf-8
num_list = range(1,101)
guess = int(raw_input(" please input number 1-100: "))

start = 0
end = len(num_list)

index = None



### 判读输入的是否正确
if guess not in num_list:
    print "input number error. please input 1-100 "
else:
### 通过中间值和输入的值进行比较。如果进来的值小于中间值就。就把索引end重新赋值，改变索引位置。重新计算出新的中间值，然后输入的值在和中间值进行比较
### 如果进来的只大于中间值，就把索引start重新赋值，改变索引位置
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