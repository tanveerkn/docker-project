from flask import Flask, request, Response,render_template
import time
import sys

sys.setrecursionlimit(10**6)

app = Flask(__name__)


@app.route('/')
def hello_world():
    res = "Hello from %s:%s to %s:%s" % (
        request.environ['REMOTE_ADDR'], request.environ['REMOTE_PORT'], request.environ['SERVER_NAME'],
        request.environ['SERVER_PORT'])
    return res



@app.route('/fib/<int:x>', methods=['POST'])
def fib(x):
    return str(calcfib(x))
def calcfib(n):
    n = request.json
    if n is not None:
        n = int(n['number'])
        if n == 0:
            resp_msg = "{'Error': 'zero'}"
            return resp_msg
	elif n<0:
	    resp_msg = "{'Error: 'Negative Number''}"
	    retutn resp_msg	
        b, a = 0, 1             # b, a initialized as F(0), F(1)
        for i in range(1,n) :
            b, a = a, a+b       # b, a always store F(i-1), F(i)
        return a

###########################################################################################


@app.route("/template")
def template():
    return render_template("index.html")

@app.route("/getTime", methods=['GET'])
def getTime():
    print("browser time: ", request.args.get("time"))
    print("Boot time : ", time.strftime('%A %B, %d %Y %H:%M:%S'));
    return "Done"
########################################################################################


def shutdown_server():
    func = request.environ.get('server.shutdown')
    if func is None:
        raise RuntimeError('Server not Running')
    func()


@app.route('/shutdown', methods=['POST'])
def shutdown():
    shutdown_server()
    return 'Server shutting down...'



if __name__ == '__main__':

    app.run(host='0.0.0.0', port=8002)


