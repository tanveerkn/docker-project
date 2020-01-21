from flask import Flask, request
import requests

app = Flask(__name__)


@app.route('/')
def hello_world():
    res = "Hello from %s:%s to %s:%s" % (
        request.environ['REMOTE_ADDR'], request.environ['REMOTE_PORT'], request.environ['SERVER_NAME'],
        request.environ['SERVER_PORT'])
    response = requests.get('http://service2:8002/')
    print(response.text)
    return res


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8001)
