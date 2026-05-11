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
