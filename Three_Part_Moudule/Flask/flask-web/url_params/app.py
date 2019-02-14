from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'

# 参数的作用: 可以在相同的URL,但是指定不同的参数,来加载不同的数据.
@app.route('/article/<id>')
def article(id):
    return u'参数是%s' % id

if __name__ == '__main__':
    app.run(debug=True)
