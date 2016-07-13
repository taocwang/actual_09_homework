# 今天课程
##1、js
1. js: 前端动态控制
1.1. 变量的定义
    var name = '谭帥';

1.2. 数据类型
    dict:{key:value}
    list:['1',1,true,['2']]
    None:null
    str:'abc'
    int:112358
    float:1.01
    boolean:true,false

1.3. 四则运算
```
boolean 运算:
    var score_1 = 10, score_2 = 55;
    console.log(score_2 + score_1);
    console.log(score_2 - score_1);
    console.log(score_2 * score_1);
    console.log(score_2 / score_1);
```
1.4 逻辑表达式
    or:一个为true则为true            ||
    and:两个都为true则true           &&
    not:true=>false, false=>true     !

1.5. 条件表达式
    >, <, =, !=, >=, <=
**例子一：**
```
        var name = prompt('请输入你的名字：');
        if ('谭帥' == name){
            alert('正确');
        }else if('kk' == name) {
            alert('kk')
        }else{
            alert('错误');
        }
```

**例子二：**
```
        var nums = prompt('请输入成绩：')
        if (80 <= nums){
            alert('成绩优秀')
        }else if (60 <= nums  && 80 >= nums){
            alert('成绩及格')
        }else if (60 >= nums){
            alert('成绩不及格')
        }
```

1.6. 循环表达式
1.6.1. 判断输入字符串
```
        var name = prompt('请输入你的名字：');
        if ('谭帥' == name){
            alert('正确');
        }else if('kk' == name) {
            alert('kk')
        }else{
            alert('错误');
        }
```
1.6.2. 判断输入成绩
```
        var nums = prompt('请输入成绩：')
        if (80 <= nums){
            alert('成绩优秀')
        }else if (60 <= nums  && 80 >= nums){
            alert('成绩及格')
        }else if (60 >= nums){
            alert('成绩不及格')
        }
```
1.6.3. while 判断
```
        var name = prompt('请输入你的名字：');
        while( 'kk' != name){
            alert('错误，请重新输入！')
            var name = prompt('请输入你的名字：');
        }
        alert('成功！')
```
1.6.4. do/while 判断
```
        do {
            var input = prompt('请输入你的名字')
            if (input == 'kk'){
                alert('成功');
            }else{
                alert('错误，请重新输入');
            }
        }while(input != 'kk');
```
1.6.5. for语法
```
        //学习js的for语句
        for (var i = 0; i <= 10; i++){
            console.log(i);
        }
```

1.7. 函数
1.7.1 js加法函数
```
//parseInt有两个参数，自己查询一下第二个参数的作用是什么？
        function add(num1,num2){
            return parseInt(num1) + parseInt(num2)
        }
        num1 = prompt('请输入第一个数字')
        num2 = prompt('请输入第二个数字')
        alert(add(num1,num2))
```
1.8 js知识点
a. 标签绑定事件
b. 调用函数处理
c. 给用户回显
d. 获取标签元素
```
        tag => jQuery('tag')
        id => jQuery('#id')
        class => jQuery('.class')
```

##2、js组件
2.









##2、模版继承
##3、开发流程
##4、cmdb开头