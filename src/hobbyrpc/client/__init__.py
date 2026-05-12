from urllib.parse import urlparse
from http.client import HTTPConnection
from .unix import UnixSocketConnection

class Client:
    def __init__(self, address, token=None):
        if address.startswith('/'):
            self.http = UnixSocketConnection(address)
            self.http_path = '/'
        else:
            url = urlparse(address)
            match url.scheme:
                case 'http':
                    self.http = HTTPConnection(url.hostname, url.port)
                    self.http_path = url.path

        self.headers = {
            'Content-type': 'application/json',
        }

        if token:
            self.headers['Authorization'] = token

from .call import call
Client.__call__ = call
