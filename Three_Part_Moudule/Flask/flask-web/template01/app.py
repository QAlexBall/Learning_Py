from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    class Person(object):
        name = 'admin'
        age = 18

    p = Person()

    context = {
        'username': 'admin',
        'gender'  : 'male',
        'age'     : 20,
        'person': p,
        'websites': {
            'baidu': 'www.baidu.com',
            'google': 'www.google.com',
        },
    }
    return render_template('index.html', **context)


if __name__ == '__main__':
    app.run(debug=True)
