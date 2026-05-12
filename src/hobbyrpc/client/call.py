import json
from .exceptions import BadRequest, Forbidden, UnexpectedStatus

def call(self, name, **input):
    body = {
        'fn': name,
    }

    if input:
        body['in'] = input

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
        case 400:
            raise BadRequest
        case 403:
            raise Forbidden
        case _:
            raise UnexpectedStatus(f'{response.status} in response {response}')
