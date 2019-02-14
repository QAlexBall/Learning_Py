### Flask-SQLAlchemy数据的增,删,改,查
1. 增:
```python
    # add:
    article1 = Article(title='aaa', content='bbb')
    db.session.add(article1)
    # 事务
    db.session.commit()
```
2. 查:
```python
    # 查
    # select * from article where title='aaa';
    article1 = Article.query.filter(Article.title == 'aaa').first()
    print('title:%s' % article1.title)
    print('content:%s' % article1.content)
    # article1 = result[0]
    # print(article1.title, article1.content)
```
3. 改:
```python    # 改:
    '''
    # 1. 先把要修改的数据查找出来
    article1 = Article.query.filter(Article.title == 'aaa').first()
    # 2. 把这条数据,需要的地方修改
    article1.title = 'new title'
    # 3. commit
    db.session.commit()
    '''
```
4. 删:
```python
    '''
    # 1. 查找需要删除的数据
    article1 = Article.query.filter(Article.title == 'aaa').first()
    # 2. 删除
    db.session.delete(article1)
    # 3. commit
    db.session.commit()
    '''
```