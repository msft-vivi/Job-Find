### 用户区分
* 0 表示求职者
* 1 表示企业用户

### 数据库迁移错误
* 1、删除迁移文件夹migrations.(此时若尝试执行迁移数据库命令，会报出版本出错version is xxx)
* 2、用navicat打开数据库  删除版本控制表(一个名为 alembic-version的版本控制表)
然后再执行迁移命令就会成功。
* [参考链接](https://blog.csdn.net/weixin_30770783/article/details/98003451?depth_1-utm_source=distribute.pc_relevant.none-task&utm_source=distribute.pc_relevant.none-task)

### 运行
* 初始化/更新数据库
    * python manage.py db init
    * python manage.py db upgrade
    * python manage.py db migrate
    * 如果已经存在数据库，则不需要执行init
* 运行网站
    * python manage.py runserver --threaded [-h -p]
    
### 注意
* js中的全局变量放到js的入口函数内部，尤其是与dom元素有关的变量必须放入
* .val() 是 jQuery中的方法，.value是原生的方法，jQuery方式选中元素不能用value
* text(),val()
    * text() 用于获取文本值，val()用于获取value值，一般使input
* radio 只有在name指定相同值时候是互斥的
* 可以利用 trigger("click")实现外部按钮触发form提交
* 可以利用 trigger("click")实现修改默认文件上传的样式
* textarea 如果不能换行写，否则会造成内容中的空白
### Q & A
* model写在不同的文件中，db.ForeignKey("user.id"")失效, 改为db.ForeignKey(User.id)
* url_for 在<script></script>中使用url_for的问题：
    * 如果url_for是在动态生成的html中嵌入，则必须放在 .html文件中，单独放在js文件不能有效转换
    * 会出现%7D%6B 等乱码
* jsonify(request.form) 中文乱码
    *[解决办法](https://blog.csdn.net/fo11ower/article/details/70062524)
* 用Flask 提交文件时候 input 中 需要由name = "file" 字段
* flask secure_file 中文会被过滤问题
    * [解决办法](https://www.jianshu.com/p/ecda2752e5b8)
* .py中current_app.config 获取当前app

* ajax请求后，后端redirect无效

    
###
* 切换选中状态
```javascript
    if ($(this).prop("checked")){
        $(this).prop("checked",true);
    }
    else {
        $(this).prop("checked",false);
    }
```

### TODO
* seeker提交表单后，enterpriser给seeker发送通知邮件
* 重新命名enterprise下载的resume名称，方便enterpriser归类
* enterprise 中 post_job部分内容
* 改成短信验证登录
* enterprise 修改企业信息部分
* enterpriser 查看简历后给seeker 通知
* enterpriser 查看简历后 seeker 不得修改简历
* read_resume 制作分页
* 公司没有编辑介绍时候，job_detail位置显示为none

### Reference
* [表单验证正则表达式](https://blog.csdn.net/tp851716/article/details/43451247?utm_source=copy)
* [改变SVG颜色](https://stackoverflow.com/questions/22252472/how-to-change-the-color-of-an-svg-element)
* [flask url_for 获取绝对路径](https://zhuanlan.zhihu.com/p/107978600)