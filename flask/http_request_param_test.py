from flask import Flask, request

app = Flask(__name__)

@app.route('/query')
def index():
    args = request.args

    id = args.get('id') #id를 꺼내오기
    date = args.get('date')
    print(id)
    print(date)

    return "Query String!"

@app.route('/path/<param1>/<param2>')
def path_param(param1, param2):
    print(param1)
    print(param2)

    return "path param"

@app.route('/body', methods=['POST'])
def request_body():
    print(request.json)

    body = request.json
    id = body['id']
    name = body['name']

    print(id)
    print(name)

    return "request body!"


if __name__ == '__main__':
    app.run(debug=True)