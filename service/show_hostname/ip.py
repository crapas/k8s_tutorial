from flask import Flask, request
import socket

app = Flask(__name__)

@app.route('/')
def get_ip():
    query_params = request.args
    client_ip = request.remote_addr
    server_ip = socket.gethostbyname(socket.gethostname())

    if len(query_params) == 0:
        return f"Server : {server_ip}, Client: {client_ip}"
    else:
        return f"Server : {server_ip}, Client: {client_ip}, QueryParams: {query_params}"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)    