"""
environ: 一个包含所有HTTP请求信息的dict对象
start_response: 一个发送HTTP响应的函数

在application()中,调用start_reponse...,就发送了HTTP响应的Header, Header只能发送一次
"""


def application(environ, start_reponse):
    start_reponse('200 OK', [('Content-Type', 'text/html')])
    return [b'<h1>Hello, web!</h1>']


def application1(environ, start_reponse):
    start_reponse('200 OK', [('Content-Type', 'text/html')])
    body = '<h1>Hello, %s</h1>' % (environ['PATH_INFO'][1:] or 'web')
    return [body.encode('utf-8')]
