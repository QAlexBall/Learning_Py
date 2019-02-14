### Flask-SQLAlchemy多对多
* 多对多的关系,需要通过一个中间表进行关联.
* 中间表,不能通过`class`的方式实现,只能通过`db.Table`的方式实现
* 设置关联:
```python
tags = db.relationship('Tag', secondary=article_tag, backref=db.backref('articles'))
```
需要使用一个关键字参数`seconddary=中间表`来进行关联
* 访问和数据添加可以通过一下方式进行操作:
```python
# 添加数据
    article1 = Article(title='aaa')
    article2 = Article(title='bbb')
    
    tag1 = Tag(name='111')
    tag2 = Tag(name='222')
    
    article1.tags.append(tag1)
    article1.tags.append(tag2)
    
    article2.tags.append(tag1)
    article2.tags.append(tag2)
    
    db.session.add(article1)
    db.session.add(article2)
    
    db.session.add(tag1)
    db.session.add(tag2)

    db.session.commit()
# 访问数据:
    article1 = Article.query.filter(Article.title == 'aaa').first()
    tags = article1.tags
    for tag in tags:
        print('-'*10)
        print(tag.name)

```