"""
Get /: index, back to home
Get / signin: signin page show forms
POST / signin: handle signin forms, show signin result

Flask通过Python的装饰器在内部自动地把URL和函数结合起来
"""
from flask import Flask
from flask import request

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def home():
    return '<h1>Home</h1>'


@app.route('/signin', methods=['GET'])
def signin_form():
    return '''<form action="/signin" method="post">
			<p><input name="username"></p>
			<p><input name="password"></p>
			<p><button type="submit">Sign In</button></p>
			</from>'''


@app.route('/signin', methods=['POST'])
def signin():
    # need read forms content from request
    if request.form['username'] == 'admin' \
            and request.form['password'] == 'password':
        return '<h3>Hello, admin<h3>'
    return '<h3>Bad username or password.</h3>'


if __name__ == '__main__':
    app.run()
