### 用户区分
* 0 表示求职者
* 1 表示企业用户

### 数据库迁移错误
* 1、删除迁移文件夹migrations.(此时若尝试执行迁移数据库命令，会报出版本出错version is xxx)
* 2、用navicat打开数据库  删除版本控制表(一个名为 alembic-version的版本控制表)
然后再执行迁移命令就会成功。
* [参考链接](https://blog.csdn.net/weixin_30770783/article/details/98003451?depth_1-utm_source=distribute.pc_relevant.none-task&utm_source=distribute.pc_relevant.none-task)

### 注意
* js中的全局变量放到js的入口函数内部，尤其是与dom元素有关的变量必须放入
* .val() 是 jQuery中的方法，.value是原生的方法，jQuery方式选中元素不能用value
* text(),val()
    * text() 用于获取文本值，val()用于获取value值，一般使input
### Q & A
* model写在不同的文件中，db.ForeignKey("user.id"")失效, 改为db.ForeignKey(User.id)
* url_for 在<script></script>中使用url_for的问题：
    * 如果url_for是在动态生成的html中嵌入，则必须放在 .html文件中，单独放在js文件不能有效转换
    * 会出现%7D%6B 等乱码
    
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
