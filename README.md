#这是一个开发中的论坛
### 1、添加了模板
- 模板已被我使用过
- 注意模板的问题
### 2、添加了主题的models，显示主题主页面

### ...后面的具体步骤暂时不更新了

### 3、 添加了operation的app（评论），添加了富文本编辑器插件

### ......

### 4、**整合了forum项目**
------
#项目已经实现的功能：
>* 用户注册与登录
>* 用户信息的修改与补充，包括头像和用户名的修改
>* 用户密码的修改
>* 显示主题页及其详情内容
>* 发表评论及在文章详情页显示评论
>* 发布主题
>* 板块的划分及标签的绑定
>* 可以显示某个板块包含的详情主题及标签下的主题
>* 主题的修改与删除
>* 富文本编辑的实现
>* 显示个人用户下的主题
>* 代码高亮
>* 全论坛搜索功能
>* 显示论坛的用户注册数、主题数及回复数
------
#项目的漏洞：
>* 不能修改主题标签
>* 不能上传本地图片，即只能以链接形式上传图片
>* 板块下没有主题时访问该板块会出现错误，新建板块必须要在该板块新增主题
>* 当主页只有一页时显示的是两个“1”页
>* 用户可以多IP同时登陆,关闭浏览器用户不会自动退出
>* 主题阅读量没有限定，主题作者访问也会自增
>* 热议主题的排序是按照阅读量的数目排序，而不是按照综合因素排序
>* “专栏”页面各板块下的主题没有合理的排列
...
------
#项目未实现的功能：
-[ ] 在线人数的显示
-[ ] 用户的多级评论
-[ ] 问答专栏
-[ ] 热门专栏
-[ ] 技术专栏
-[ ] 用户密码找回
-[ ] 使用第三方账户登录
-[ ] 评论的提醒功能
-[ ] 主题收藏
-[ ] 用户互粉
-[ ] 举报功能
-[ ] 顶置功能...