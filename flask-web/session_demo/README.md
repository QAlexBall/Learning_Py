### 操作session

1. session擦做方式
* 使用session需要从flask中导入session,以后所有和session有关的操作都是通过这个变量来的.
* 使用session需要设置SECRET_KEY,用来作为加密使用.
* 操作session和操作字典相似
* 添加session: `session['username']`
* 删除: `session.pop('username')`或者`del session['username']`
* 清除所有session: `session.clear()`
* 获取session: `session.get('username')`

2. 设置session的过期时间
```python
# 设置permanent为True的默认时间为7天
app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(days=7)
session['username'] = 'admin'
# 默认过期时间为浏览器关闭之后
# permanent设置为True后过期时间为31天
session.permanent = True
```