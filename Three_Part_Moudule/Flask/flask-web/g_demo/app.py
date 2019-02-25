# g对象是专门用来保存用户数据的.
# g对象在当前请求中全局存在
from flask import Flask, g, render_template, request
from utils import login_log

app = Flask(__name__)


@app.route('/')
def index():
    return 'index'

@app.route('/login/', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    else:
        username = request.form.get('username')
        password = request.form.get('password')
        if username == 'admin' and password == 'password':
            # 认为该用户登录成功
            # login_log(username)
            g.username = username
            login_log()
            return 'login success.'
        else:
            return 'username or password error.'

if __name__ == '__main__':
    app.run(debug=True)
