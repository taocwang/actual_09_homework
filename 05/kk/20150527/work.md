作业
完成
1. 用户的登录
  localhost
  =>跳转到用户名/密码输入的页面

2. 显示用户的列表
3. 添加新用户
  在用户列表中添加一个超链接“新建用户”
  点击=>跳转到用户信息输入的页面

4. 修改原有用户信息
  跳转到用户的修改信息输入页面
  
5. 删除原有用户

web 开发， flask框架

1. 通过浏览器发起一个请求，给web程序提交一堆数据
   在地址栏输入url       get
   在页面上点击超链接    get
   在页面有form 通过submit按钮提交   get/post method属性控制

2. flask程序，接收提交的数据
    通过request.form 和 args接收提交数据
    request.form 用来接收post提交的数据
    request.args 用来接收get提交的数据

3. falsk程序返回内容给用户显示，字符串
    return 直接返回字符串
    return render_template 加载模板，并将一些变量渲染到模板内容



用户信息存储在文件中，使用json字符串的方式存储
json.dumps([{}, {}])
json.dumps({"" : []})

json.dumps() => list/dict => str  保存用户数据
json.loads() => str = > list/ dict  获取用户数据
