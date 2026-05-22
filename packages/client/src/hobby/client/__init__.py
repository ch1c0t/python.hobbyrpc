from urllib.parse import urlparse
from http.client import HTTPConnection, HTTPSConnection

from .unix import UnixSocketConnection
from .exceptions import NotImplementedScheme

class Client:
    def __init__(self, address, token=None):
        if address.startswith('/'):
            self.http = UnixSocketConnection(address)
            self.http_path = '/'
        else:
            url = urlparse(address)
            match url.scheme:
                case 'http':
                    Connection = HTTPConnection
                case 'https':
                    Connection = HTTPSConnection
                case _:
                    raise NotImplementedScheme(f'#{url.scheme} of #{url}')
            self.http = Connection(url.hostname, url.port)
            self.http_path = url.path

        self.headers = {
            'Content-Type': 'application/json',
        }

        if token:
            self.headers['Authorization'] = token

from .call import call
Client.__call__ = call
