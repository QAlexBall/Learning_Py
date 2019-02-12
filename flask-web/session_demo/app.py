from flask import Flask, session
import os
from datetime import timedelta

app = Flask(__name__)
# 24个字符的字符串
app.config['SECRET_KEY'] = os.urandom(24)
# 设置permanent为True的默认时间为7天
app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(days=7)

# 添加数据到session中
# 操作session的时候,跟操作字典是一样的.
# SECRET_KEY

@app.route('/')
def hello_world():
    session['username'] = 'admin'
    # 默认过期时间为浏览器关闭之后
    # permanent设置为True后过期时间为31天
    session.permanent = True
    return 'Hello World!'

@app.route('/get/')
def get():
    return session.get('username')

@app.route('/delete/')
def delete():
    print(session.get('username'))
    session.pop('username')
    print(session.get('username'))
    return 'success'

@app.route('/clear/')
def clear():
    print(session.get('username'))
    # 删除session中的所有数据
    session.clear()
    print(session.get('username'))
    return 'success'

if __name__ == '__main__':
    app.run(debug=True)
