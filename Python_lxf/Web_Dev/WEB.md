### WSGI
Web Server Gateway Interface

WSGI的接口定义非常简单,只要求实现一个函数,就可以响应HTTP请求.
```python
def application(environ, start_reponse):
	start_reponse('200 OK', [('Content-Type', 'text/html')])
	return [b'<h1>Hello, web!</h1>']
```
上面的application()函数就是符合WSGI标准的一个HTTP处理函数,它接受两个参数:
* environ: 一个包含所有HTTP请求信息的dict对象;
* start_response: 一个发送HTTP响应的函数

在application()函数中,调用:
start_response('200, OK', [('Content-Type', 'text/html')])
就发送了HTTP响应的Header,Header只能发送一次,也就是只能调用一次start_response()函数.start_response()函数接受两个参数,一个是HTTP响应码,一个是一组list表示的HTTPHeader,每个Header用一个包含两个str的tuple表示.

PYthon内置一个WSGI服务器,这个模块叫wsgiref.

不管多么复杂的Web应用程序,入口都是一个WSGI处理函数.HTTP请求的所有输入信息都可以通过environ获得, HTTP响应的输出都可以通过start_response()加上函数返回值作为Body.

Flask通过Python的装饰器在内部自动把URL和函数关联起来.

### 使用模版
模版技术, 使用模版我们需要预先准备一个HTML文档,这个HTML文档不是普通的HTML,而是嵌入了一些变量和指令, 然后,根据我们传入的数据替换后,得到最终的html,发送给用户
MVC: Model-View-Controller(模型-视图-控制器)
Python处理URL的函数就是C: Controller, Controller负责业务逻辑,比如检查用户名是否存在,取出用户信息等等;
包含变量{{name}}的模版就是V: View, View负责显示逻辑,通过简单地替换一些变量,View最终输出的就是用户看到的HTML
Model是用来传给View的,这样View在替换变量的时候,就可以从Model中取出相应的数据
上面的例子中,Model就是一个dict:
{'name': 'Michael'}
只是因为Python支持关键字参数,很多Web框架允许传入关键字参数,然后,在框架内部组装出一个dict作为Model.
Flask通过render_remplate()函数来实现模版的渲染.















