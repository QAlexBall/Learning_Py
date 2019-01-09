```bash
➜  Django git:(master) ✗ django-admin startproject mysite
➜  mysite git:(master) ✗ tree 
.
├── manage.py
└── mysite
    ├── __init__.py     一个空文件告诉python这个目录应该被认为是一个Python包
    ├── settings.py     Django项目配置文件
    ├── urls.py         Django项目URL声明
    └── wsgi.py         作为项目运行在WSGI兼容的Web服务器上的入口
 ➜  mysite git:(master) ✗ python manage.py runserver
 ```
 
### 创建投票应用
##### 项目VS应用
应用是一个专门做某件事的网络应用程序——比如博客系统，或者公共记录的数据库，或者简单的投票程序。
项目则是一个网站使用的配置和应用的集合。项目可以包含很多个应用。应用可以被很多个项目使用。
```bash
➜  mysite git:(master) ✗ python manage.py startapp polls
➜  polls git:(master) ✗ tree
.
├── admin.py
├── apps.py
├── __init__.py
├── migrations
│   └── __init__.py
├── models.py
├── tests.py
└── views.py

1 directory, 7 files
```
##### 编写第一个视图
* polls/views.py
* 为了创建URLconfs,在polls目录里创建一个urls.py
```python
from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
]
```
* 下一步是要在根URLconf文件中指定创建的polls.urls模块,在mysite/urls.py文件的urlpatterns列表里插入一个include(),如下
```python
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path(route='polls/', view=include('polls.urls')),
    path('admin/', admin.site.urls),
]
```
函数include()允许引用其他URLconfs.

***** path()
path()具有四个参数,两个必选参数:route和view,两个可选参数kwargs和name
* route
route是一个匹配URL的准则(类似正则表达式).当Django响应一个请求时它会从urlpatterns的
第一项开始,按顺序依次匹配列表中的项,直到找到匹配的项
* view
当Django找到了匹配的准则,就会调用这个特定的视图参数,并传入一个HTTPRequest对象作为第一个参数,
被"捕获"的参数以关键字的形式传入
* kwargs
任意个关键字参数可以作为一个字典传递给目标视图函数
* name
为URL取名使得在Django的任意地方唯一地引用它,尤其是在模板中
