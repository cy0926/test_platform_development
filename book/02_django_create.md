### manage 常用命令
```
# 创建项目
$ django-admin startproject mysite

# 创建应用
$ django-admin startapp polls

# 运行项目
$ python manage.py runserver

# 生成数据库同步文件
$ python manage.py makemigrations polls

# 执行数据库同步
$ python manage.py migrate

# django shell模式
$ python manage.py shell

# 创建超级管理员账号
$ python manage.py createsupper

# 运行django单元测试
$ python manage.py test


```

### django MTV 模型
* M: models, django封装了ORM，免于直接操作数据库。
* T: templates，django自带模版语言，可以在HTML中处理数据的展示。
* V: views，在models和templates之间处理数据。


### django简单处理流程
1、浏览器URL：http://127.0.0.1:8000/index
2、__urls.py__ 文件中匹配丽江 __/index/__
```
path('index/', views.index),

```
3、在__views.py__文件中定义__index()__函数，将_index.html_文件返回给客户端浏览器
```
def index(request):
    return render(request, "index.html")
```