### Flask-SQLAlchemy外键及关系
1. 外键
* 语法:
```python
# 用户表
'''
create table user (
    id int primary key autoincrement,
    username varchar(100) not null,
)
'''
class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(100), nullable=False)

# 文章表
'''
create table article (
    id int primary key autoincrement,
    title varchar(100) not null,
    content text not null,
    author_id int,
    foreign key `author_id` references `users.id`    
)
'''
class Article(db.Model):
    __tablename__ = 'article'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.Text, nullable=False)
    author_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    author = db.relationship('User', backref=db.backref('articles'))
```

2. 解释`author = db.relationship('User', backref=db.backref('articles'))`:
* 给`Article`这个模型添加一个`author`属性,可以访问这篇文章的作者的数据,像访问普通模型一样
* `backref`是定义反向引用,可以通过`User.articles`模型访问这个模型的所有文章