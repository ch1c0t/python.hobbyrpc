from hobbyrpc import Server

CORS = {
    'origins': [
        'https://allowed.domain',
        'https://web.allowed.domain',
    ]
}

rpc = Server(
    CORS=CORS,
)

@rpc.fun
class SomeFunction:
    def call(self):
        return ['custom', 'origins']
