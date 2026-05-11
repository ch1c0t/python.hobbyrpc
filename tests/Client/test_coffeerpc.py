from http.client import HTTPConnection
from pathlib import Path
import socket

class UnixSocketConnection(HTTPConnection):
    def __init__(self, path):
        self.socket_path = Path(path)
        super().__init__(host='0.0.0.0')

    def connect(self):
        self.sock = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
        self.sock.connect(self.socket_path.as_posix())

def test_its_response(coffeerpc_server):
    match coffeerpc_server.transport:
        case 'tcp':
            c = HTTPConnection('127.0.0.1', 8080)
        case 'unix_socket':
            c = UnixSocketConnection(coffeerpc_server.address)

    c.request('OPTIONS', '/')
    response = c.getresponse()

    assert response.status == 200

    header = response.getheader('Access-Control-Allow-Headers')
    assert header == 'Authorization, Content-Type'

# from pprint import pprint as p
# def test_its_info(coffeerpc_server):
#     p(dir(coffeerpc_server))
#     p(vars(coffeerpc_server))
