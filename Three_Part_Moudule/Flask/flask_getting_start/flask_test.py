from flask import Flask 

app = Flask((__name__))

@app.route('/')
def hello_world():
    return 'hi jack!'

@app.route('/jack/')
def hello_jack():
    return 'jack is not jack'

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=9000)

