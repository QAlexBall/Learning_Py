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

##### path()
path()具有四个参数,两个必选参数:route和view,两个可选参数kwargs和name
* route:
route是一个匹配URL的准则(类似正则表达式).当Django响应一个请求时它会从urlpatterns的
第一项开始,按顺序依次匹配列表中的项,直到找到匹配的项
* view:
当Django找到了匹配的准则,就会调用这个特定的视图参数,并传入一个HTTPRequest对象作为第一个参数,
被"捕获"的参数以关键字的形式传入
* kwargs:
任意个关键字参数可以作为一个字典传递给目标视图函数
* name:
为URL取名使得在Django的任意地方唯一地引用它,尤其是在模板中

#### 数据库配置
打开mysite/settings.py.这是包含了Django项目设置的Python模块
通常这个配置文件使用SQLite作为默认浏览器.
* ENGINE -- 可选值有 'django.db.backends.sqlite3'， 'django.db.backends.postgresql'，'django.db.backends.mysql'， 'django.db.backends.oracle'。
* NAME - 数据库的名称。
* 如果使用的是 SQLite，数据库将是你电脑上的一个文件，在这种情况下， NAME 应该是此文件的绝对路径，包括文件名。**默认值 os.path.join(BASE_DIR, 'db.sqlite3') 将会把数据库文件储存在项目的根目录**
通常， INSTALLED_APPS 默认包括了以下 Django 的自带应用：

* django.contrib.admin -- 管理员站点， 你很快就会使用它。
* django.contrib.auth -- 认证授权系统。
* django.contrib.contenttypes -- 内容类型框架。
* django.contrib.sessions -- 会话框架。
* django.contrib.messages -- 消息框架。
* django.contrib.staticfiles -- 管理静态文件的框架。

```bash
➜  myweb git:(master) ✗ python manage.py migrate
```
这个migrate命令检查INSTALLED_APPS设置,为其中的每个应用穿件需要的数据表.

#### 创建模型
在Django里写一个数据库驱动的Web应用第一步是定义模型-也就是数据库结构设计和附加的其他元数据.
```python
from django.db import models

# Create your models here.
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('data published')

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
```
#### 激活模型
* 为这个应用创建schema(生成CREATE TEABLE语句).
* 创建可以与Question和Choice对象进行交互的Python数据库API
但是首先得把polls应用安装到项目里面
为了在我们的工程中包含这个应用,我们需要配置类INSTALL_APPS中添加设置.
因为PollsConfig类写在polls/apps.py中,所以它的点式路径是'polls.apps.PollsConfig'.
在文件mysite/settings.py中INSTALL_APPS添加点式路径.