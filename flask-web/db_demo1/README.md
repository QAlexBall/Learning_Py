### Flask-SQLAlchemy的使用
1. 初始化和设置数据库配置信息:
* 使用`flask-sqlalchemy`中的SQLAlchemy进行初始化:
```python
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
db = SQLAlchemy(app)
```
2. 设置配置信息: 在`config.py`文件中添加一下配置信息:
```python
DIALECT = 'mysql'
DRIVER = 'mysqldb'
USERNAME = 'root'
PASSWORD = 'password'
HOST = '127.0.0.1'
PORT = '3306'
DATABASE = 'db_demo1'

SQLALCHEMY_DATABASE_URI = "{}+{}://{}:{}@{}:{}/{}?charset=utf8".format(
    DIALECT, DRIVER, USERNAME, PASSWORD, HOST, PORT, DATABASE)

SQLALCHEMY_TRACK_MODIFICATIONS = False
```
3. 在主app问价中,添加配置文件:
```python
app = Flask(__name__)
app.config.from_object(config)
db = SQLAlchemy(app)
```
4. 测试
```python
db.create_all()
```