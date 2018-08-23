"""
MVC:Model-View-Controller
C: Controller python处理URL的函数,比如检查用户名是否存在,取出用户信息等等
V: View       包含{{name}}的模板,负责显示逻辑,通过简单的替换一些变量,View最终输出的就是用户看到的HTML
M: Model      Model是用来传给View的,这样View在替换变量时,就可以从Model中取出相应的数据
"""
from flask import Flask, request, render_template

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def home():
    return render_template('home.html')


@app.route('/signin', methods=['GET'])
def signin_form():
    return render_template('form.html')


@app.route('/signin', methods=['POST'])
def signin():
    username = request.form['username']
    password = request.form['password']
    if username == 'admin' and password == 'password':
        return render_template('signin-ok.html', username=username)
    return render_template('form.html', message='Bad username or password', username=username)


if __name__ == '__main__':
    app.run()
