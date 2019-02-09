from flask import Flask, render_template

app = Flask(__name__)

# for遍历字典

# @app.route('/')
# def index():
#     user = {
#         'username': 'admin',
#         'age'     : 20
#     }
#     websites = ['baidu.com', 'google.com']
#     return render_template('index.html', user=user,websites=websites)

@app.route('/')
def index():
    books = [
        {
        'name': u'西游记',
        'author': u'吴承恩',
        'price': 109,
        },
        {
         'name': u'红楼梦',
         'author': u'曹雪芹',
         'price': 200,
        },
    ]
    return render_template('index.html', books=books)

if __name__ == '__main__':
    app.run(debug=True)
