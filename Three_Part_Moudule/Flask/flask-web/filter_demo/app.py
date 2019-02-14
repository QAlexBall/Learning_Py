from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    comments = [
        {
            'user': 'admin',
            'content': 'xxx',
        },
        {
            'user': 'admin1',
            'content': 'xxx1',
        },
    ]
    return render_template('index.html', comments=comments)


if __name__ == '__main__':
    app.run(debug=True)
