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

