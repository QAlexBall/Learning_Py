from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search/')
def search():
    print(request.args)
    q = request.args.get('q')
    print(request.args.get('q'))
    return 'user return is %s' % q

# 默认的视图函数,智能采用get请求
# 如果你想采用post请求,需要写明
@app.route('/login/', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    elif request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        print('username: ', username, 'password: ', password)
        return 'post'

if __name__ == '__main__':
    app.run(debug=True)
