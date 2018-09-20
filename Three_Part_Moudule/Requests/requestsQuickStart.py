# coding=utf-8
import json, requests


"""
# 尝试获取某个网页
# r = requests.get('https://api.github.com/events')
# 现在,有一个名为r的Response对象,可以从这个对象中获取所有想要的信息
发送一个HTTP POST请求: r = requests.post('http://www.example.com/post', data = {'key': 'value'})
PUT: r = requests.put('http://http://www.example.com/put', data = {'key', 'value'})
DELETE: r = requests.delete('http://www.example.com/delete')
HEAD: r = requests.head('http://www.example.com/get')
OPTIONS: r = requests.options('http://www.baidu.com/get')

# print(r.content)
# print(r.url) # https://api.github.com/events

# 传递URL参数
payload = {'key1': 'value1', 'key2': 'value2'}
r = requests.get('http://baidu.com/get', params=payload)
# print(r.url)  # http://example.com/get?key1=value1&key2=value2

payload = {'key1': 'value1', 'key2': ['value2', 'value3']}
r = requests.get('http://baidu.com/get', params=payload)
# print(r.url) # http://httpbin.org/get?key1=value1&key2=value2&key2=value3

url = 'http://api.github.com/some/endpoint'
payload = {'some': 'data'}

r = requests.post(url, data=json.dumps(payload))
r = requests.post(url, json=payload)
"""

# 响应内容
r = requests.get('https://api.github.com/events')
print(r.text)
print(r.encoding)
r.encoding = 'ISO-8859-1'
print(r.encoding)
