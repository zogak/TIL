from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return "Hello World!"

@app.route('/user')
def get_user():
    return "hello USER"

@app.route('/post')
def get_post():
    return "hello POST"

@app.route('/user/list')
def get_user_list():
    return "hello USER LIST"

@app.route('/ohno')
def get_ohno():
    return "Oh No"

if __name__ == '__main__':
    app.run(debug=True)
