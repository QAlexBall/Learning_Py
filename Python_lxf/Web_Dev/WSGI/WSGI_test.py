"""
Web应用的本质
1.浏览器发送一个HTTP请求
2.服务器收到请求,生成一个html文档
3.服务器把html文档作为http响应的Body发送给浏览器
4.浏览器收到http响应,从http Body取出html文档并显示

WSGI接口定义,只需要Web开发这实现一个函数,就可以响应HTTP请求
"""
from wsgiref.simple_server import make_server
from hello import application1

httpd = make_server('', 8000, application1)
print('Server HTTP on port 8000...')
httpd.serve_forever()

