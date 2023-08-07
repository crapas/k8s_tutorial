from flask import Flask, request
import socket

app = Flask(__name__)

@app.route('/')
def get_host_name():
    query_params = request.args
    if len(query_params) == 0:
        return f"Hostname: {socket.gethostname()}"
    else:
        return f"Hostname: {socket.gethostname()}, QueryParams: {query_params}"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)