from flask import Flask, render_template, request, session, redirect, url_for, g
import config
from extensions import db
from models import Article

app = Flask(__name__)
app.config.from_object(config)
db.init_app(app)

@app.route('/')
def hello_world():
    print('index')
    # article1 = Article(title='aaa', content='bbb')
    # db.session.add(article1)
    # db.session.commit()
    return render_template('index.html')

@app.route('/login/', methods=('GET', 'POST'))
def login():
    print('login')
    if request.method == 'GET':
        return render_template('login.html')
    else:
        username = request.form.get('username')
        password = request.form.get('password')
        if username == 'admin' and password == 'password':
            session['username'] = 'admin'
            return 'login success!'
        else:
            return 'username or password error!'

@app.route('/edit/')
def edit():
    if hasattr(g, 'username'):
        print('article_id is: ', g.article_id)
        return render_template('edit.html')
    else:
        return redirect(url_for('login'))


# before_request: 在请求之前执行的
# before_request: 是在视图函数执行之前执行的
# before_request: 这个函数只是一个装饰器,它可以把需要设置为钩子函数的代码放到视图函数执行之前执行
# 可以利用g率先存储数据库查询内容,避免反复查询消耗资源.
@app.before_request
def my_before_request():
    if session.get('username'):
        g.username = session.get('username')
    article_id = Article.query.filter(Article.title == 'aaa').first()
    g.article_id = article_id

# 上下文处理器应该返回一个字典.字典中的`key`会在模板中被当成变量来渲染.
# 上下文处理器返回的字典,在所有页面都是可用的.

@app.context_processor
def my_context_processor():
        return {'username': 'admin'}

if __name__ == '__main__':
    app.run(debug=True)

