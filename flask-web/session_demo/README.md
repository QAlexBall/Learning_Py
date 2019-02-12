### 操作session

1. session擦做方式
* 使用session需要从flask中导入session,以后所有和session有关的操作都是通过这个变量来的.
* 使用session需要设置SECRET_KEY,用来作为加密使用.
* 操作session和操作字典相似
* 添加session: `session['username']`
* 删除: `session.pop('username')`或者`del session['username']`
* 清除所有session: `session.clear()`
* 获取session: `session.get('username')`
