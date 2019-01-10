### Redis介绍
Redis最为常用的数据类型主要有一下五种:
* String
* Hash
* List
* Set
* Sorted set


### python操作redis
##### redis连接
redis提供两个类Redis和StricRedis用于实现Redis命令,StrictReids用于实现大部分官方命令,并使用官方的语法和命令,Redis是StrictRedis的子类,用于向后兼容旧版的redis-py
redis连接实例是线程安全的,可以将redis连接实例设置为一个全局变量,直接使用.如果需要另一个Redis实例(or Redids数据库)时,就需要重新创建redis连接实例来获取一个新的连接.同理,python的redis没有实现select命令.

* **redis1.py**
```python
# 连接redis,加上decode_responses=True,写入的键值对中value为str类型,不加这个参数写入的则为字节类型
import redis
r = redis.Redis(host='localhost', port=6379, decode_responses=True)
r.set('name', 'alex')
print(r['name'])
print(r.get('name')) # 取出键name对应的值
print(type(r.get('name')))
"""
output:
➜  redis git:(master) ✗ python redis1.py
alex
alex
<class 'str'>
"""
```

##### 连接池
redis-py使用connect pools来管理对一个redis server的所有连接,避免每次建立,释放连接的开销.默认,每个Redis实例都会维护一个自己的连接池.可以直接建立一个连接池,然后作为参数Redis,这样就可以实现多个Redis实例共享一个连接池
* **redis2.py**
```python
import redis

pool = redis.ConnectionPool(host='localhost', port=6379, decode_responses=True)
r = redis.Redis(connection_pool=pool)
r.set('gender', 'male')
print(r.get('gender'))
```
##### redis基本命令String
set(name, value, ex=None, nx=False, xx=False)
在Redis中设置值,默认,不存在创建,存在则修改参数:
ex, 过期时间(秒)
px, 过期时间(毫秒)
nx, 如果设置为True,则只有name不存在时,当前set操作才执行
xx, 如果设置为True,则只有name存在时,当前set操作才执行
