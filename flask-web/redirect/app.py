from flask import Flask, redirect, url_for

app = Flask(__name__)


@app.route('/')
def index():
    login_url = url_for('login')
    return redirect(login_url)
    return 'Home'

@app.route('/login/')
def login():
    return 'login'

@app.route('/question/<is_login>')
def question(is_login):
    if is_login == '1':
        return 'question'
    else:
        return redirect(url_for('login'))
if __name__ == '__main__':
    app.run(debug=True)
