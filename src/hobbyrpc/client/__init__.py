import json
from urllib.parse import urlparse
from http.client import HTTPConnection

class Client:
    def __init__(self, address):
        url = urlparse(address)
        match url.scheme:
            case 'http':
                self.http = HTTPConnection(url.hostname, url.port)
                self.http_path = url.path

        self.headers = {
            'Content-type': 'application/json',
        }

    def __call__(self, name):
        body = {
            'fn': name,
        }

        self.http.request(
            'POST', self.http_path,
            body=json.dumps(body),
            headers=self.headers,
        )

        response = self.http.getresponse()
        raw_data = response.read()

        match response.status:
            case 200:
                data = json.loads(raw_data.decode('utf-8'))
                return data
